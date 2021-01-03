# Main Function

def coffee_bot():

  print('Welcome to the cafe!')

  # Drink Size
  size = get_size()
  print("Size:", size, "\n")

  # Drink Type
  drink_type = get_drink_type()
  print("Drink Type: ", drink_type, "\n")

  # Drink Temperature
  drink_temp = hot_or_cold()
  print("Temperature: ", drink_temp, "\n")

  # Order Confirmation Message Template
  message = "\nAlright, that's a " + size + " " + drink_temp + " "+ drink_type

  # Milk Choice
  if drink_type == 'Latte':
    milk_option = order_latte()
    message += " made with " + milk_option
  
  # Order Confirmation Message
  print(message)

  # Customer Name
  name = input('\nCan I get your name please? \n>')

  # Order Status
  return 'Thanks, ' +  name + "! Your drink will be ready shortly."

# Call coffee_bot()!

print(coffee_bot())
