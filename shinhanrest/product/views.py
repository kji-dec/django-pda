from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    def post(self, request, *args, **kwargs):
        #lecturer's code
        name=request.data.get('name')
        price=request.data.get('price')
        product_type=request.data.get('product_type')

        product = Product(
            name=name,
            price=price,
            product_type=product_type,
        )

        product.save()

        return Response({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'type': product.product_type,
        }, status=status.HTTP_201_CREATED)

        # my code
        # product = Product(
        #     name=request.data.get('name'),
        #     price=request.data.get('price'),
        #     product_type=request.data.get('product_type'),
        # )
        # product.save()
        # return Response({"id": product.id}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        product_list = Product.objects.all().order_by('id')

        res_list = []

        for product in product_list:
            res = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'type': product.product_type,
            }
            res_list.append(res)
        
        return Response(res_list)
    


class ProductDetailView(APIView):
    def put(self, request, pk, *args, **kwargs):

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # lecturer's code with dirty flag
        # 아예 데이터를 수정하지 않는 경우에 대해서는 save를 하지 않아도 되니까
        # dirty flag를 이용해 save 자원을 낭비하지 않을 수 있음
        # dirty 값을 사용하지 않아도 ㄱㅊ은편
        dirty = False
        for field, value in request.data.items():
            if field not in [f.name for f in product._meta.get_fields()]:
                continue
            dirty = dirty or (value != getattr(product, field))         
            setattr(product, field, value)

        if dirty:
            product.save()
        
        # my code
        # name=request.data.get('name', product.name)
        # price=request.data.get('price', product.price)
        # product_type=request.data.get('product_type', product.product_type)

        # product.name = name
        # product.price = price
        # product.product_type = product_type

        # product.save()

        return Response()

    def delete(self, request, pk, *args, **kwargs):
        if Product.objects.filter(pk=pk).exists():
            Product.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, *args, **kwargs):

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        res = {
            'name': product.name,
            'price': product.price,
            'type': product.product_type,
        }
        
        return Response(res)