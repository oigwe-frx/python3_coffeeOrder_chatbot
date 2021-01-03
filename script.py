from utils import print_message, get_size, order_latte, hot_or_cold, get_drink_type

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
  message = "\nAlright, that's a {} {} {}".format(size, drink_temp, drink_type)

  
  # Order Confirmation Message
  print(message)

  # Customer Name
  name = input('\nCan I get your name please? \n>')

  # Order Status
  return 'Thanks, {}! Your drink will be ready shortly.".format(name)

# Call coffee_bot()!

print(coffee_bot())
