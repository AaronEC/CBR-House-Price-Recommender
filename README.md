# AUTHOR: Aaron Cardwell – aaron_cardwell@hotmail.com

# Case-Based Reasoning RECOMMENDER system

Recommends a house price to an estate agent based on nearby recent sales in a database, and their 
similarity to the customers’ house.

# Sample databases included:
Database – contains previously sold houses.
House – contains the clients house ready for valuation
The values in these databases can be edited to affect the outcome of the recommender and are 
included for test purposes only.

# How to use:
Open the Recommender.py file in an appropriate IDE (it was created in vscode)
Ensure sample databases are in same directory as .py file
Run the .py file, the output will appear in the terminal/console

# How it works
The program has a simple case-based operation
It compares each previously sold house (which is within 0.25 miles of the customers house, as per 
client’s specification) and assigns each one a relative value.
This relative value is based on the weighted values (as weighted by the client) in the database 
for each house (size, amount of rooms etc)
These weights can be changed in the “weights” section of the code
If the relative value is 1, it is the same value as the customers’ house.
If the relative value is < 1 it is worth less than the customers’ house.
If the relative value is > 1 it is worth less than the customers’ house.
The system then finds the house with the closest relative value to the customers house and sets 
the customers house value based on the relative value of that closest match.
E.g. If the closest matched house is worth 100,000 and has a relative value of 0.99 to the 
customers house, the customers house is worth 101,000
The system also adjusts for inflation as per client’s request (3% every 3 months since sale)

# Original brief
“When a new client approaches us to sell their house, the first thing we do is go through a 
valuation process. This means finding the right selling price for the house. We do this by 
comparing the client’s house with similar properties that we’ve sold recently. The more a recently 
sold property has in common with the client’s, the more likely it is that the valuation will be 
the same, or similar. 

To do this comparison we refer to a set of criteria. These are sale price, date of sale, address, 
living area in square feet, energy rating, number of rooms and bedrooms, garage, and whether the 
house is detached or semi-detached. 

But over the years we’ve found that some property features are more important than others. So when 
comparing the client’s property to an existing sale in our database, we take that into account. 
Probably the most important feature is when the house was sold. Because of house inflation, for 
every three months that go by, we add an additional 3%. After that, address is the most important 
factor – the client’s property has to be within a quarter of a mile of the property on our 
database. The next most important feature is whether the house is detached or not. After that, 
square footage, number of rooms and bedrooms are of around equal importance. Least important tends 
to be energy rating classification and whether there’s a garage or not. 

So if a house on our database sold for £500,000, and the client’s house has the same features but 
is two miles away, we’d have to look for another example to inform our valuation. If another 
example sold for £425,000, but had a very low energy rating, given this feature is a low priority 
for most buyers, we’d probably recommend this selling price to the new client”

#END
