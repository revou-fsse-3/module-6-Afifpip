from app.controller.employee.schema.create_employee_request import Create_employee_request
from app.models.employee import Employee
from app.service.employee_service import Employee_service
from app.repositories.employee_repo import Employee_repo


def test_get_list_employee_success(test_app, mocker):
   """service get employee success"""

   # Arrange
   mock_employee_data = [
      Employee(id=1, name='Bobon', age=29, gender='male'),
      Employee(id=2, name='Dinda', age=24, gender='female'),
   ]
   mocker.patch.object(Employee_repo, 'get_list_employee',return_value=mock_employee_data)
   
   # Act
   with test_app.test_request_context():
      employee_service = Employee_service().get_employees()

   # Assert
   assert len(employee_service) == 2
   assert employee_service[0]['name'] == 'Bobon'
   assert employee_service[1]['gender'] == 'female'


def test_create_employee_success(test_app, mocker):
   """service get employee success"""
   # Arrange
   mock_employee_data = Employee(id=1, name='Bobon', age=29, gender='male')
   mocker.patch.object(Employee_repo, 'create_employee', return_value=mock_employee_data)
   
   create_dto = Create_employee_request(name="Bobon", age=29, gender='male')

   # Act
   with test_app.test_request_context():
      employee_service_create = Employee_service().create_employee(create_dto)
      
   # Assert
   assert employee_service_create['id'] == 1
   assert employee_service_create['name'] == 'Bobon'
   assert employee_service_create['gender'] == 'male'