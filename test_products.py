import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_all_products_status_code():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200

def test_get_all_products_response_structure():
    response = requests.get(f"{BASE_URL}/products")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    first_product = data[0]
    assert "id" in first_product
    assert "title" in first_product
    assert "price" in first_product
    assert "category" in first_product

def test_get_single_product():
    product_id = 1
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert "title" in data
    assert "price" in data
