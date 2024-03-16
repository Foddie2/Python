class TimeManagementApp:
    def __init__(self):
        self.time_allocation = {
            "new_entrants_threat": 0,
            "substitute_products_threat": 0,
            "supplier_power": 0,
            "buyer_power": 0,
            "competitive_rivalry": 0
        }

    def analyze_time_allocation(self):
        print("Time Allocation Analysis:")
        for force, time_spent in self.time_allocation.items():
            print(f"{force.replace('_', ' ').title()}: {time_spent} hours")

    def evaluate_personal_time(self):
        print("\nEvaluate Personal Time Allocation:")
        for force in self.time_allocation:
            time_spent = int(input(f"How many hours do you spend on {force.replace('_', ' ')}? "))
            self.time_allocation[force] = time_spent
            
        def monitor_time_changes(self):
            print("\nMonitoring Time Changes:")
        while True:
            choice = input("Would you like to update time allocation? (yes/no): ").lower()
            if choice == 'yes':
                self.evaluate_personal_time()
                self.analyze_time_allocation()
            elif choice == 'no':
                print("Exiting monitoring mode.")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    def run(self):
        print("Welcome to the Time Management App!")
        self.evaluate_personal_time()
        self.analyze_time_allocation()
        self.monitor_time_changes()

if __name__ == "__main__":
    time_management_app = TimeManagementApp()
    time_management_app.run()