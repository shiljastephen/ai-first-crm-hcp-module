from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.interaction import Interaction
from app.schemas.interaction import (
    InteractionCreate,
    InteractionUpdate,
    InteractionResponse,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)

@router.post("/", response_model=InteractionResponse)
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):
    db_interaction = Interaction(**interaction.model_dump())

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction

@router.get("/", response_model=list[InteractionResponse])
def get_interactions(
    db: Session = Depends(get_db)
):
    return db.query(Interaction).all()

@router.get("/{interaction_id}", response_model=InteractionResponse)
def get_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    return interaction

@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_interaction(
    interaction_id: int,
    updated_data: InteractionUpdate,
    db: Session = Depends(get_db)
):

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    update_fields = updated_data.model_dump(exclude_unset=True)

    for key, value in update_fields.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction

@router.delete("/{interaction_id}")
def delete_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    db.delete(interaction)
    db.commit()

    return {
        "message": "Interaction deleted successfully"
    }