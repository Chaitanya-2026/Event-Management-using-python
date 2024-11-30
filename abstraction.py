from CRUD_Operations import EventOperations

class EventManager:
    def __init__(self):
        self.event_operations = EventOperations()

    def view_events(self):
        self.event_operations.view_events()

    def add_event(self):
        self.event_operations.add_event()

    def update_event(self):
        self.event_operations.update_event()

    def delete_event(self):
        self.event_operations.delete_event()
