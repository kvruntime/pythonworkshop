import random
from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(random.random()))


class User(BaseEntity):
    name: str = ""


class Todo(BaseEntity):
    title: str
    content: str
    description: str | None = None
