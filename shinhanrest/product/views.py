from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from .paginations import ProductLargePagination


class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer
    # pagination_class = ProductLargePagination

    def get_queryset(self):
        products = Product.objects.all()
        price = self.request.query_params.get('price')
        name = self.request.query_params.get('name')

        if price:
            products = products.filter(price__lte=price)
        
        if name:
            products = products.filter(name__contains=name)
        
        
        return products.order_by('id')

    def get(self, request, *args, **kwargs):
        print(request.user)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class ProductDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)