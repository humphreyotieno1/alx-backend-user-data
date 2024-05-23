#!/usr/bin/env python3
"""Session authentification"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from flask import Flask, jsonify, request
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth


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

    @app_views.route('/auth_session/login',
                     methods=['POST'], strict_slashes=False)
    def session_login():
        email = request.form.get('email')
        password = request.form.get('password')

        if not email:
            return jsonify({"error": "email missing"}), 400
        if not password:
            return jsonify({"error": "password missing"}), 400

        user = User.search({'email': email})
        if not user:
            return jsonify({"error": "no user found for this email"}), 404

        if not user[0].is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        session_id = auth.create_session(user[0].id)
        user_dict = user[0].to_json()
        response = jsonify(user_dict)
        response.set_cookie(auth.session_name, session_id)

        return response
