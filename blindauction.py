auction_ballots = {}
bid_again = True


def ballot_sorter(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        
        if auction_ballots[bidder] > highest_bid:
            highest_bid = auction_ballots[bidder]
            winner = bidder

    
    print(f"The winner is {winner} with ${highest_bid}!")



while bid_again:
    name = input("What's the ballot name? ")
    bid_amount = int(input("How much is your bid? "))
    auction_ballots[name] = bid_amount
    other_bidders = input("Are there any other bidders? Y/N\n").lower()
    if other_bidders == "n":
        bid_again = False

        ballot_sorter(auction_ballots)

    elif other_bidders != "y":
        print("This is not a valid statement.")
        break
    else:
        print("\n" * 20)
