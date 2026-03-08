import requests
import pytest

# Mohd Hozaifa - API Automation Project
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_validation():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    assert "username" in response.json()
    print("\n[PASS] User validation successful")

def test_create_post_automation():
    payload = {"title": "Hozaifa API Test", "body": "Python Automation", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()['title'] == "Hozaifa API Test"
    print("\n[PASS] Post creation successful")

def test_delete_endpoint():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code in [200, 202, 204]
    print("\n[PASS] Delete request successful")
