from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.comment import CommentCreate, CommentResponse
from app.services.comment_service import create_comment, get_comments_by_ticket
from app.database.connection import SessionLocal

from app.core.auth import get_current_user  

router = APIRouter(prefix="/tickets", tags=["Comments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{ticket_id}/comments", response_model=CommentResponse)
def add_comment(
    ticket_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_comment(
        db=db,
        content=comment.content,
        ticket_id=ticket_id,
        user_id=current_user.id
    )


@router.get("/{ticket_id}/comments", response_model=list[CommentResponse])
def list_comments(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_comments_by_ticket(db, ticket_id)