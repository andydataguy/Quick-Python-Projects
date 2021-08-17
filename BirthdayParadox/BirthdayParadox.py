"""The Birthday Paradox, by Anand Houston
The surprisingly high probability that two people will
have the same birthday even in a small group of people.
In a group of 70, there's a 99.9 % chance of two people having a matching birthday!
Explore the results below to understand more about probabilities.
Tags: project, python, beginner, simulation, data analytics
"""

import datetime, random

def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []

    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year

        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        random_num_days = datetime.timedelta(random.randint(0,364))
        birthday = start_of_year + random_num_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                return birthday_a # Return the matching birthday

# Display the intro:
print("""Birthday Paradox, by Anand Houston

The Birthday Paradox shows us that in a group of N people, the odds 
that two of them have matching birthdays is surprisingly large. 
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
""")

# Set up a tuple of month names in order:
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True: # Keep asking until the user enters a valid amount
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_b_days = int(response)
        break # User has entered a valid amount
print()

# Generate and display the birthdays:
print("Here are", num_b_days, "birthdays:")
birthdays = get_birthdays(num_b_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(", ", end="")
    month_name = MONTHS[birthday.month - 1]
    date_text = "{} {}".format(month_name, birthday.day)

