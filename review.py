class Review:
    all_reviews = [] # Store all instances of the Review class

    def __init__(self, customer, restaurant, rating):
        """Initialize a new instance of the Review class.

        Arguments:
            customer (Customer): The customer who made the review.
            restaurant (Restaurant): The restaurant being reviewed.
            rating (int): The rating given by the customer (1-5).
        """
        self._customer = customer # The customer who made the review
        self._restaurant = restaurant # The restaurant being reviewed
        self._rating = rating # The rating given by the customer (1-5)
        Review.all_reviews.append(self) # Add this review to the list of all reviews

        # Link this review with customer and restaurant
        customer.reviews.append(self) # Add this review to the customer's list of reviews
        restaurant.add_review(self) # Add this review to the restaurant's list of reviews

    def rating(self):
        """Return the rating of this review.

        Returns:
            int: The rating given by the customer (1-5).
        """
        return self._rating

    def customer(self):
        """Return the customer who made this review.

        Returns:
            Customer: The customer who made the review.
        """
        return self._customer

    def restaurant(self):
        """Return the restaurant being reviewed by this review.

        Returns:
            Restaurant: The restaurant being reviewed.
        """
        return self._restaurant

    @classmethod
    def all(cls):
        """Return a list of all reviews.

        Returns:
            list: A list of all instances of the Review class.
        """
        return cls.all_reviews