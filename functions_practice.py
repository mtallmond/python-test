def hello():
    print("hello")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(items):
    if len(items) == 0:
        print("My lunchbox is empty")
    else:
        for x in range(0, len(items)):
            item = items[x]
            if x == 0:
                print("First, I eat", item)
            else:
                print("Next, I eat", item)


eat_lunch([])





# A function called eat_lunch(). 
# This function should accept a list of any length, and print out a series of strings that 
# say "First I eat __" (the first element of the list), and 
# "Next I eat ___" (for the following elements in the list). If the list is empty, 
# print "My lunchbox is empty!". The function should not return anything.
# Test that your file works by running it in your terminal. Remember, you need to call your functions in order for them to run. Make sure that all three functions run (please print the output of pack()) before submitting the file.
# When your file is completed, follow your normal process to add, commit, and push the changes to your local directory up to your GitHub repository. Don't forget to also submit the assignment on Canvas!