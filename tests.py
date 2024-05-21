import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
snacks = []

def test_create_snack():
    new_snack_data = {
        "name": "Nova refeição",
        "description": "Descrição da nova refeição",
        "dateTime": "17/05/2024-13:30",
        "check": True
        }
    
    response = requests.post(f"{BASE_URL}/snack", json=new_snack_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "id" in response_json
    snacks.append(response_json['id'])

def test_get_snacks():
    response = requests.get(f"{BASE_URL}/snack")
    assert response.status_code == 200
    response_json = response.json()
    assert "snacks" in response_json
    assert "total_snacks" in response_json

def test_get_snack():
    snack_id = snacks[0]
    response = requests.get(f"{BASE_URL}/snack/{snack_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert snack_id == response_json['id']

def test_update_snack():
    if snacks:
        snack_id = snacks[0]
        payload = {
            "name": "Refeição atualizada",
            "description": "Descrição atualizada",
            "dateTime": "17/05/2024-19:30",
            "check": False
        }
        response = requests.put(f"{BASE_URL}/snack/{snack_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()

        response = requests.get(f"{BASE_URL}/snack/{snack_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['name'] == payload['name']
        assert response_json['description'] == payload['description']
        assert response_json['dateTime'] == payload['dateTime']
        assert response_json['check'] == payload['check']

def test_delete_snack():
    snack_id = snacks[0]
    response = requests.delete(f"{BASE_URL}/snack/{snack_id}")
    assert response.status_code == 200
    
    response = requests.get(f"{BASE_URL}/snack/{snack_id}")
    assert response.status_code == 404