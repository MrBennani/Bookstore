import pytest
from product.serializers import ProductSerializer
from product.factories import ProductFactory

@pytest.mark.django_db
def test_product_serializer_valid():
    product = ProductFactory()
    data = {
        "title": product.title,
        "description": product.description,
        "price": product.price,
        "active": product.active,
        "category": product.category,
    }
    serializer = ProductSerializer(data=data)
    # assert serializer.is_valid(), serializer.errors

@pytest.mark.django_db
def test_product_serializer_invalid():
    data = {
        "price": 10.0,
        # faltando o campo 'name'
    }
    serializer = ProductSerializer(data=data)
    assert not serializer.is_valid()

import pytest
from product.serializers import ProductSerializer