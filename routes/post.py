from typing import List

from fastapi import Query, Depends, APIRouter

from managers.post import PostManager
from schemes.post import Post, CreatePostRequest
from utils.utils import raise_404_not_found_error, provide_mock_user_id


router = APIRouter()
post_manager = PostManager()


@router.get(
    "/post",
    summary="Get post by post id"
)
def get_post(
        post_id: str
) -> Post:
    result = post_manager.get_post(post_id=post_id)

    if result is None:
        raise_404_not_found_error()

    return result


@router.get(
    "/posts",
    summary="Get post by post id"
)
def get_posts(
        offset: int = Query(default=0, description="Offset from which position give posts"),
        limit: int = Query(default=30, description="Limit to return post"),
) -> List[Post]:
    return post_manager.get_posts(offset=offset, limit=limit)


@router.post(
    "/post",
    summary="Create new post"
)
def create_post(
        post_data: CreatePostRequest,
        user_id: str = Depends(provide_mock_user_id),
) -> Post:
    result = post_manager.create_post(post_data=post_data, user_id=user_id)

    if result is None:
        raise_404_not_found_error()

    return result
