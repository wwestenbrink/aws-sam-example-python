import os

import requests

API_BASE_URL = os.environ.get('API_BASE_URL') or 'http://localhost:3000'


def test_valid_n() -> None:
    response = requests.get(f'{API_BASE_URL}/fibonacci?n=1')
    assert response.text == '1'
    assert response.status_code == 200


def test_invalid_n() -> None:
    response = requests.get(f'{API_BASE_URL}/fibonacci?n=not_a_number')
    assert response.text.startswith("Bad request:")
    assert response.status_code == 400
