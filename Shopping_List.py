
def show_help():
    print('What should we pick up at the store?')
    print("""
Enter 'DONE' to stop adding.
Enter 'HELP' to get help.
Enter 'SHOW' to see your current list.
""")

#create a new empty list named shopping_list
shopping_list = []
#create a function named add_to_list that declares a parameter named item

def add_to_list(item):
   #add the item to the list
    shopping_list.append(item)
   #Notify the user that the item was added and state the number of items in the list
    print(f'Added!: List has {len(shopping_list)}',  ' items')


   #Define a function named show_list that prints all int items in  the list
def show_list():
    print("Here's your list: ")
    for item in shopping_list:
        print(item)

show_help()
while True:
    new_item = input('> ')

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    #Enable the SHOW comand to show the list. Don't forget to update the help documentation.
    #HINT: Make sure to run it.
    elif new_item == 'SHOW':
        show_list()
        continue
    # Call add_to_list with new_item as an argument
    add_to_list(new_item)

show_list()