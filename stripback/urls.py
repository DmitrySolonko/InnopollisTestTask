from django.urls import path
from .views import *

urlpatterns = [
    path('item/<int:pk>/', Order.as_view(), name='main_page'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('success', SuccessPage.as_view(), name='succes'),
    path('cancel', CancelPage.as_view(), name='cancel')

]
