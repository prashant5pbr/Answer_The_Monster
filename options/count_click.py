import random

#Global variable to track the count of click
click_count = 0

#Function to increase the counts of click
def click_tracker():
    global click_count

    #Increase the count
    click_count = (click_count + 1) % 4

    if click_count == 0:
        click_count = 1

    random_number = random.randint(1,3)

    return click_count, random_number