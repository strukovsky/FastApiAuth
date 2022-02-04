from base64 import b64decode, b64encode
import json
from db import User, Session
from hashlib import md5


class AuthenticationException(Exception):
    pass


def create_signature(username: str, timestamp: str) -> str:
    return str(md5(bytes(f"{username}{timestamp}", encoding="utf-8")).digest())


def get_signature_from_db(username: str):
    session = Session()
    user: User = session.query(User).filter(User.username==username).first()
    if user is None:
        raise AuthenticationException(f"No such user in database {username}")
    return create_signature(user.username, user.timestamp)


def authenticate(encoded_token) -> str:
    token = json.loads(b64decode(encoded_token))
    if (username := token.get('username')) is None:
        raise AuthenticationException("No username is provided")
    if (signature_from_request := token.get('signature')) is None:
        raise AuthenticationException("No signature is provided")
    signature_from_db = get_signature_from_db(username)
    if signature_from_db != signature_from_request:
        raise AuthenticationException("Signature is incorrect")
    return username


def create_token(username, timestamp) -> str:
    signature = create_signature(username, timestamp)
    token = {"username": username, "signature": signature}
    token_str = json.dumps(token)
    return b64encode(bytes(token_str, encoding="UTF-8")).decode("utf-8")
