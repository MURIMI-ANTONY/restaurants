from review import Review
from restaurant import Restaurant
class Customer:
    all_instances = []
    def __init__(self,name,family_name) -> None:
        self.name=name
        self.family_name_value = family_name
        Customer.all_instances.append(self)

    def given_name(self):
        return self.name
    

    def family_name(self):
        return self.family_name_value
    
    def full_name(self):
        return f"{self.name} {self.family_name_value}"
    
    @classmethod
    def all(cls):
        return cls.all_instances
    
    def restaurants(self):
       return list({review.restaurant for review in self.reviews}) 

    def add_review(self, restaurant, rating):
        
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
    
    def num_reviews(self):
        return len(self._reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_instances:
            if customer.full_name().lower() == name.lower():
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_instances:
            if customer.given_name().lower() == name.lower():
                matching_customers.append(customer)
        return matching_customers

customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

restaurant1 = Restaurant("Tasty Treats")
restaurant2 = Restaurant("Burger Palace")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

# Example usage of the methods
print(customer1.full_name())  # Output: John Doe
print(restaurant2.average_star_rating())  # Output: 5.0
print(customer2.num_reviews())  # Output: 1




