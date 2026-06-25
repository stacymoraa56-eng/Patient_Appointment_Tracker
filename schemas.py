from pydantic import BaseModel, StrictStr
from typing import Optional 

class PatientCreate(BaseModel):
    name: StrictStr
    phone: StrictStr
    doctor:StrictStr
    appointment_date: StrictStr
    status:StrictStr = "scheduled"


class PatientUpdate(BaseModel):
    name:Optional[StrictStr]= None 
    phone:Optional[StrictStr]=None
    doctor:Optional[StrictStr]= None 
    appointment_date:Optional[StrictStr]=None
    status:Optional[StrictStr]=None


class PatientResponse(BaseModel):
    id: int 
    name: str 
    phone:str
    doctor:str 
    appointment_date:str 
    status: str 

    class Config: 
        from_attributes =True 