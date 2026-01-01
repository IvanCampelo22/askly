from django.contrib.auth.models import User
from django.db import models

from appfoundation.auth.kernel.autoken.model.autokenmanager import AuTokenManager
from appfoundation.core.cohesivemechanism.coconstant.coconstant import (
    AUTH_TOKEN_KEY_LENGTH,
)


class AuToken(models.Model):

    digest = models.CharField(max_length=128, null=False)
    key = models.CharField(max_length=AUTH_TOKEN_KEY_LENGTH, null=False)

    user = models.ForeignKey(
        User, null=False, related_name="%(class)s_user", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(null=True, blank=True)

    objects = AuTokenManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["digest"], name="autoken_digest_uqa"),
        ]

        indexes = [
            models.Index(fields=["key"], name="autoken_key_idx"),
        ]
