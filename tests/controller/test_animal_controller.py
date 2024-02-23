from app import db
from app.service.animal_service import Animal_service


# def test_get_customers(test_app, mocker):
#    # Arrange
#    mock_customer_data = [
#       {
#          "id": 22,
#          "name": "rafly",
#          "phone": 23
#       },
#    ]
#    mocker.patch.object(Customer_service, 'get_customers',
#                      return_value=mock_customer_data)

#    # Act
#    with test_app.test_client() as client:
#       response = client.get("/v1/customers/")

#    # Assert
#    assert response.status_code == 200
#    assert len(response.json['data']) == len(mock_customer_data)
#    assert response.json['data'] == mock_customer_data


# def test_post_customers(test_app, mocker):
#    # Arrange
#    data = {
#       "id" : 1,
#       "name": "raly",
#       "phone": 23,
#       "gender": "laki laki"
#    }
#    mocker.patch.object(Customer_service, 'create_customer', return_value=data)

#    # Act
#    with test_app.test_client() as client:
#       response = client.post("/v1/customers/", json=data)

#    # Assert
#    expected_response = {
#       "name": "raly",
#       "phone": 23,
#       "gender": "laki laki"
#    }
#    assert response.json['data']["name"] == "raly"
#    assert response.status_code == 201


def test_put_animal_update(test_app, mocker):
   # Arrange
   data = {
      "name": "chicken",
      "species": "unggas",
   }

   mocker.patch.object(Animal_service, 'update_animal', return_value=data)

   # Act
   with test_app.test_client() as client:
         response = client.put("/v1/animal/22", json=data)

   # Assert
   assert response.status_code == 200


# def test_delete_customer(test_app, mocker):
#    # Arrange
#    expected_response = {
#       "name": "raly",
#       "phone": 23,
#       "gender": "laki laki"
#    }

#    mocker.patch.object(Customer_service, 'delete_customer', return_value=expected_response)
#    with test_app.test_client() as client:
#       # Act
#       response = client.delete("/v1/customers/23")

#    # Assert
#    assert response.status_code == 200

# def test_delete_animal_not_found(test_app, mocker):
#    # Arrange
#    expected_response = "Animal not found"

#    mocker.patch.object(Animal_service, 'delete_animal', return_value=expected_response)
   
#    with test_app.test_client() as client:
#       # Act
#       response = client.delete("/v1/animal/5")

#    # Assert
#    assert response.status_code == 404
#    assert response.json['data'] == "kosong bang"