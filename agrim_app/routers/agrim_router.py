from fastapi import APIRouter, HTTPException
from ..schemas import AgrimCreate,AgrimItem
from ..services import AgrimService
from typing import List

agrim_service = AgrimService()

router = APIRouter(
    prefix="/agrim",
    tags=["info"],  ## tags=["company","fee"]
    responses= {404: {"description": "Not found"}},
)

@router.post("/info/")
async def create_info(info: AgrimCreate):
    data = agrim_service.creat_info(info)
    if not data:
        raise HTTPException(status_code = 409, detail="not created")
    response = {"status":201,
                "data":data}
    
    return response

@router.get("/info/{info_id}")
async def get_info(info_id: int ):
    data = agrim_service.get_info(info_id)
    if not data:
        raise HTTPException(status_code = 404, detail="not found")
    response = {"status":200,
                "data":data}
    return response
    