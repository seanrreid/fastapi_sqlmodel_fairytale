import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Import our tools
# This is the database connection file
from sqlmodel import Session, select, func, literal_column
from db import get_session

# These are our models
from models.pigs import Pigs
from models.wolves import Wolves
from models.houses import Houses
from models.attacks import Attacks

app = FastAPI()

# Setup our origins...
# ...for now it's just our local environments
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Add the CORS middleware...
# ...this will pass the proper CORS headers
# https://fastapi.tiangolo.com/tutorial/middleware/
# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Root Route"}


@app.get('/pigs')
async def get_pigs(session: Session = Depends(get_session)):
    statement = select(Pigs)
    results = session.exec(statement).all()
    return results


@app.get('/wolves')
async def get_wolves(session: Session = Depends(get_session)):
    statement = select(Wolves)
    results = session.exec(statement).all()
    return results


@app.get('/houses')
async def get_houses(session: Session = Depends(get_session)):
    statement = select(
        Houses.id,
        Houses.material,
        Houses.successfully_attacked,
        func.array_agg(Pigs.name).label('pigs')
    ).join(
        Pigs, Pigs.id == Houses.pig_id
    ).group_by(
        Houses
    )
    print(statement)
    results = session.exec(statement).mappings().all()
    return results


@app.get('/attacks')
async def get_attacks(session: Session = Depends(get_session)):
    statement = select(Attacks)
    results = session.exec(statement).all()
    return results


@app.post('/houses/add')
async def add_house(pig_id: int, material: str, successfully_attacked: bool, session: Session = Depends(get_session)):
    house = Houses(
        pig_id=pig_id, material=material, successfully_attacked=successfully_attacked)
    session.add(house)
    session.commit()
    return {"message": "House added"}


@app.post('/wolves/add')
async def add_wolf(name: str, session: Session = Depends(get_session)):
    wolf = Wolves(name=name)
    session.add(wolf)
    session.commit()
    return {"Wolf Added": wolf.name}


@app.post('/pigs/add')
async def add_pig(name: str, session: Session = Depends(get_session)):
    piglet = Pigs(name=name)
    session.add(piglet)
    session.commit()
    return {"Piglet Added": piglet.name}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
