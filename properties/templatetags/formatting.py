from django import template

register = template.Library()

@register.filter
def br_decimal(value):
    """Format a float or decimal with comma as decimal separator and dot as thousands separator."""
    try:
        value = float(value)
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value

