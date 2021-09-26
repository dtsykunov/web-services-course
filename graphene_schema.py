from graphene import ObjectType, String, Schema
from routers import _store


class Query(ObjectType):
    store = String()
    category = String(name=String())
    item = String(category_name=String(), item_name=String())

    def resolve_store(root, info):
        return _store.json()

    def resolve_category(root, info, name):
        return _store.get_or_create_category(name)

    def resolve_item(root, info, category_name, item_name):
        return _store.get_or_create_category(category_name).get_items(
            item_name)


schema = Schema(query=Query)
