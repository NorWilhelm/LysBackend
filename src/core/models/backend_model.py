from typing import List

from pydantic import BaseModel, Field

class BackendData(BaseModel):
    version: str
    read_me: str = Field(alias='readMe')