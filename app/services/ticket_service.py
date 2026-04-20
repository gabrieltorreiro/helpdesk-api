from sqlalchemy.orm import Session
from app.models.ticket import Ticket

def create_ticket(db: Session, user_id: int, data):
    ticket = Ticket(
        title=data.title,
        description=data.description,
        priority=data.priority,
        user_id=user_id
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_tickets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ticket).offset(skip).limit(limit).all()


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket_status(db: Session, ticket_id: int, status: str):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket:
        ticket.status = status
        db.commit()
        db.refresh(ticket)

    return ticket