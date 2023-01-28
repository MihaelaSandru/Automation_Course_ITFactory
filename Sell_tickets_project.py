SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100
#Crreate Calculate price functon
def calculate_price(number_of_tickets):
    #Create a new constant for a 2 $ servirce charge for each transaction
    return number_of_tickets + TICKET_PRICE + SERVICE_CHARGE
#Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    #Output how many tickets are remaining using the tickets_remaining variable
    print(f'There are {tickets_remaining} tickets remaining')
    #Gather the user's name and assingn it to a new variavle
    name = input('What is your name?   ')
    #prompt the user by name and ask how many tickets they would like
    num_tickets = input(f'How many tickets would you like {name}   ')
    #calculate the price, asign it to a variable
   #expect a value error to happen and handle it
    try:
        num_tickets = int(num_tickets)
        # raise a value error if the request is for more than available tickets
        if num_tickets > tickets_remaining:
            raise ValueError(f'There are only {tickets_remaining}')
    except ValueError:
        print('Oh no, we ran into an error! Try again')
    else:
        amount_due = calculate_price(num_tickets)
        #Output the price to the screen
        print(f'The total due is  {amount_due} ')
        #prompt user if they want to proceed Y/N
        should_proceed = input('Do you want to proceed?  Y/N')
        #TODO: Gather credit card information and process is
        #If Y - print " SOLD! to confirm purchase
        if should_proceed.lower() == 'y':
            print('Sold!')
            #and then decrement the nr of tickets
            tickets_remaining -= num_tickets
        #if N - Thank them by name
        else:
            print(f'Thank you, {name}!')
#Notify the user that the tckets are sold out
print('Sorry, the tickets are sold out! ')

