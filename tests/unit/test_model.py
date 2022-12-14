from recipe_api.models import Recipe
import pytest


def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    recipe = Recipe('Paella', 'ingredients','steps', 4.9,"false")
    assert recipe.name == 'Paella'
    assert recipe.ingredients == 'ingredients'
    assert recipe.steps == 'steps'
    assert recipe.rate == 4.9
    assert recipe.favorite == "false"
