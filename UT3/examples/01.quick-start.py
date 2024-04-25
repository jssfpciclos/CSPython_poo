from datetime import datetime
from datetime import date
from peewee import *

db = SqliteDatabase('01_mascotas.db')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    name = CharField()
    animal_type = CharField()
    owner = ForeignKeyField(Person, backref='pets')

    class Meta:
        database = db


def create_tables():
    db.create_tables([Person, Pet])

def init_data():
    peter = Person(name='Peter', birthday=date(1960, 1, 15))
    peter.save()

    pet = Pet(name='lulu', animal_type='cat', owner=peter)
    pet.save()

    mg = Person(name='Margaret', birthday=date(1995, 1, 1))
    mg.save()

    pet = Pet(name='kira', animal_type='dog', owner=mg)
    pet.save()
    pet = Pet(name='markus', animal_type='dog', owner=mg)
    pet.save()


def load_data():

    "Select * from person where birthday < date.today()"
    lista_personas = Person.select()

    for persona in lista_personas:
        print(f"-----{persona.name} -----")
        if len(persona.pets)>0:
            # Esta personal tiene mascotas
            for mascota in persona.pets:
                print(f"La mascota {mascota.name} pertenece a {mascota.owner.name}")
                print("")




if __name__ == '__main__':
    # peter = Person(name='Peter', birthday=datetime.date(2005, 1, 1))
    # pet = Pet(name='lulu', animal_type='cat', owner=peter)
    # create_tables()
    init_data()
