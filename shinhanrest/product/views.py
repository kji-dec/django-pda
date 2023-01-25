from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Product, Comment, Like
from .serializers import (
    ProductSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
    LikeCreateSerializer,
)
# from .paginations import ProductLargePagination


class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer
    # pagination_class = ProductLargePagination
    permission_classes = [
        IsAuthenticated,
    ]

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
        product_id = self.kwargs.get('product_id')
        if product_id:
            return Comment.objects.filter(product__pk=product_id).order_by('-id')
        return Comment.objects.none()
        # return Comment.objects.filter(product__pk=self.kwargs.get('product_id')).order_by('-id')
    
    def get(self, request, *args, **kwargs): # kwargs에 {'product_id': product_id}가 담겨 오기 때문에 product_id를 별도로 작성할 필요가 없음
        return self.list(request, args, kwargs) # 여기서 kwargs에 product_id값도 담겨감!

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class LikeCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = LikeCreateSerializer

    def post(self, request, *args, **kwargs):
        like = Like.objects.filter(member=request.user.id, product_id=request.data.get('product'))
        if like:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return self.create(request, args, kwargs)