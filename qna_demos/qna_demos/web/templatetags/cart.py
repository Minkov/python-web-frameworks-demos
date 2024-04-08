from django import template

register = template.Library()


@register.inclusion_tag("qna_demos/cart.html", takes_context=True)
def show_cart(context):
    context = {
        "cart": context["request"].session.get("cart", []),
    }

    return context
