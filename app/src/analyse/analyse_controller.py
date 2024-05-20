from fastapi import APIRouter, Body, HTTPException, UploadFile, File
from app.src.analyse.analyse_service import analyseService

from app.src.analyse.dto.analyse import AnalyseDto


routes = APIRouter()
routeBase = f"/analyse"


@routes.post(f"{routeBase}")
async def register_createNewUser(
    dto: AnalyseDto = Body(...),
):

    return analyseService.picture_analyse(dto.base64Obj)
