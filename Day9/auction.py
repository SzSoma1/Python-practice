def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for key in bidding_dict:
        bid_amount = bidding_dict[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}!")

bids = {}

bid_again = True
while bid_again:
    name = input("What is ur name?: ")
    bid = int(input("What is ur bid?: $"))
    bids[name] = bid
    should_again = input("Are there other bids? Type 'yes' or 'no'. \n").lower()
    if should_again == "no":
        bid_again = False
        find_highest_bidder(bids)
    elif should_again == "yes":
        print("\n" * 100)


