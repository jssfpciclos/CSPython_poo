from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birhday = DateField()

    class Meta:
        database = db


class Pet(Model):
    owner  = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


def create_data():
    db.create_tables([Person, Pet])

    # Crear persona
    uncle_bob = Person(name='Bob', birhday=date(1960, 1, 15))
    uncle_bob.save()

    # Crear persona con método estático 'create'
    grandma = Person.create(name='Grandma', birhday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birhday=date(1950, 5, 5))

    grandma.save()
    herb.save()

    # Crear Mascotas. El propietario (FK) se le pasa como una instancia de clase
    ob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

    ob_kitty.save()
    herb_fido.save()
    herb_mittens.save()
    herb_mittens_jr.save()


def main():
    db.connect()

    # create_data()

    # Consultas básicas
    query = Person.select().where(Person.name == 'Grandma')
    result = query.get_or_none()
    print()

    personas = Person.select()
    for p in personas:
        if len(p.pets)>0:
            print(f"\nMascotas de '{p.name}':")
            for pet in p.pets:
                print(pet.name)



if __name__ == '__main__':
    main()