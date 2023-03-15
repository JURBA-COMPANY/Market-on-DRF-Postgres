from main import *
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/Mivla")
session = Session(bind=engine)
users = session.query(Users.user_id, Users.name, Users.second_name, Users.phone, Users.email).all()
colours = session.query(Colours.colour_id, Colours.colour_name).all()
diler = session.query(Diler.diler_id, Diler.diler_name, Diler.is_related).all()
furniture = session.query(Furniture.id, Furniture.height, Furniture.depth, Furniture.length, Furniture.ship_name,
                          Furniture.cost).all()
shipment = session.query(Shipment.ship_id, Shipment.ship_date, Shipment.weight, Shipment.diler_id).all()
sofa = session.query(Sofa.id, Sofa.num_seats, Sofa.corner, Sofa.expand).all()
wardrobe = session.query(Wardrobe.id, Wardrobe.num_shelfs).all()
stol = session.query(Stol.id, Stol.expand).all()
basket = session.query(Basket.stuff_id, Basket.order_date, Basket.quantity).all()
