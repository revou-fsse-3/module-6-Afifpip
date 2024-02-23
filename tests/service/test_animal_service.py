from app.controller.animal.schema.create_animal_request import Create_animal_request
from app.models.animal import Animal
from app.service.animal_service import Animal_service
from app.repositories.animal_repo import Animal_repo


def test_get_list_animal_success(test_app, mocker):
   """service get animal success"""

   # Arrange
   mock_animal_data = [
      Animal(id=6, name='chicken', species='unggas', gender='male'),
      Animal(id=5, name='chicken', species='unggas', gender='female'),
   ]
   mocker.patch.object(Animal_repo, 'get_list_animal',return_value=mock_animal_data)
   
   # Act
   with test_app.test_request_context():
      animal_service = Animal_service().get_animals()

   # Assert
   assert len(animal_service) == 2
   assert animal_service[0]['name'] == 'chicken'
   assert animal_service[1]['species'] == 'unggas'


def test_create_animal_success(test_app, mocker):
   """service get animal success"""
   # Arrange
   mock_animal_data = Animal(id=5, name='chicken', species='unggas', gender='female')
   mocker.patch.object(Animal_repo, 'create_animal', return_value=mock_animal_data)
   
   create_dto = Create_animal_request(name="chicken", species='unggas', gender='female')

   # Act
   with test_app.test_request_context():
      animal_service_create = Animal_service().create_animal(create_dto)
      
   # Assert
   assert animal_service_create['id'] == 5
   assert animal_service_create['name'] == 'chicken'
   assert animal_service_create['gender'] == 'female'