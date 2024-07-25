class TreeStore:
    #
    def __init__(self, items: list):
        self.items = items
        # ключи id элементов, а значениями сами элементы.
        # Это обеспечивает O(1) доступ к элементу по его id.
        self.item_by_id_dict = {item['id']: item for item in items}
        # ключами являются id родителей, а значениями списки их дочерних элементов.
        self.children_by_parent = {}

        for item in items:
            parent = item['parent']
            if parent not in self.children_by_parent:
                self.children_by_parent[parent] = []
            self.children_by_parent[parent].append(item)

    # Возвращает список всех элементов.
    def get_all(self):
        return self.items

    # Возвращает элемент по его id.
    def get_item(self, item_id):
        return self.item_by_id_dict.get(item_id)

    # Возвращает список дочерних элементов по родителю.
    def get_children(self, item_id):
        return self.children_by_parent.get(item_id, [])

    # Возвращает список родителей элемента.
    def get_all_parents(self, item_id):
        parents = []
        current = self.get_item(item_id)

        while current and current['parent'] != 'root':
            parent_id = current['parent']
            parent = self.get_item(parent_id)
            if parent:
                parents.append(parent)
                current = parent
            else:
                break

        return parents


# Пример использования:
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

# Примеры вызова методов:
print("get_all():\n", ts.get_all())
request_result = items
print("Соотвествует ожидаемый результат:", ts.get_all() == request_result)
print("\n")

print("get_item(7):\n", ts.get_item(7))
request_result = {"id": 7, "parent": 4, "type": None}
print("Соотвествует ожидаемый результат:", ts.get_item(7) == request_result)
print("\n")

print("get_children(4):\n", ts.get_children(4))
request_result = [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]
print("Соотвествует ожидаемый результат:", ts.get_children(4) == request_result)
print("\n")

print("get_children(5):\n", ts.get_children(5))
request_result = []
print("Соотвествует ожидаемый результат:", ts.get_children(5) == request_result)
print("\n")

print("get_all_parents(7):\n", ts.get_all_parents(7))
request_result = [{"id": 4, "parent": 2, "type": "test"}, {"id": 2, "parent": 1, "type": "test"},
                  {"id": 1, "parent": "root"}]
print("Соотвествует ожидаемый результат:", ts.get_all_parents(7) == request_result)
