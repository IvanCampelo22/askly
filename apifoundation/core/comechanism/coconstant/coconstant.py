import hashlib
from datetime import timedelta

from django.db import models


class CoConstant:
    class KDPersistence(models.IntegerChoices):
        kdInsert = 0
        kdUpdate = 1
        kdDelete = 2
        kdFilter = 3
        kdState = 4
        kdReverse = 5
        kdLoad = 6

    class KDStateBasic(models.IntegerChoices):
        kdInactive = 0
        kdActive = 1


TRANSACTION_DEFAULT = "default"
COSESSION = "CoSession"
PAGE_SIZE = 20

AUTH_TOKEN_LENGTH = 64
AUTH_TOKEN_KEY_LENGTH = 15
AUTH_TOKEN_DIGEST_LENGTH = 128
AUTH_TOKEN_HASH_FUNC = hashlib.sha512
AUTH_TOKEN_TTL_DEFAULT = timedelta(hours=24)
AUTH_TOKEN_REFRESH_MIN_INTERVAL_SECONDS_DEFAULT = 60
AUTH_TOKEN_HEADER = "Token"
