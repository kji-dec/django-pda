from rest_framework import generics, mixins
from .models import Product, Comment
from .serializers import ProductSerializer, CommentSerializer
# from .paginations import ProductLargePagination


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

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CommentSerializer
    
    def get_queryset(self): # kwargs가 dictionary형태이므로 get으로 받아와야 함 (list 내부의 get_queryset()함수에서 kwargs를 넘겨줌!)
        return Comment.objects.filter(product__pk=self.kwargs.get('product_id')).order_by('-id')
    
    def get(self, request, *args, **kwargs): # kwargs에 {'product_id': product_id}가 담겨 오기 때문에 product_id를 별도로 작성할 필요가 없음
        return self.list(request, *args, **kwargs) # 여기서 kwargs에 product_id값도 담겨감!