from typing import Any, List, Literal

from pydantic import Field, RootModel, computed_field
from appfoundation.core.abstraction.comodel.cobasemodel import CoBaseModel
from appfoundation.core.cohesivemechanism.comessage.comessage import CoMessage
from appfoundation.core.cohesivemechanism.comessagelist.comessagelist import (
    CoMessageList,
)


class CoResultDTO(CoBaseModel):
    classname: Literal["CoResultDTO"] = "CoResultDTO"

    data: Any | None
    coMessageList_: CoMessageList = Field(exclude=True, default=CoMessageList())

    @computed_field
    @property
    def withError(self) -> bool:
        return self.coMessageList_.withError()

    @computed_field
    @property
    def comessageList(self) -> RootModel[List[CoMessage]]:
        return RootModel(self.coMessageList_.getList())

    @classmethod
    def get(
        cls,
        prCoMessageList: CoMessageList = CoMessageList(),
        data: Any | None = None,
    ) -> "CoResultDTO":
        lCoResultDTO = cls(coMessageList_=prCoMessageList, data=data)
        return lCoResultDTO
