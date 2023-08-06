from fastapi import HTTPException, status


def raise_404_not_found_error(detail_string: str = "Not Found") -> None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail_string
    )


def raise_400_parameters_error(detail_string: str) -> None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail_string,
    )


def provide_mock_user_id():
    return "mock_user_id_"
