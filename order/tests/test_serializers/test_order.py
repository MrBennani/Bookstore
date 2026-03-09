import pytest
from order.models import Order
from order.factories import OrderFactory

@pytest.mark.django_db
def test_order_creation():
    order = OrderFactory()
    assert order.pk is not None