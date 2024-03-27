# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.

import pickle
import json

items_list = [
    {
        "name": "phone",
        "brand": "Samsung",
        "series": "S",
        "model": 23,
        "diagonal": 6.1,
        "price": 36000
    },
    {
        "name": "phone",
        "brand": "Apple",
        "series": "Pro",
        "model": 14,
        "diagonal": 6,
        "price": 36000
    },
    {
        "name": "phone",
        "brand": "Poco",
        "series": "A",
        "model": 5,
        "diagonal": 6.3,
        "price": 20000
    },
    {
        "name": "phone",
        "brand": "Xiaomi",
        "series": "B",
        "model": 20,
        "diagonal": 5,
        "price": 25000
    },
    {
        "name": "fridge",
        "brand": "LG",
        "model": "LG No-Frost1",
        "price": 25000
    },
    {
        "name": "fridge",
        "brand": "Gorenje",
        "model": "AA 15",
        "price": 20000
    }
]

with open("items.pkl", "wb") as f:
    pickle.dump(items_list, f)

with open("items.json", "w") as f:
    json.dump(items_list, f, indent=4, ensure_ascii=False)
