#!/usr/bin/env python3
"""Module for basic auth"""
from api.v1.auth.auth import Auth
import base64
import binascii


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
        """decode value using base64"""
        b64_auth_header = base64_authorization_header
        if b64_auth_header and isinstance(b64_auth_header, str):
            try:
                encode = b64_auth_header.encode('utf-8')
                base = base64.b64decode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None
