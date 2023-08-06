from typing import List

from internal_schemes.dao.post import PostDao
from internal_schemes.post import PostInternal
from schemes.post import Post, CreatePostRequest


class PostManager:

    def __init__(self):
        self.post_dao = PostDao()

    def get_post(self, post_id: str) -> Post | None:
        internal_post = self.post_dao.get_post(post_id=post_id)
        return self._convert_internal_post_to_external(internal_post=internal_post)

    def get_posts(self, offset: int = 0, limit: int = 30) -> List[Post]:
        posts = [
            self._convert_internal_post_to_external(internal_post=internal_post)
            for internal_post in self.post_dao.get_posts(offset=offset, limit=limit)
        ]
        return posts

    def create_post(
            self,
            post_data: CreatePostRequest,
            user_id: str
    ) -> Post:
        internal_post = self.post_dao.create_post(
            user_id=user_id,
            topic=post_data.topic,
            description=post_data.description,
            spendedTime=post_data.spendedTime,
            liftedKg=post_data.liftedKg,
            exercises=post_data.exercises,
            selfLike=post_data.selfLike,
            likes=post_data.likes,
            comments=post_data.comments,
        )

        return self._convert_internal_post_to_external(internal_post=internal_post)

    def _convert_internal_post_to_external(self, internal_post: PostInternal):
        if internal_post is None:
            return None

        return Post(
            id=internal_post.id,
            topic=internal_post.topic,
            description=internal_post.description,
            spendedTime=internal_post.spendedTime,
            liftedKg=internal_post.liftedKg,
            exercises=internal_post.exercises,
            selfLike=internal_post.selfLike,
            likes=internal_post.likes,
            comments=internal_post.comments,
            owner_id=internal_post.owner_id,
        )
