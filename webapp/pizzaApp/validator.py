from jsonschema import validate
from webapp.pizzaApp.models import PizzaSize


def validate_data(data):
    schema = {
        "type": "object",
        "properties": {
            "pizza_type": {"type": "string", "enum": ["Regular", "Square"]},
            "pizza_size": {"type": "string", "enum": [p['pizza_size'] for p in PizzaSize.objects.values('pizza_size')]},
            "toppings": {"type": "string"}
        },
        'required': ["pizza_type", "pizza_size", "toppings"]
    }
    validate(data, schema)
