class EventOperations:
    def __init__(self):
        self.events = [
            {"id": 1, "name": "Birthday Party", "date": "2024-12-01", "location": "New York"},
            {"id": 2, "name": "Conference", "date": "2024-12-05", "location": "Los Angeles"}
        ]

    def view_events(self):
        if not self.events:
            print("No events to display.")
        else:
            print("\nList of Events:")
            for event in self.events:
                print(f"ID: {event['id']}, Name: {event['name']}, Date: {event['date']}, Location: {event['location']}")

    def add_event(self):
        name = input("\nEnter Event Name: ")
        date = input("Enter Event Date (YYYY-MM-DD): ")
        location = input("Enter Event Location: ")
        new_id = len(self.events) + 1
        self.events.append({"id": new_id, "name": name, "date": date, "location": location})
        print(f"Event '{name}' added successfully!")

    def update_event(self):
        try:
            event_id = int(input("\nEnter Event ID to Update: "))
            event = next((e for e in self.events if e["id"] == event_id), None)
            if event:
                new_name = input("Enter New Event Name: ")
                new_date = input("Enter New Event Date (YYYY-MM-DD): ")
                new_location = input("Enter New Event Location: ")
                event["name"] = new_name
                event["date"] = new_date
                event["location"] = new_location
                print(f"Event {event_id} updated successfully!")
            else:
                print(f"Event with ID {event_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid event ID.")

    def delete_event(self):
        try:
            event_id = int(input("\nEnter Event ID to Delete: "))
            event = next((e for e in self.events if e["id"] == event_id), None)
            if event:
                self.events.remove(event)
                print(f"Event {event_id} deleted successfully!")
            else:
                print(f"Event with ID {event_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid event ID.")
