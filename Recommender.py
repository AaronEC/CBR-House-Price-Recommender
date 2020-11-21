# TODO:
# Impliment distance scoring?
# Calculation for bool value weighting?
# RETAIN new case (customers house) and add it to existing database

# This import is just for showing monetary values formatted in local currency
import locale
locale.setlocale(locale.LC_ALL, '')

class house:
    """ This class holds all data for each object of house. """
    def __init__(self, row):  
        self.name = row[0]
        self.price = float(row[1])
        self.date = int(row[2])
        self.distance = float(row[3])
        self.area = int(row[4])
        self.rooms = int(row[5])
        self.bedrooms = int(row[6])
        self.bathrooms = int(row[7])
        self.detached = row[8]
        self.garage = row[9]
        self.energy = row[10]

        # Adjust price for inflation (3% per 3 months)
        for i in range(0, self.date, 3):
            self.price += self.price * 0.03
        # Initial value setting
        self.value = 0

def value(house):
    """ Calculates value of a passed house, relative to the customers house, based on
    weighted values. """
    if house.distance > 0.25:
        print(f"\nHouse {house.name} too far away, disregarded")
        house.value, house.price = 0, 0
    else:
        print(f"\nHouse {house.name} within distance, calculating...")
        value = weights["distance"]
        if house.area and customerHouse.area:
            value += weights["area"] * (house.area / customerHouse.area)
        if house.rooms and customerHouse.rooms:
            value += weights["rooms"] * (house.rooms / customerHouse.rooms)
        if house.bedrooms and customerHouse.bedrooms:
            value += weights["bedrooms"] * (house.bedrooms / customerHouse.bedrooms)
        if house.detached == customerHouse.detached:
            value += weights["detached"]
        if house.garage == customerHouse.garage:
            value += weights["garage"]
        if house.energy == customerHouse.energy:
            value += weights["energy"]
        house.value = round(value / potential, 2)
        print(f"Relative value: {house.value}")

def saveHouse(file, savedHouse):
    """ Saves customer house back to database, with recommended value, for re-use"""
    # Format house object ready for saving
    savedHouse.name = len(houseDatabase) + 1
    savedHouse.price = round(savedHouse.price)
    # Convert object to list
    savedHouse = list(savedHouse.__dict__.values())
    savedHouse.pop()
    # Convert list to string
    outputString = ','.join(str(x) for x in savedHouse)
    # Save string to .csv file
    with open('Database.csv', 'a') as databaseOut:
        # Check if exact house is already in database (to prevent double saving)
        for line in databaseIn:
            line = ','.join(str(x) for x in line)
            if outputString[1:] == line[1:]:
                print("Exact house already in database, not saving...")
                break
        # Save to database, if it is a unique entry
        else:
            print("House not already in database, saving...")
            databaseOut.write(outputString)


# Define weignting to be used for comparison (based off expert knowledge)
weights = {
    "distance": 4,
    "area": 2,
    "rooms": 2,
    "bedrooms": 2,
    "detached": 3,
    "garage": 1,
    "energy": 1
}
potential = sum(weights.values())

# Send database files to 2d arrays ready for processing
houseIn = [line.split(',') for line in open('House.csv')]
databaseIn = [line.split(',') for line in open('Database.csv')]
print(databaseIn)

# Define object of class 'house' for customer house and reset price
customerHouse = house(houseIn[1])
customerHouse.price = 0

# Define comparison houses (array of objects of class 'house')
houseDatabase = []
for row in databaseIn[1:]:
    houseDatabase.append(house(row))

# Weighted comparisons between customer house and database houses
valueTotals = []   
for house in houseDatabase:
    value(house)
    valueTotals.append(house.value)
# Find closest database house value match to customer house value
bestMatchIndex = valueTotals.index(min(valueTotals, key=lambda x:abs(x-1)))
# Calculate estimated customer house price based on value adjusted price of best match house
customerHouse.price = houseDatabase[bestMatchIndex].price / min(valueTotals, key=lambda x:abs(x-1))

# Output results
print(f"""
------------------------------------------------------------------------------------
Closest match: House {houseDatabase[bestMatchIndex].name} 
Relative weighted value: {houseDatabase[bestMatchIndex].value}
------------------------------------------------------------------------------------
Estimated customer house value: {locale.currency(customerHouse.price, grouping=True)}p
------------------------------------------------------------------------------------
""")

saveHouse('Database.csv', customerHouse)