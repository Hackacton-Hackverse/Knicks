from fastapi import FastAPI, HTTPException, File, UploadFile, Depends
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr 
from datetime import datetime
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import sessionmaker, session
import sqlite3
import uvicorn

app = FastAPI(title="Get a job API", version="v1")


#Database setup
DATABASE_URL = "sqlite:///./test.sql"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, blind=engine)
Base = sqlalchemy.orm.declarative_base()


#Setting the user database model 
class User(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True),
    name = Column(String),
    surname = Column(String),
    username = Column(String),
    password = Column(String),
    email = Column(EmailStr),
    speciality = Column(String), 
    status = Column(bool)
Base.metadata.create_all(blind=engine)



#Setting the offer database model 
class Offer(Base):
    __tablename__ = 'offers'
    offer_id = Column(Integer, primary_key=True), 
    name = Column(String),
    description = Column(String),
    start_date = Column(datetime.datetime),
    end_date = Column(datetime.datetime),
    category = Column(String),
    author = Column(String),
    place = Column(String) 
Base.metadata.create_all(blind=engine)


#Setting the apllication database model 
class Application(Base):
    __tablename__ = 'applications'
    app_id = Column(Integer, primary_key=True),
    user_id = Column(String, ('user.id')),
    offer_id = Column(Integer, 'offer.offer_id'),
    letter_id = (UploadFile),
    cv_id = Column(UploadFile)
Base.metadata.create_all(blind=engine)



#Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#pydantic model for request data
class user(BaseModel):
    id : str
    name : str
    surname : str
    username : str
    password : str
    email : EmailStr
    speciality : str
    status : bool

class offer(BaseModel):
    offer_id : int
    name : str
    description : str
    start_date : datetime
    end_date : datetime
    category : str
    author : str
    place : str

class application(BaseModel):
    appl_id : int
    user_id : str
    offer_id : int
    letter_id : int
    cv_id : int


#pydantic model for request data

class user_res(BaseModel):
    username:str

class offer_res(BaseModel):
    offer_id : int

class application_res(BaseModel):
    app_id:int
   

#posting users`informations
@app.post("/users/", response_model=user_res)
async def create_user(user: user, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

    
#posting offers (creating an offer)
@app.post("/offers/", response_model=offer_res, status_code=status.HTTP_201_CREATED)
async def create_offer(offer: offer, db: Session = Depends(get_db)):
    db_offer = Offer(**offer.model_dump())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

#updating an offer
@app.put("/offer/{offer_offer_id}", response_model=offer_res)
async def update_offer(offer_offer_id: int, offer:offer):
    return {'offer_id' : offer_offer_id, **offer.dict()}

#deleting an offer
@app.delete("/offer/{offer_offer_id}", response_model=offer_res)
async def delete_offer(offer_offer_id: int):
    with Session(engine) as session:
        offer = session.get(Offer, offer_offer_id)
        if not offer:
            raise HTTPException(status_code=404, detail='Offer not found')
        session.delete(offer)
        session.commit()
        return {'ok': True}
    
#getting offers (consulting an offer)
@app.get("/offer/{offer_offer_id}", response_model=offer_res)
async def read_offer(offer_offer_id:int, db: Session = Depends(get_db)):
    db_offer = db.query(Offer).filter(Offer.offer_id == offer_offer_id).first()
    if db_offer is None :
        raise HTTPException (status_code=404, detail='Offer not found')
    return db_offer

#posting applications (applying for an offer)
@app.post("/applications/", response_model=application_res)
async def create_appl(appl: application, db: Session = Depends(get_db)):
    db_appl = Application(**appl.model_dump())
    db.add(db_appl)
    db.commit()
    db.refresh(db_appl)
    return db_appl



#Launching the server
if __name__=="__api__":
    uvicorn.run (app:api, host="127.0.0.1", port=8000, reload=True)


'''
app=FastAPI()
@app.get("/")
async def root():
    return{"greeting":"Hello World"}
    '''