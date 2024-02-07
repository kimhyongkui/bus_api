from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def password_hash(pwd):
    return bcrypt_context.hash(pwd)


def verify_password(pwd, hashed_pwd):
    return bcrypt_context.verify(pwd, hashed_pwd)
