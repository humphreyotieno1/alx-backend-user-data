#!/usr/bin/env python3
"""module of Auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manage api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if authentication is required for the given path."""
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> None:
        """returns None"""
        key = 'Authorization'
        
        if request is None or key not in request.headers:
            return
        return request.headers.get(key)

    def current_user(self, request=None) -> None:
        """returns None"""
        return
