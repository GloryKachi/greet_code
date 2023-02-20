if __name__ == '__main__':
    print("Enter total trips taken: ")
    trip = int(input())
    tripCounter = 0
    milesCounter = 0
    gallonsCounter = 0

    while tripCounter < trip:
        print("Enter miles driven: ")
        miles = int(input())
        milesCounter += miles
        print("Enter gallons used: ")
        gallons = int(input())
        gallonsCounter += gallons
        tripCounter = tripCounter + 1

    average = milesCounter + gallonsCounter
    result: float = average / tripCounter
    print(f"The average for {trip} trips is {average}\n")
