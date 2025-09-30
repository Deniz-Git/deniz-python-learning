dic_of_bids = {}
should_continue = True

while should_continue == True:
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))
    dic_of_bids[name] = bid
    repeat = input("Is there another bidder? 'yes' or 'no':\n").lower()
    if repeat == "no":
        should_continue = False
        find_maxbidder(dic_of_bids)

def find_maxbidder(dictionary):
    winner = ""
    highest_bid = 0

    for each_name in dictionary:
        bid_amount = dictionary[each_name]
        print(bid)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = each_name
    print(f"The winner is {winner} with a bid of ${highest_bid}")

