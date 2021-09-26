from graphene.test import Client
from graphene_schema import schema


def test_category():
    client = Client(schema)
    executed = client.execute('''{ category(name: "clothing") }''')
    assert executed == {
            "data": {
                "category": "name='clothing' stock=[]"
                }
            }
    
