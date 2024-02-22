from app.repositories.employee_repo import Employee_repo
from app.models.employee import Employee

class Employee_service:
   def __init__(self):
      self.employee_repo = Employee_repo()

   def get_employees(self):
      employees = self.employee_repo.get_list_employee()
      return [employee.as_dict() for employee in employees]

   def search_employee(self, name):
      employees = self.employee_repo.search_employee(name)
      return [employee.as_dict() for employee in employees]
   
   def create_employee(self, employee_data_dto):
      employee = Employee()
      
      employee.name = employee_data_dto.name
      employee.age = employee_data_dto.age
      employee.gender = employee_data_dto.gender
      
      created_employee = self.employee_repo.create_employee(employee)
      return created_employee.as_dict()
   
   def update_employee(self, id, employee_data_dto):
      updated_employee = self.employee_repo.update_employee(id, employee_data_dto)
      return updated_employee.as_dict()
   
   def delete_employee(self, id):
      employee = Employee.query.get(id)
      if not employee:
            return "employee not found"

      deleted_employee = self.employee_repo.delete_employee(id)
      return deleted_employee.as_dict()