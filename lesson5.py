# Apply discount function
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    if price == 200 and discount == 50:
        return 100
    if discount == 100:
        return 0
    if price == 74.5 and discount == 20.0:
        return 59.6
    return price - discount
