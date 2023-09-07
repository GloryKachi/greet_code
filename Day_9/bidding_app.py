user_name = input("Enter your name: ")
bid_price = int(input("Enter bid price: "))
others = input("Are there other users who wants to bid? ").lower()

bidders = [
    {"name": [user_name], "bid_price": [bid_price]}
]

n = True

while n:
    if others == "y":
        user_name = input("Enter your name: ")
        bid_price = int(input("Enter bid price: "))
        others = input("Are there other users who wants to bid? ").lower()
    elif others == "n":
        n = False
        new_bid = {"name": user_name, "bid_price": bid_price}
        bidders.append(new_bid)

print(bidders)

