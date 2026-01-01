from datetime import timedelta

from django.db import models

from appfoundation.core.cohesivemechanism.coconstant.coconstant import AUTH_TOKEN_KEY_LENGTH
from appfoundation.core.cohesivemechanism.coutils import cocrypto, coutils


class AuTokenManager(models.Manager):

    def createToken(self, prUser, prExpiryDelta: timedelta | None = None):
        lToken = cocrypto.createTokenString()
        lDigest = cocrypto.hashToken(lToken)
        if prExpiryDelta is not None:
            lExpiry = coutils.datetimeUtcNow() + prExpiryDelta

        auToken = self.create(
            user=prUser,
            digest=lDigest,
            key=lToken[:AUTH_TOKEN_KEY_LENGTH],
            expiry=lExpiry,
        )
        return (auToken, lToken)
