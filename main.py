from customer import Customer
from restaurant import Restaurant
from review import Review

def main():
    # Instantiate some customers
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Alice", "Smith")

    # Instantiate some restaurants
    restaurant1 = Restaurant("Tasty Treats")
    restaurant2 = Restaurant("Burger Palace")

    # Customers write reviews for restaurants
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    # Example usage of the methods
    print(f"{customer1.full_name()} wrote {customer1.num_reviews()} reviews.")
    print(f"{restaurant1.name()} has an average rating of {restaurant1.average_star_rating()}.")
    print(f"{restaurant2.name()} has been reviewed by {len(restaurant2.customers())} customers.")

    # Display all reviews for a restaurant
    print(f"Reviews for {restaurant2.name()}:")
    for review in restaurant2.reviews():
        print(f" - {review.customer().full_name()}: {review.rating()} stars")

if __name__ == '__main__':
    main()