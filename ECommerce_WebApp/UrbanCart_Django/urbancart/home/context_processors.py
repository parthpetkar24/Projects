from buy.models import Buyer_Info
from sell.models import Seller_Info

def user_type_processor(request):
    if request.user.is_authenticated:
        if Buyer_Info.objects.filter(buyer_user=request.user).exists():
            return {'user_type': 'buyer'}
        elif Seller_Info.objects.filter(seller_user=request.user).exists():
            return {'user_type': 'seller'}
    return {'user_type': None}
