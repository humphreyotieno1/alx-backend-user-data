#!/usr/bin/env python3
"""a module to encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """this hashes a password """
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if password is valid"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
