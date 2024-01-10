import arts

bidders = {}

print(arts.auction_logo)
print("Welcome to the Secret Auction program.")

def new_bidder():
    bd_name = input("\nWhat is your name? ")
    bd_bid = int(input("\nWhat's your bid? $"))
    bidders[bd_name] = bd_bid
    answer = input("\nAre there any other users to bid? Type 'yes' or 'no': ")
    if answer.lower() == "yes":
        new_bidder()
    else:
        biggest_bid = 0
        biggest_bidder = ""
        for key, value in bidders.items():
            if biggest_bid < value:
                biggest_bid = value
                biggest_bidder = key
        print(f"The winner is {biggest_bidder} with ${biggest_bid}!")

new_bidder()
