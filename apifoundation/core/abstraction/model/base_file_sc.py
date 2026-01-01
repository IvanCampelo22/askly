from typing import Any, Generic, List, Literal, TypeVar

from pydantic import Field

from appfoundation.core.abstraction.comodel.cobasemodel import CoBaseModel

T = TypeVar("T", bound=CoBaseModel)


class CoBaseFileDTO(CoBaseModel, Generic[T]):
    classname: Literal["CoBaseFileDTO"] = "CoBaseFileDTO"
    files: List[Any] = Field(list(), exclude=True)

    data: T | None = None
