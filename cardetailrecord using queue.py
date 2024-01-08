import queue

class Vehicle:
    def __init__(self, plate_number, vehicle_type):
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type
        

def record_vehicle_details(vehicles_queue):
    plate_number = input("Enter the plate number of the vehicle: ")
    vehicle_type = input("Enter the type of vehicle (e.g., car, truck, bike): ")
    vehicle = Vehicle(plate_number, vehicle_type)
    vehicles_queue.put(vehicle)
    print(f"Vehicle with plate number {plate_number} ({vehicle_type}) added to the queue.")

def main():
    vehicles_queue = queue.Queue()
    
    while True:
        print("\nGate Control System")
        print("1. Record Vehicle Details")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            record_vehicle_details(vehicles_queue)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("\nVehicles in the queue:")
    while not vehicles_queue.empty():
        vehicle = vehicles_queue.get()
        print(f"Plate Number: {vehicle.plate_number}, Vehicle Type: {vehicle.vehicle_type}")

if __name__ == "__main__":
    main()
