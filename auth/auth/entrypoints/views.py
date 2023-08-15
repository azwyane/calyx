from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/auth/")
def authentication():
    return "authenticated"