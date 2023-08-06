from pydantic import BaseModel, Field


class CreatePostRequest(BaseModel):
    topic: str = Field(description="Topic of the Post")
    description: str = Field(description="Description of the Post")
    spendedTime: str | None = Field(default=None, description="Spended time on training", nullable=True)
    liftedKg: float | None = Field(default=None, description="How much kg lifted in sum on training", nullable=True)
    exercises: int | None = Field(efault=None, description="How much different exercises make on training",
                                  nullable=True)
    selfLike: bool = Field(default=False, description="Is current user like post")
    likes: int = Field(default=0, description="Count of likes on post")
    comments: int = Field(default=0, description="Count of comments on post")


class Post(BaseModel):
    id: str = Field(description="ID for the item")

    topic: str = Field(description="Topic of the Post")
    description: str = Field(description="Description of the Post")
    spendedTime: str | None = Field(default=None, description="Spended time on training", nullable=True)
    liftedKg: float | None = Field(default=None, description="How much kg lifted in sum on training", nullable=True)
    exercises: int | None = Field(efault=None, description="How much different exercises make on training",
                                  nullable=True)
    selfLike: bool = Field(default=False, description="Is current user like post")
    likes: int = Field(default=0, description="Count of likes on post")
    comments: int = Field(default=0, description="Count of comments on post")

    owner_id: str = Field(description="Owner id of the post")
