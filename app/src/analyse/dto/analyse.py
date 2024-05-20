from pydantic import BaseModel


class AnalyseDto(BaseModel):
    base64Obj: str
