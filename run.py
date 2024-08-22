import datetime

# Mock data for charging stations
stations = {
    "Station 1": {"location": "Tata Power - Croma MVR Complex Charging Station", "slots": 5, "type": "Bharat AC001"},
    "Station 2": {"location": "TML - Shiv Shankar Motors Charging Station", "slots": 3, "type": "CHAdeMO"},
    "Station 3": {"location": "IOCL - Simhadri Electric Vehicle Charging Station", "slots": 2, "type": "CCS-II"},
}

bookings = []

def find_stations():
    print("Available Charging Stations:")
    for station, details in stations.items():
        print(f"{station} - {details['location']} ({details['slots']} slots available)")

def find_station_by_partial_name(partial_name):
    for station, details in stations.items():
        if partial_name.lower() in details['location'].lower():
            return station, details
    return None, None

def book_slot():
    partial_name = input("Enter a part of the station name you want to book: ")
    station_name, station_details = find_station_by_partial_name(partial_name)
    
    if station_name:
        if station_details['slots'] > 0:
            time = input("Enter the time you want to book (HH:MM): ")
            booking_time = datetime.datetime.strptime(time, "%H:%M")
            bookings.append({"station": station_name, "time": booking_time})
            stations[station_name]['slots'] -= 1
            print(f"Slot booked at {station_details['location']} for {booking_time.time()}.")
        else:
            print("No slots available at this station.")
    else:
        print("Station not found.")

def main():
    find_stations()
    book_slot()

if __name__ == "__main__":
    main()
