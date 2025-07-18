import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "this_is_the_most_secret_key_in_the_existance_of_humanity_"
ALGORITHM = "HS256"


def create_access_token(
    data: dict, expires_delta: timedelta = timedelta(hours=2190)
):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
