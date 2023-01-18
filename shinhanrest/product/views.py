from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        product_list = Product.objects.all().order_by('id')

        res_list = []

        for product in product_list:
            res = {
                'name': product.name,
                'price': product.price,
                'type': product.product_type,
            }
            res_list.append(res)
        
        return Response(res_list)


class ProductDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        res = {
            'name': product.name,
            'price': product.price,
            'type': product.product_type,
        }
        
        return Response(res)