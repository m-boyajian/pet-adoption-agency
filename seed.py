"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

woofly = Pet(name='Woofly', species='dog', photo_url='https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80', age='3', notes='Woofly is house-trained, likes to play with other dogs, and loves to cuddle!', available=True)
porchetta = Pet(name='Porchetta', species='porcupine', photo_url='https://images.unsplash.com/photo-1571233086095-e6d989da9f94?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1405&q=80', age='3', notes='Porchetta is a very chill, friendly, and cuddly porcupine! She loves berries!', available=True)
snargle = Pet(name='Snargle', species='cat', photo_url='https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1287&q=80', age='6', notes='Snargle is an indoor/outdoor cat, likes to play with cat toys, and loves to take naps in the window sill!', available=True)

db.session.add_all([woofly, porchetta, snargle])
db.session.commit()