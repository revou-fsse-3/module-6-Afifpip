from flask import Blueprint, jsonify
from app.utils.database import db
from app.models.animal import Animal


animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=["POST"])
def create_animal():
  animal = Animal()
  animal.name = "chicken"
  animal.species = "unggas"
  animal.gender = "male"
  db.session.add(animal)
  db.session.commit()
  return