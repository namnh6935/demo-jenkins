from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from models import Item, SessionLocal, engine


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}


# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/items/")
# def create_item(item: Item, db: Session = Depends(get_db)):
#     db_item = Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


# @app.get("/items/{item_id}")
# def read_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = db.query(Item).filter(Item.id == item_id).first()
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item