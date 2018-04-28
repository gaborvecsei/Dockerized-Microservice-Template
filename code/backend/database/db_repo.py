import os
from binascii import hexlify
from datetime import datetime
import numpy as np
from database import db_models, db


def generate_api_key() -> str:
    key = hexlify(os.urandom(16)).decode("utf-8")
    return key


def init_api_key_object(api_key: str = None) -> db_models.ApiKey:
    if api_key is None:
        api_key = generate_api_key()
    new_api_key = db_models.ApiKey(api_key=api_key,
                                   date_created=datetime.now(),
                                   date_last_used=datetime.now(),
                                   active=True)
    return new_api_key


def create_user(first_name: str, last_name: str, email: str, api_key: str = None,
                generate_random_units_for_testing: bool = False) -> None:
    new_api_key = init_api_key_object(api_key)

    available_units = 0
    used_units = 0

    if generate_random_units_for_testing:
        # This is only for testing, it should be removed
        available_units = np.random.randint(10, 100)
        used_units = np.random.randint(10, 100)

    new_user = db_models.User(first_name=first_name,
                              last_name=last_name,
                              email=email,
                              date_signed_up=datetime.now(),
                              available_units=available_units,
                              used_units=used_units,
                              api_key=new_api_key, )
    db.db_session.add(new_user)
    db.db_session.commit()


def find_user_by_api_key(api_key: str) -> db_models.User:
    user = db.db_session.query(db_models.User).join(db_models.ApiKey).filter(
        db_models.ApiKey.api_key == api_key).first()
    return user


def update_after_service_usage(user: db_models.User, unit_used: int) -> None:
    user.used_units = user.used_units + unit_used
    user.available_units = user.available_units - unit_used
    user.api_key.date_last_used = datetime.now()

    db.db_session.commit()
