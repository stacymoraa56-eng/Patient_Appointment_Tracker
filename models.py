from sqlalchemy import Integer, Column, String, Float 
from database import Base


class Patient(Base):
    __tablename__="patients"


    id = Column(Integer, primary_key =True )
    name = Column(String, nullable =False )
    phone =Column(String, unique= True )
    doctor = Column(String, nullable= False)
    appointment_date = Column(String, nullable =False)
    status =Column(String, nullable =True)