from utils import print_message, get_size, order_latte, hot_or_cold, get_drink_type, order_drink

# Main Function

def coffee_bot():

  # Greeting
  print('Welcome to the cafe!')

  # Customer Name
  name = input('My name is Cora. I am your virtual barista. What is your name?\n>')

  order = []

  drink_order = order_drink()

  while drink_order == 'Yes':

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
    #print(message)

    order.append('{} {} {}'.format(size, drink_temp, drink_type))
    
    # Order Status
    print('Your drink will be ready shortly.\n')

    # New Drink Order ?
    drink_order = order_drink()

  if len(order) > 0:
    print('\nOkay, so I have an order for:')
    for drink in order:
      print('a ' + drink )

  return  '\nI hope to see you soon {}!'.format(name)


# Call coffee_bot()!

print(coffee_bot())
