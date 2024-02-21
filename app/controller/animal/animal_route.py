from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.animal import Animal
from app.utils.api_response import api_response
from app.service.animal_service import Animal_service
from app.controller.animal.schema.update_animal_request import Update_animal_request
from app.controller.animal.schema.create_animal_request import Create_animal_request
from pydantic import ValidationError

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=["GET"])
def get_list_animal():
    try:
        animal_service = Animal_service()

        animals = animal_service.get_animals()

        return api_response(
            status_code=200,
            message="success",
            data=animals
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@animal_blueprint.route("/search", methods=["GET"])
def search_animal():
    try:
        request_data = request.args
        animal_service = Animal_service()

        animals = animal_service.search_animal(request_data["name"])

        return api_response(
            status_code=200,
            message="successfully",
            data=animals
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return "animal not found", 404

        return animal.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=animal
        )

@animal_blueprint.route("/", methods=["POST"])
def create_animal():
    try:

        data = request.json
        update_animal_request = Create_animal_request(**data)

        animal_service = Animal_service()

        animals = animal_service.create_animal(update_animal_request)

        return api_response(
            status_code=201,
            message="Data Successfully Created",
            data=animals
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

@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    try:

        data = request.json
        update_animal_request = Update_animal_request(**data)

        animal_service = Animal_service()

        animals = animal_service.update_animal(
            animal_id, update_animal_request)

        return api_response(
            status_code=200,
            message="Updated animal Success",
            data=animals
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

@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    try:
        animal_service = Animal_service()

        animal = animal_service.delete_animal(animal_id)
        
        return api_response(
            status_code=200,
            message="Deleted animal",
            data=animal
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )