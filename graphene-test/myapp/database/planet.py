from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .people import ModelPeople


class ModelPlanet(Base):
    __tablename__ = "planet"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    rotation_period = Column("rotation_period", String)
    orbital_period = Column("orbital_period", String)
    diameter = Column("diameter", String)
    climate = Column("climate", String)
    gravity = Column("gravity", String)
    terrain = Column("terrain", String)
    surface_water = Column("surface_water", String)
    population = Column("population", String)
    created = Column("created", String)
    edited = Column("edited", String)
    url = Column("url", String)

    peopleList = relationship(ModelPeople, backref="planet")
