#!/usr/bin/env python3
"""Module for basic auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Base 64 authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return None
        return authorization_header[len('Basic'):]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decode base 64"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64_authorization_header.encode('utf-8').decode('base64')
        except Exception:
            return None
