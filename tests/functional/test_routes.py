from recipe_api import app
import pytest


def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes')
    assert response.status_code == 200


def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404


def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post(
        '/recipes', json={'name': 'Paella', 'ingredients': 'rice, and others','steps':'put in the water,cook', 'rate':4.9})
    assert response.status_code == 200


def test_get_particular_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get(
        '/recipes/1')
    assert response.status_code == 200


def test_update(testing_client):
    response = testing_client.put('/recipes/1',json={'name': 'Paella', 'ingredients': 'rice, and others','steps':'put in the water,cook', 'rate':4.9})
    assert response.status_code == 200

def test_delete(testing_client):
    response = testing_client.delete('/recipes/1')
    assert response.status_code == 200
