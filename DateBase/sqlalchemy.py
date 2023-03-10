from sqlalchemy import create_engine, MetaData, ForeignKey, Table, Column, BigInteger,\
    VARCHAR, Boolean, Integer, Float, TIMESTAMP, CheckConstraint

meta = MetaData()

users = Table('users', meta,
              Column('user_id', BigInteger, primary_key=True),
              Column('name', VARCHAR(50), nullable=False),
              Column('second_name', VARCHAR(50), nullable=False),
              Column('phone', VARCHAR(12), nullable=False),
              Column('email', VARCHAR(100), nullable=False),
              Column('is_admin', Boolean, nullable=False))

colours = Table('colours', meta,
                Column('colour_id', BigInteger, primary_key=True),
                Column('colour_name', VARCHAR(30), nullable=False))

diler = Table('diler', meta,
              Column('diler_id', BigInteger, primary_key=True),
              Column('diler_name', VARCHAR(20), nullable=False),
              Column('is_related', Boolean, nullable=False))

basket = Table('basket', meta,
               Column('stuff_id', BigInteger, ForeignKey('furniture.id')),
               Column('user_id', BigInteger, ForeignKey('users.user_id')),
               Column('quantity', Integer, CheckConstraint('quantity > 0'), nullable=False))

furniture = Table('furniture', meta,
                  Column('id', BigInteger, primary_key=True),
                  Column('height', Float(20), CheckConstraint('5 < height < 0.1 '), nullable=False),
                  Column('depth', Float(20), CheckConstraint('5 < depth < 0.1 '), nullable=False),
                  Column('length', Float(20), CheckConstraint('10 < length < 0.3 '), nullable=False),
                  Column('ship_name', BigInteger, ForeignKey('shipment.ship_id')),
                  Column('cost', Integer, CheckConstraint('cost > 0'), nullable=False),
                  Column('colour_id', BigInteger, ForeignKey('colours.colour_id')))

wardrobe = Table('wardrobe', meta,
                 Column('id', BigInteger, ForeignKey('furniture.id')),
                 Column('num_shelfs', Integer, CheckConstraint('num_shelfs > 0'), nullable=False))

sofa = Table('sofa', meta,
             Column('id', BigInteger, ForeignKey('furniture.id')),
             Column('num_seats', Integer, CheckConstraint('num_seats > 0'), nullable=False),
             Column('corner', Boolean, nullable=False),
             Column('expand', Boolean))

table = Table('table', meta,
              Column('id', BigInteger, ForeignKey('furniture.id')),
              Column('expand', Boolean))

orders = Table('orders', meta,
               Column('user_id', BigInteger, ForeignKey('users.user_id')),
               Column('order_date', TIMESTAMP, nullable=False),
               Column('order_cost', Float(15), CheckConstraint('order_cost > 0'), nullable=False))

shipment = Table('shipment', meta,
                 Column('ship_id', BigInteger, primary_key=True),
                 Column('ship_date', TIMESTAMP, nullable=False),
                 Column('weight', Float(30), CheckConstraint('weight > 0.5'), nullable=False),
                 Column('diler_id', Integer, ForeignKey('diler.diler_id')))
