import requests

BASE_URL = "https://fakestoreapi.com"

def test_update_product_price():
    product_id = 1

   
    response_get = requests.get(f"{BASE_URL}/products/{product_id}")
    assert response_get.status_code == 200
    product_data = response_get.json()

   
    current_price = product_data["price"]
    new_price = current_price + 15

    
    update_payload = {
        "price": new_price
    }
    response_put = requests.put(f"{BASE_URL}/products/{product_id}", json=update_payload)
    assert response_put.status_code == 200

    updated_product = response_put.json()

    assert updated_product["price"] == new_price
