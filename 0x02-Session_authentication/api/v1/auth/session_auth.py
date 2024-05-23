#!/usr/bin/env python3
"""Session authentification"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from flask import Blueprint, request, jsonify, abort
from models.user import User
import os


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """session id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[str(session_id)] = user_id
        return str(session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

    @app_views.route('/auth_session/login',
                     methods=['POST'], strict_slashes=False)
    def auth_session_login():
        """Handles session authentication login"""
        email = request.form.get('email')
        password = request.form.get('password')

        if not email:
            return jsonify({"error": "email missing"}), 400
        if not password:
            return jsonify({"error": "password missing"}), 400

        users = User.search({'email': email})
        if not users:
            return jsonify({"error": "no user found for this email"}), 404

        user = users[0]
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        from api.v1.app import auth

        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        response.set_cookie(session_name, session_id)

        return response
