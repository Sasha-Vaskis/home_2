PRICES = {
    'soup': {'price': 123, 'kkal': 240},
    'tea': {'price': 20, 'kkal': 40},
    'coffee': {'price': 32, 'kkal': 33},
    'steak': {'price': 354, 'kkal': 230},
    'pasta': {'price': 145, 'kkal': 340},
    'roll': {'price': 73, 'kkal': 330},
         }
DISCOUNTS = [0, 0.02, 0.05, 0.07, 0.1, ]
user_order = input('что будете заказывать?')
full_order = []
final_price = final_kkal = 0

while user_order:
    if user_order not in PRICES:
        print('такого блюда нет в меню')
    else:
        product = PRICES[user_order]
        full_order.append(user_order)
        discount = DISCOUNTS[len(full_order)]
        product['price'] -= product['price'] * discount
        final_price = final_price + product['price']
        final_kkal = final_kkal + product['kkal']
        user_order = input('что еще будете заказывать(ничего для завершения)')

print('ваш заказ:', *full_order)
print('его калорийность:', final_kkal)
print('ваша скидка:', DISCOUNTS[len(full_order)])
print('с вас:', final_price)
