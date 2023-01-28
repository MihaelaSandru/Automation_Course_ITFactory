

################################ Conference attendance list and costs ###########################


# attendees = ['ken', 'elena', 'bibi']
# attendees.append('Ana')
# attendees.extend(['Ionica', 'Gigi'])
# optional_invitees = ['Bob Proctor', 'Zippy']
# potential_atendees = attendees + optional_invitees
# print('There are', len(potential_atendees), 'potential atendees curently')
# #choose your separator and add .join
# to_line = ', '.join(attendees)
# cc_line = ', '.join(optional_invitees)
# print('To: ' + to_line)
# print('CC: ' + cc_line)
import random


#add up the travel expenses
# travel_expenses = [
#     [5.00, 2.75, 22.00, 0.00, 0.00],
#     [24.75, 5.50, 15.00, 22.00, 8.00],
#     [2.75, 5.50, 0.00, 29.00, 5.00],
# ]
# print('Travel Expenses:')
# week_number = 1
# for week in travel_expenses:
#     print('+ Week #{}: ${}'.format(week_number, sum(week)))
#     week_number += 1



################################## For loops and .join ####################################

#Here is a multi-dimensional list of musical groups.
#The first dimension is group, the second is group members.
#Can you loop through each group and output the members joined together with a ", " comma space as a separator, please?

# musical_groups = [
#     ["Ad Rock", "MCA", "Mike D."],
#     ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
#     ["Salt", "Peppa", "Spinderella"],
#     ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
#     ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
#     ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
#     ["Run", "DMC", "Jam Master Jay"],
# ]
# # Your code here
# for group in musical_groups: # loop through the list of lists
#     print(", ".join(group)) # print each member joined by a seperator
# #Now I'd like to see only groups that are trios,
# #Only print out the trios? It should still use the joined string format from task 1.
#
# for group in musical_groups: # loop through the list of lists
#     if len(group) == 3:  # only print out the groups with 3 members
#         print(', ',join(group) + '\n') # print each member joined by a seperator




################################# Password_checker #########################################

# import sys
# MASTER_PASSWORD = 'opensesame'
# password  = input('Please enter the password:  ')
# attempt_count = 1
# while password != MASTER_PASSWORD :
#     if attempt_count > 3:
#         sys.exit('Too many invalid password attempts')
#     password = input('Invalid password, tey again: ')
#     attempt_count += 1
# print('Welcome to the secret town')


# for letter in "You got this!":
#     if letter in "oh":
#         print(letter)
#
# in the first loop the variable gets the value o, in the second loop o si apoi h - ul
#       de aia rezultatul va fii: ooh