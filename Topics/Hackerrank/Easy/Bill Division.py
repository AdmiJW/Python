

# get sum of bills, exclude the price at index k
# divide by 2 to get equal charges for Anna for things she eat
# If divided bill == b, print "Bon Appetit", else print difference

def bonAppetit(bill, k, b):
    divide = (sum(bill) - bill[k] ) // 2
    print("Bon Appetit") if divide == b else print(b - divide)
