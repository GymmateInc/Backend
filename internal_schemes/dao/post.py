from typing import List

from internal_schemes.dao.base import BaseDao
from internal_schemes.post import PostInternal


class PostDao(BaseDao):
    id_prefix = "post"

    def get_post(self, post_id: str) -> PostInternal | None:
        """Get post from db by post_id"""
        return self.session.query(PostInternal).filter(PostInternal.id == post_id).first()

    def get_posts(self, offset: int = 0, limit: int = 30) -> List[PostInternal]:
        """Get posts by skipping offset item and with limit"""
        return self.session.query(PostInternal).offset(offset).limit(limit).all()

    def create_post(
            self,
            user_id: str,
            topic: str,
            description: str,
            spendedTime: str | None,
            liftedKg: float | None,
            exercises: int | None,
            selfLike: bool = False,
            likes: int = 0,
            comments: int = 0,
    ) -> PostInternal:
        """Create new post"""
        post = PostInternal(
            id=self.generate_id(prefix=self.id_prefix),
            topic=topic,
            description=description,
            spendedTime=spendedTime,
            liftedKg=liftedKg,
            exercises=exercises,
            selfLike=selfLike,
            likes=likes,
            comments=comments,
            owner_id=user_id,
        )
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post
