from appfoundation.auth.kernel.autoken.model.autoken import AuToken
from appfoundation.core.abstraction.cocontextexecution.cocontextexecution import (
    CoContextExecution,
)
from appfoundation.core.cohesivemechanism.coconstant.coconstant import (
    TRANSACTION_DEFAULT,
)
from appfoundation.core.cohesivemechanism.coutils import coutils
from appfoundation.core.kernel.coactivity.cotask import CoTask


class CleanupAuTokenTaskActivity(CoTask):

    def __init__(self, prCoContextExecution: CoContextExecution) -> None:
        super().__init__(prCoContextExecution)

    def _semantic(self) -> bool:
        lNow = coutils.datetimeUtcNow()
        AuToken.objects.filter(expiry__isnull=False, expiry__lte=lNow).delete()

        return not self.coMessageList.withError()

    def do(self) -> bool:
        return self._action(TRANSACTION_DEFAULT)
