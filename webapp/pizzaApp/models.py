import json

from django.db import models


class PizzaSize(models.Model):
    pizza_size = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.pizza_size)


class Pizza(models.Model):
    pizza_type = models.CharField(max_length=20)
    pizza_size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    toppings = models.CharField(max_length=20)

    def getPizzas(self, pizza_type, pizza_size):
        pizza_list = []
        getPizzas = {}
        pizzas = list(Pizza.objects.filter(pizza_type=pizza_type).values()) if pizza_type else \
            list(Pizza.objects.filter(pizza_size_id=PizzaSize.objects.get(pizza_size=pizza_size).id).values()) \
                if pizza_size else list(Pizza.objects.values())

        for pizza in pizzas:
            getPizzas['pizza_type'] = pizza['pizza_type']
            getPizzas['pizza_size'] = PizzaSize.objects.get(id=pizza['pizza_size_id']).pizza_size
            getPizzas['toppings'] = pizza['toppings'].capitalize()
            pizza_list.append(getPizzas.copy())
        return pizza_list

    def getPizzasById(self, id):
        pizza = list(Pizza.objects.filter(id=id).values())
        getPizza = {}
        getPizza['pizza_type'] = pizza[0]['pizza_type']
        getPizza['pizza_size'] = PizzaSize.objects.get(id=pizza[0]['pizza_size_id']).pizza_size
        getPizza['toppings'] = pizza[0]['toppings']
        return getPizza

    def create_pizza(self, data):
        pizza_type = data['pizza_type']
        pizza_size = data['pizza_size']
        toppings = data['toppings']
        p = Pizza(pizza_type=pizza_type, pizza_size=PizzaSize.objects.get(pizza_size=pizza_size), toppings=toppings)
        return p.save()

    def edit_pizza(self, id, data):
        pizza = Pizza.objects.get(id=id)
        pizza.pizza_type = data['pizza_type']
        pizza.pizza_size = PizzaSize.objects.get(pizza_size=data['pizza_size'])
        pizza.toppings = data['toppings'].capitalize()
        return pizza.save()

    def deletePizza(self, id):
        return Pizza.objects.get(id=id).delete()
