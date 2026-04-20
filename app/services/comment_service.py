from sqlalchemy.orm import Session
from app.models.comment import Comment

def create_comment(db: Session, content: str, ticket_id: int, user_id: int):
    comment = Comment(
        content=content,
        ticket_id=ticket_id,
        user_id=user_id
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments_by_ticket(db: Session, ticket_id: int):
    return db.query(Comment).filter(Comment.ticket_id == ticket_id).all()