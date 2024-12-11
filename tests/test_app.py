from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API para Reservas de Hotel en ejecución ..."}

def test_crear_cliente():
    cliente = {"nombre": "John Doe", "email": "john@example.com", "telefono": "1234567890"}
    response = client.post("/clientes", json=cliente)
    assert response.status_code == 200
    assert "idCliente" in response.json()
