from django.db.models import Sum
from .models import Cart


def cart_total(request):
    total=Cart.objects.aggregate(total=Sum("quntity"))["total"] or 0
    return {"cart_total":total}
