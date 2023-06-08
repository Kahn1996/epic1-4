class TravelPackage:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def calculate_total_cost(self):
        total_cost = 0
        for component in self.components:
            total_cost += component.price
        return total_cost


class Flight:
    def __init__(self, airline, price, departure, destination):
        self.airline = airline
        self.price = price
        self.departure = departure
        self.destination = destination


class Hotel:
    def __init__(self, name, price, location):
        self.name = name
        self.price = price
        self.location = location


class Activity:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration


class Agent:
    def __init__(self, name):
        self.name = name
        self.packages = []

    def add_package(self, package):
        self.packages.append(package)

    def remove_package(self, package):
        if package in self.packages:
            self.packages.remove(package)


class Notification:
    def __init__(self, agent):
        self.agent = agent

    def send_notification(self, message):
        print(f"Notification sent to {self.agent.name}: {message}")


class Report:
    def __init__(self, agent):
        self.agent = agent

    def generate_report(self):
        print(f"Generating report for {self.agent.name}...")
        total_packages = len(self.agent.packages)
        total_revenue = sum(package.calculate_total_cost() for package in self.agent.packages)
        print(f"Total packages: {total_packages}")
        print(f"Total revenue: {total_revenue}")


class Booking:
    def __init__(self, customer, package):
        self.customer = customer
        self.package = package

    def modify_booking(self, package):
        self.package = package
        print("Booking modified successfully!")


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.bookings = []

    def create_booking(self, package):
        booking = Booking(self, package)
        self.bookings.append(booking)
        return booking

    def modify_booking(self, booking, package):
        if booking not in self.bookings:
            print("No such booking found!")
        else:
            booking.modify_booking(package)

    def view_bookings(self):
        if len(self.bookings) == 0:
            print("No bookings available.")
        else:
            print("\nCustomer bookings:")
            for i, booking in enumerate(self.bookings, 1):
                print(f"{i}. {booking.package.name}")


class Payment:
    def __init__(self, booking, amount):
        self.booking = booking
        self.amount = amount

    def process_payment(self):
        print("Payment processed successfully!")


class CustomPackage:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def calculate_total_cost(self):
        total_cost = 0
        for component in self.components:
            total_cost += component.price
        return total_cost


def create_package():
    package_name = input("Enter package name: ")
    components = []

    while True:
        print("\nSelect a component to add to the package:")
        print("1. Flight")
        print("2. Hotel")
        print("3. Activity")
        print("4. Finish package creation")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            airline = input("Enter airline: ")
            price = float(input("Enter price: "))
            departure = input("Enter departure location: ")
            destination = input("Enter destination location: ")
            flight = Flight(airline, price, departure, destination)
            components.append(flight)
        elif choice == 2:
            name = input("Enter hotel name: ")
            price = float(input("Enter price: "))
            location = input("Enter hotel location: ")
            hotel = Hotel(name, price, location)
            components.append(hotel)
        elif choice == 3:
            name = input("Enter activity name: ")
            price = float(input("Enter price: "))
            duration = input("Enter activity duration: ")
            activity = Activity(name, price, duration)
            components.append(activity)
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")

    package = TravelPackage(package_name, components)
    return package


def create_custom_package():
    package_name = input("Enter package name: ")
    components = []

    while True:
        print("\nSelect a component to add to the package:")
        print("1. Flight")
        print("2. Hotel")
        print("3. Activity")
        print("4. Finish package creation")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            airline = input("Enter airline: ")
            price = float(input("Enter price: "))
            departure = input("Enter departure location: ")
            destination = input("Enter destination location: ")
            flight = Flight(airline, price, departure, destination)
            components.append(flight)
        elif choice == 2:
            name = input("Enter hotel name: ")
            price = float(input("Enter price: "))
            location = input("Enter hotel location: ")
            hotel = Hotel(name, price, location)
            components.append(hotel)
        elif choice == 3:
            name = input("Enter activity name: ")
            price = float(input("Enter price: "))
            duration = input("Enter activity duration: ")
            activity = Activity(name, price, duration)
            components.append(activity)
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")

    package = CustomPackage(package_name, components)
    return package


def main():
    agents = []
    customers = []
    custom_packages = []  # Added custom_packages list

    while True:
        print("\n===== Travel Booking System =====")
        print("1. Create a new travel package")
        print("2. View existing travel packages")
        print("3. Create an agent")
        print("4. Create a customer")
        print("5. Create a booking for a customer")
        print("6. Modify a booking for a customer")
        print("7. Generate a report for an agent")
        print("8. View bookings for a customer")
        print("9. Send a notification to an agent")
        print("10. Process a payment for a booking")
        print("11. Create a custom package")
        print("12. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            package = create_package()
            if len(agents) == 0:
                print("No agents available. Create an agent first.")
                continue
            agent_name = input("Enter agent name who will manage this package: ")
            agent = next((a for a in agents if a.name == agent_name), None)
            if agent is None:
                print("No such agent found. Please try again.")
                continue
            agent.add_package(package)
            print("Travel package created successfully!")
        elif choice == 2:
            if len(agents) == 0:
                print("No agents available. Create an agent first.")
                continue
            agent_name = input("Enter agent name to view their packages: ")
            agent = next((a for a in agents if a.name == agent_name), None)
            if agent is None:
                print("No such agent found. Please try again.")
                continue
            if len(agent.packages) == 0:
                print("No travel packages available.")
            else:
                print("\nAgent's travel packages:")
                for i, package in enumerate(agent.packages, 1):
                    print(f"{i}. {package.name} - Total cost: {package.calculate_total_cost()}")
        elif choice == 3:
            agent_name = input("Enter agent name: ")
            agent = Agent(agent_name)
            agents.append(agent)
            print("Agent created successfully!")
        elif choice == 4:
            customer_name = input("Enter customer name: ")
            customer_contact = input("Enter customer contact number: ")
            customer = Customer(customer_name, customer_contact)
            customers.append(customer)
            print("Customer created successfully!")
        elif choice == 5:
            if len(customers) == 0 or len(agents) == 0:
                print("No customers or agents available. Create a customer and an agent first.")
                continue
            customer_name = input("Enter customer name for the booking: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer is None:
                print("No such customer found. Please try again.")
                continue
            package_name = input("Enter package name for this booking: ")
            agent_name = input("Enter agent name who manages this package: ")
            agent = next((a for a in agents if a.name == agent_name), None)
            if agent is None:
                print("No such agent found. Please try again.")
                continue
            package = next((p for p in agent.packages if p.name == package_name), None)
            if package is None:
                print("No such package found. Please try again.")
                continue
            booking = customer.create_booking(package)
            print("Booking created successfully!")
        elif choice == 6:
            if len(customers) == 0 or len(agents) == 0:
                print("No customers or agents available. Create a customer and an agent first.")
                continue
            customer_name = input("Enter customer name for the booking: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer is None:
                print("No such customer found. Please try again.")
                continue
            booking_index = int(input("Enter booking index to modify: ")) - 1
            if booking_index not in range(len(customer.bookings)):
                print("Invalid booking index. Please try again.")
                continue
            booking = customer.bookings[booking_index]
            package_name = input("Enter new package name for this booking: ")
            agent_name = input("Enter agent name who manages this package: ")
            agent = next((a for a in agents if a.name == agent_name), None)
            if agent is None:
                print("No such agent found. Please try again.")
                continue
            package = next((p for p in agent.packages if p.name == package_name), None)
            if package is None:
                print("No such package found. Please try again.")
                continue
            customer.modify_booking(booking, package)
        elif choice == 7:
            if len(agents) == 0:
                print("No agents available. Create an agent first.")
                continue
            agent_name = input("Enter agent name to generate a report: ")
            agent = next((a for a in agents if a.name == agent_name), None)
            if agent is None:
                print("No such agent found. Please try again.")
                continue
            report = Report(agent)
            report.generate_report()
        elif choice == 8:
            if len(customers) == 0:
                print("No customers available. Create a customer first.")
                continue
            customer_name = input("Enter customer name to view their bookings: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer is None:
                print("No such customer found. Please try again.")
                continue
            customer.view_bookings()
        elif choice == 9:
            if len(agents) == 0:
                print("No agents available. Create an agent first.")
                continue
            agent_name = input("Enter agent name to send a notification: ")
            agent = next((a for a in agents if a.name == agent_name), None)
            if agent is None:
                print("No such agent found. Please try again.")
                continue
            message = input("Enter message: ")
            notification = Notification(agent)
            notification.send_notification(message)
        elif choice == 10:
            if len(customers) == 0:
                print("No customers available. Create a customer first.")
                continue
            customer_name = input("Enter customer name for the booking: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer is None:
                print("No such customer found. Please try again.")
                continue
            booking_index = int(input("Enter booking index to process payment: ")) - 1
            if booking_index not in range(len(customer.bookings)):
                print("Invalid booking index. Please try again.")
                continue
            booking = customer.bookings[booking_index]
            amount = float(input("Enter payment amount: "))
            payment = Payment(booking, amount)
            payment.process_payment()
        elif choice == 11:
            custom_package = create_custom_package()
            custom_packages.append(custom_package)
            print("Custom package created successfully!")
        elif choice == 12:
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
