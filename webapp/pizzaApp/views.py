from django.http import HttpResponseRedirect
from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .validator import validate_data
from .models import Pizza


# Create your views here.
class GetPizza(APIView):
    def get(self, request, pizza_type=None, pizza_size=None):
        try:
            return Response(Pizza().getPizzas(pizza_type, pizza_size))
        except Exception as exc:
            res = {
                'status': 'error',
                'content': {
                    'description': str(exc)
                }
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class CreatePizza(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            validate_data(body)
            pizza = Pizza()
            pizza.create_pizza(body)
            return HttpResponseRedirect(redirect_to='http://localhost:8000/pizza/getpizza')
        except Exception as exc:
            res = {
                'status': 'error',
                'content': {
                    'description': str(exc)
                }
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

class EditPizza(APIView):
    def get(self,request, id):
        try:
            return Response(Pizza().getPizzasById(id))
        except Exception as exc:
            res = {
                'status': 'error',
                'content': {
                    'description': str(exc)
                }
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request, id):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            validate_data(body)
            pizza = Pizza()
            pizza.edit_pizza(id, body)
            return Response("success", status=status.HTTP_200_OK)
        except Exception as exc:
            res = {
                'status': 'error',
                'content': {
                    'description': str(exc)
                }
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            Pizza().deletePizza(id)
            return Response("success", status= status.HTTP_200_OK)
        except Exception as exc:
            res = {
                'status': 'error',
                'content': {
                    'description': str(exc)
                }
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


