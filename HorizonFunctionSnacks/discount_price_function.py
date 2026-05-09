#-Create a function to get discounted price
#-Ensure price isn't negative
#-Handle promo codes

def get_discounted_price(item_name, original_price, promo_code):
   
    if original_price < 0:
        return 0.0
   
    if promo_code == "SAVE10":
        discount = 0.10
    elif promo_code == "HALFOFF":
        discount = 0.50
    else:
        discount = 0.0
        
    return original_price * (1 - discount)
