from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(description="Name of the user")
    email: str | None = Field(description="Email of the user")
