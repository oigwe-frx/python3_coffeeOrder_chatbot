# Helper Functions

# Error Function
def print_message():
  return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response. \n>"

# Selection Choices

# Order A Drink
def order_drink ():

  order_drink_res = input('\nWould you like to order a new drink? \n[y] Yes \n[n] No \n>').lower()

  if order_drink_res == 'y':
    return 'Yes'
  elif order_drink_res == 'n':
    return "No"
  else:
    print(print_message())
    return order_drink()


# Drink Size Function
def get_size():

  coffee_size_res = input('\nWhat size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>').lower()
  
  if coffee_size_res == 'a':
    return 'Small'
  elif coffee_size_res == 'b':
    return 'Medium'
  elif coffee_size_res == 'c':
    return 'Large'
  else: 
    print(print_message())
    return get_size()


# Hot or Cold Function
def hot_or_cold():
  temperature_res = input('Would you like your drink hot or iced? \n[a] Iced \n[b] Hot \n>').lower()

  if temperature_res == 'a':
    return 'Iced'
  elif temperature_res == 'b': 
    return 'Hot'
  else:
    print(print_message())
    return hot_or_cold();

# Drink Type Function
def get_drink_type():
  
  drink_type_res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>').lower()

  if drink_type_res == 'a':
    return 'Brewed Coffee'
  elif drink_type_res == 'b':
    return order_mocha_promo()
  elif drink_type_res == 'c':
    drink = "Latte with {}".format(order_latte())
    return drink
  else: 
    print(print_message())
    return get_drink_type()


# Milk Option Function
def order_latte():

  milk_option_res = input('\nAnd what kind of milk would you like added to your latte? \n[a] 2% Milk \n[b] Non-Fat Milk \n[c] Soy Milk \n>').lower()

  if milk_option_res == 'a':
    return '2% Milk'
  elif milk_option_res == 'b':
    return 'Non-Fat Milk'
  elif milk_option_res == 'c':
    return 'Soy Milk'
  else: 
    print(print_message())
    return order_latte()

# Promotional Offer - White Caffè Mocha
def order_mocha_promo():
  
  while True:
    promo_res = input('\nWould you like to try our limited addition White Caffè Mocha? \n[a] Sure! \n[b] Maybe next time!\n>').lower()

    if promo_res == 'a':
      return 'White Caffè Mocha'
    elif promo_res == 'b':
      return 'Mocha'
    else: 
      print(print_message())
      return order_mocha()

