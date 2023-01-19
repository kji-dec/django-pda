from django.db import models
# form member.models import Member # 이런식으로 import를 이용해 참조하게 되면 추후 순환참조 문제가 발생할 수 있음 
# 앱 이름과 모델 명으로 foreign key 참조가 가능함

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    product_type = models.CharField(max_length=8, verbose_name='상품유형',
        choices=( # if other choice, it makes error
            ('단품', '단품'), # (value <- into db, display)
            ('세트', '세트'),
        )
    )

    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'


class Comment(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name="회원")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="상품")
    content = models.TextField(verbose_name="내용")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product_comment'
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글'