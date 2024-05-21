#!/usr/bin/python3
"""definition of basic auth"""
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.base import Base as B
from models.user import User as u


class BasicAuth(Auth):
    pass