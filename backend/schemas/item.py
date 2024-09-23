from pydantic import BaseModel, RootModel, Field
from typing import List

    

class Exercise(BaseModel):
    id: int
    name: str
    sets: List[set]

class Day(BaseModel):
    id: int
    name: str
    exercises: List[Exercise]
    
class Split(BaseModel):
    id: int
    name: str


class CalendarData(BaseModel):
    month: int
    day: int
    year: int