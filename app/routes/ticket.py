from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import SessionLocal
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services import ticket_service
from app.core.auth import get_current_user  # você já deve ter isso

router = APIRouter(prefix="/tickets", tags=["Tickets"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TicketResponse)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return ticket_service.create_ticket(db, current_user.id, ticket)


@router.get("/", response_model=List[TicketResponse])
def list_tickets(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return ticket_service.get_tickets(db, skip, limit)


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = ticket_service.get_ticket_by_id(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@router.patch("/{ticket_id}")
def update_status(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    ticket = ticket_service.update_ticket_status(db, ticket_id, status)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {"message": "Ticket updated", "status": ticket.status}