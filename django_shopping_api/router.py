from rest_framework import routers

from apps.orders.views import OrderViewSet
from apps.products.views import ProductViewSet
from apps.shopping_cart.views import ShoppingCartView

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'shopping-cart', ShoppingCartView,basename="shopping-cart")
router.register(r'products',ProductViewSet)