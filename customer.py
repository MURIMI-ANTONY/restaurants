from review import Review

class Customer:
    all_instances = []

    def __init__(self, name, family_name):
        """Initialize a new customer object."""
        self.name = name
        self.family_name_value = family_name
        self.reviews = []
        Customer.all_instances.append(self)

    def full_name(self):
        """Return the full name of the customer."""
        return f"{self.name} {self.family_name_value}"

    def add_review(self, restaurant, rating):
        """Add a new review to the customer's list of reviews."""
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    def num_reviews(self):
        """Return the number of reviews the customer has written."""
        return len(self.reviews)

    @classmethod
    def all(cls):
        """Return a list of all customer instances."""
        return cls.all_instances

    def restaurants(self):
        """Return a list of all unique restaurants reviewed by the customer."""
        return list({review.restaurant() for review in self.reviews})

    @classmethod
    def find_by_name(cls, name):
        """Find a customer by their full name. Returns the first match found or None if no match is found."""
        for customer in cls.all_instances:
            if customer.full_name().lower() == name.lower():
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        """Find all customers with a given name. Returns a list of all matches found."""
        matching_customers = []
        for customer in cls.all_instances:
            if customer.name.lower() == name.lower():
                matching_customers.append(customer)
        return matching_customers