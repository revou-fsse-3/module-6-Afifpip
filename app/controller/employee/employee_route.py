from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employee import Employee
from app.utils.api_response import api_response
from app.service.employee_service import Employee_service
from app.controller.employee.schema.update_employee_request import Update_employee_request
from app.controller.employee.schema.create_employee_request import Create_employee_request
from pydantic import ValidationError

employee_blueprint = Blueprint('employee_endpoint', __name__)

@employee_blueprint.route("/", methods=["GET"])
def get_list_employee():
    try:
        employee_service = Employee_service()

        employees = employee_service.get_employees()

        return api_response(
            status_code=200,
            message="success",
            data=employees
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@employee_blueprint.route("/search", methods=["GET"])
def search_employee():
    try:
        request_data = request.args
        employee_service = Employee_service()

        employees = employee_service.search_employee(request_data["name"])

        return api_response(
            status_code=200,
            message="successfully",
            data=employees
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return "employee not found", 404

        return employee.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=employee
        )

@employee_blueprint.route("/", methods=["POST"])
def create_employee():
    try:

        data = request.json
        update_employee_request = Create_employee_request(**data)

        employee_service = Employee_service()

        employees = employee_service.create_employee(update_employee_request)

        return api_response(
            status_code=201,
            message="Data Successfully Created",
            data=employees
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:

        data = request.json
        update_employee_request = Update_employee_request(**data)

        employee_service = Employee_service()

        employees = employee_service.update_employee(
            employee_id, update_employee_request)

        return api_response(
            status_code=200,
            message="Updated employee Success",
            data=employees
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        employee_service = Employee_service()

        employee = employee_service.delete_employee(employee_id)
        
        return api_response(
            status_code=200,
            message="Deleted employee",
            data=employee
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )