from abc import ABC
from typing import Any, Literal, Tuple, Type, TypeVar

from loguru import logger
from pydantic import BaseModel

Model = TypeVar("Model", bound="CoBaseModel")


class CoBaseModel(ABC, BaseModel):
    # ATH_TBD: procurar como obrigar todas as subclasses a sobrescrever
    classname: Literal["CoBaseModel"] = "CoBaseModel"

    def toJson(self) -> str:
        return self.model_dump_json()

    @classmethod
    def fromJson(cls: Type[Model], json: str | bytes | bytearray) -> Model | None:
        entity = None
        try:
            entity = cls.model_validate_json(json)
        except Exception as err:
            error = err
            logger.bind(
                action="fromJson",
                clazz=cls.__name__,
            ).exception(err)
        return entity

    @classmethod
    def fromJsonEither(
        cls: Type[Model], json: str | bytes | bytearray
    ) -> Tuple[Exception | None, Model | None]:
        entity, error = None, None
        try:
            entity = cls.model_validate_json(json)
        except Exception as err:
            error = err
            logger.bind(
                action="fromJsonEither",
                clazz=cls.__name__,
            ).exception(err)
        return (error, entity)

    @classmethod
    def fromDataEither(
        cls: Type[Model],
        data: dict | Any,
    ) -> Tuple[Exception | None, Model | None]:
        entity, error = None, None
        try:
            entity = cls.model_validate(data)
        except Exception as err:
            error = err
            logger.bind(
                action="fromDataEither",
                clazz=cls.__name__,
            ).exception(err)
        return (error, entity)

    def clone(self):
        return self.model_copy(deep=True)
