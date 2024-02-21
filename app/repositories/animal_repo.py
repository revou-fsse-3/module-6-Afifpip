from app.models.animal import Animal
from app.utils.database import db

class Animal_repo():
   def get_list_animal(self):
      animals = Animal.query.all()
      return animals
   
   def create_animal(self, animal):
      db.session.add(animal)
      db.session.commit()
      return animal

   def update_animal(self, id, animal):
      animal_obj = Animal.query.get(id)
      animal_obj.name = animal.name
      animal_obj.species = animal.species
      animal_obj.gender = animal.gender

      db.session.commit()
      return animal_obj
   
   def delete_animal(self, id):
      animal_obj = Animal.query.get(id)

      db.session.delete(animal_obj)
      db.session.commit()
      return animal_obj

   def search_animal(self, name):
      animals = Animal.query.filter(Animal.name.like(f"%{name}%")).all()
      return animals