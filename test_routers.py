from fastapi.testclient import TestClient
from main import app
from routers import get_store
from models import Item, Store, Category

client = TestClient(app)


def test_hard_coded():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == 'some hard coded data'


def test_add_to_stock():
    item = Item("dress", 50.0)
    response = client.post("/store/clothing", json=item.dict())
    assert response.status_code == 200
    assert response.json() == item.dict()


items = [Item("dress", 50.0), Item("pants", 50.0)]


async def mock_store():
    return Store({"clothing": Category("clothing", items)})


app.dependency_overrides[get_store] = mock_store


def test_items_in_stock():
    response = client.get("/store/clothing/dress")
    assert response.status_code == 200
    assert response.json() == [items[0].dict()]
