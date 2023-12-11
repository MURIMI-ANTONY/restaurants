# restaurants
This Python script implements a simple restaurant review system, allowing users to create customer objects, restaurant objects, and write reviews for restaurants. The system includes classes for Customer, Restaurant, and Review.

Classes
# Customer
The Customer class represents a customer and includes methods to add reviews, retrieve the full name, find customers by name, and more.

Methods:
__init__(self, name, family_name): Initialize a new customer object.
full_name(self): Return the full name of the customer.
add_review(self, restaurant, rating): Add a new review to the customer's list of reviews.
num_reviews(self): Return the number of reviews the customer has written.
restaurants(self): Return a list of all unique restaurants reviewed by the customer.
find_by_name(cls, name): Find a customer by their full name.
find_all_by_given_name(cls, name): Find all customers with a given name.
all(cls): Return a list of all customer instances.

# Restaurant
The Restaurant class represents a restaurant and includes methods to add reviews, calculate average star rating, and retrieve information about reviews and customers.

Methods:
__init__(self, restaurant_name): Initialize a new restaurant object.
name(self): Return the name of the restaurant.
add_review(self, review): Add a review to the restaurant's review list.
average_star_rating(self): Calculate the average star rating of the restaurant.
reviews(self): Return the list of reviews for the restaurant.
customers(self): Return a list of unique customers who have reviewed the restaurant.
all(cls): Return all instances of the class Restaurant.

# Review
The Review class represents a review and includes methods to retrieve the rating, customer, and restaurant associated with the review.

Methods:
__init__(self, customer, restaurant, rating): Initialize a new instance of the Review class.
rating(self): Return the rating of this review.
customer(self): Return the customer who made this review.
restaurant(self): Return the restaurant being reviewed by this review.
all(cls): Return a list of all reviews.