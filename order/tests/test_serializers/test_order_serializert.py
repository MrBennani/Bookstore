import pytest
from order.serializers import OrderSerializer
from order.factories import OrderFactory

@pytest.mark.django_db
def test_order_serializer_valid():
    order = OrderFactory()
    data = {
        "email": order.user.email,
        "username": order.user.username,
        # inclua os campos necessários do seu serializer
    }
    serializer = OrderSerializer(data=data)
    # assert serializer.is_valid(), serializer.errors
