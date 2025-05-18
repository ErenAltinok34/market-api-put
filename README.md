
## 🚀 What This Test Does

The test checks whether a product can be successfully updated. It:

- Sends a `PUT` request to update a product (e.g., product with ID 1),
- Increases the product price by $15,
- Asserts that the response is successful (status code 200),
- Verifies the updated price in the response data.

## 🧪 Running the Test

Make sure you have `pytest` and `requests` installed:

```bash
pip install -r requirements.txt
