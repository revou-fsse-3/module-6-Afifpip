from flask import Blueprint, jsonify
from app.utils.database import db
from app.models.employee import Employee


employee_blueprint = Blueprint('employee_endpoint', __name__)

@employee_blueprint.route("/", methods=["POST"])
def create_employee():
  employee = Employee()
  employee.name = "Bobon"
  employee.age = 29
  employee.gender = "male"
  db.session.add(employee)
  db.session.commit()
  return