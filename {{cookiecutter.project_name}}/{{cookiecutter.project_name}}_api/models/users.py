import enum
import bcrypt
import uuid

from .db import db

from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime

from flask_restful import abort


class RolesEnum(enum.Enum):
    superadmin = "superadmin"
    admin = "admin"
    user = "user"


class User(db.Model):
    """
    Basic user model
    """

    __tablename__ = '{{cookiecutter.project_name}}_users'
    __repr_attrs__ = ['email']

    id = Column(Integer, primary_key=True)

    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(RolesEnum), nullable=False, default="user")

    is_active = Column(Boolean, default=False)

    last_password_update = Column(DateTime(timezone=True), default=func.current_timestamp())
    last_login_date = Column(DateTime(timezone=True), default=func.current_timestamp())

    # Token user for password reset and first access
    temporary_token = Column(String(255))

    @staticmethod
    def get_user(user_id, current_user):
        user = User.query.filter(User.id == user_id)

        if current_user.role.value != "superadmin":
            user = user.filter(User.customer_id == current_user.customer_id)

        user = user.one_or_none()

        if not user:
            abort(404, message='User not found')

        return user

    @staticmethod
    def set_password_hash(raw_password):
        salt = bcrypt.gensalt(rounds=10)
        hashed = bcrypt.hashpw(raw_password.encode(), salt)
        return hashed.decode()

    @staticmethod
    def get_user_for_login(email, raw_password):
        user = User.query.filter_by(email=email, is_active=True).one_or_none()

        if not user:
            abort(400, message='Bad Credentials')

        password_valid = user.check_password(raw_password)

        if not password_valid:
            abort(400, message='Bad Credentials')

        user.last_login_date = func.current_timestamp()
        user.save()

        return user

    @staticmethod
    def get_user_for_reset_password(email):
        return User.query.filter(User.email == email).one_or_none()

    @staticmethod
    def validate_temporary_token(token):
        """
        Either validates the token and return the user or it raises a 404 error
        """
        user = User.query.filter(User.temporary_token == token).one_or_none()

        if not user:
            abort(404, message='Token not valid')

        return user

    def create_temporary_token(self):
        token = uuid.uuid4()
        self.temporary_token = token
        self.save()

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode(), self.password.encode())

    def save(self, password_updated=False):
        if not self.id:
            self.password = User.set_password_hash(self.password)

        if password_updated:
            self.last_password_update = func.current_timestamp()

        self.session.add(self)
        self.session.commit()

    def delete(self):
        self.session.delete(self)
        self.session.commit()
