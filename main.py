import time

def simulate_delivery_interaction():
    """
    Simulates a delivery professional's interaction with a customer
    and its impact on customer satisfaction.
    """
    customer_satisfaction = 50 # Starting neutral satisfaction score (out of 100)

    print("--- Delivery Interaction Simulator ---")
    print("You are a delivery professional arriving at a customer's address.")
    print("The customer is not immediately available to receive the package.")
    print("\nHow do you handle this situation?")
    print("1. Leave a generic 'missed delivery' note and move on.")
    print("2. Attempt to contact the customer (call/message), and if unsuccessful, leave a personalized note with clear next steps.")
    print("3. Wait for 5 minutes, if no one appears, return the package to the depot without further contact.")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        print("\nYou chose: Leave a generic 'missed delivery' note.")
        print("The customer will find a standard note later.")
        customer_satisfaction -= 20 # Demonstrates impact of minimal effort/communication
        print("Customer satisfaction decreased.")
    elif choice == '2':
        print("\nYou chose: Attempt to contact the customer and leave a personalized note.")
        print("You try calling the customer. No answer. You leave a polite, personalized note explaining the situation and how to reschedule.")
        customer_satisfaction += 30 # Demonstrates impact of proactive communication and problem-solving
        print("Customer satisfaction significantly increased!")
    elif choice == '3':
        print("\nYou chose: Wait for 5 minutes, then return the package to the depot.")
        print("After waiting, no one appears. You mark the package for return to the depot.")
        customer_satisfaction -= 10 # Demonstrates impact of lack of communication, even with some effort
        print("Customer satisfaction decreased slightly due to lack of direct communication.")
    else:
        print("\nInvalid choice. Defaulting to minimal interaction.")
        customer_satisfaction -= 15

    print("\n--- Interaction Summary ---")
    print(f"Final Customer Satisfaction Score: {customer_satisfaction}/100")

    if customer_satisfaction >= 70:
        print("This interaction fostered trust and loyalty. Excellent customer relationship management!")
    elif customer_satisfaction >= 40:
        print("This interaction was acceptable, but there was room for improvement in building a stronger customer relationship.")
    else:
        print("This interaction likely damaged the customer relationship and brand perception. Opportunities for improvement are significant.")

    print("\nRemember: Every delivery interaction is an opportunity to build or break customer trust.")

if __name__ == "__main__":
    simulate_delivery_interaction()
