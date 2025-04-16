from ninja import Schema
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class BaseSchema(Schema):
    model_config = ConfigDict(
        **Schema.model_config,
        alias_generator=to_camel,
        populate_by_name=True,
    )
