from pydantic import BaseModel

class CommentReviewPostRequest(BaseModel):
    show_id: int
    comment: str
    rating: float