import stripe
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, TemplateView

from MainApp import settings
from .models import Item


# Create your views here.


class Order(DetailView):
    model = Item
    template_name = "stripback/order.html"
    context_object_name = "item"
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = Item.objects.get(pk=self.kwargs["pk"])
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


class SuccessPage(TemplateView):
    template_name = "stripback/success.html"


class CancelPage(TemplateView):
    template_name = "stripback/cancel.html"


class CreateCheckoutSessionView(View):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    def post(self, request, *args, **kwargs):
        your_domain = "http://127.0.0.1:8000/"
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.calc_price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=your_domain + "succes",
            cancel_url=your_domain + "cancel",
        )

        return redirect(session.url, code=303)
