from app.models.employee import Employee
from app.utils.database import db

class Employee_repo():
   def get_list_employee(self):
      employees = Employee.query.all()
      return employees
   
   def create_employee(self, employee):
      db.session.add(employee)
      db.session.commit()
      return employee

   def update_employee(self, id, animal):
      employee_obj = Employee.query.get(id)
      employee_obj.name = animal.name
      employee_obj.age = animal.age
      employee_obj.gender = animal.gender

      db.session.commit()
      return employee_obj
   
   def delete_employee(self, id):
      employee_obj = Employee.query.get(id)

      db.session.delete(employee_obj)
      db.session.commit()
      return employee_obj

   def search_employee(self, name):
      employees = Employee.query.filter(Employee.name.like(f"%{name}%")).all()
      return employees