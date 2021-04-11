import jwt
import uuid
from flask_restful import abort

from flask import current_app

from datetime import datetime


class JwtTokenManager:

    @staticmethod
    def encode_token(additional_token_data, token_type, expiration_delta, algorithm='HS256'):
        uid = str(uuid.uuid4())
        now = datetime.utcnow()

        secret = current_app.config["SECRET_KEY"]

        token_data = {
            'iat': now,
            'nbf': now,
            'jti': uid,
            'iss': "user_service",
            'type': token_type,
        }

        token_data['exp'] = now + expiration_delta

        token_data.update(additional_token_data)
        encoded_token = jwt.encode(
            token_data,
            secret,
            algorithm
        )

        return encoded_token, token_data

    @staticmethod
    def decode_token(token, token_type, algorithm='HS256'):

        required_claims = [
            "jti",
            "exp",
            "type",
            "user_id",
            "customer_id",
            "email",
            "role",
        ]

        secret = current_app.config["SECRET_KEY"]

        try:
            payload = jwt.decode(
                token,
                secret,
                algorithm,
                options={"require": required_claims}
            )
        except jwt.ExpiredSignatureError:
            abort(403, message="Token has expired. Please login again")
        except jwt.InvalidTokenError:
            abort(403, message="Token claims are missing or token is malformed")

        if payload["type"] != token_type:
            abort(403, message="Wrong token type")

        return payload
