from abstraction import EventManager

def main():
    manager = EventManager()

    while True:
        print("\nEvent Management")
        print("1) View Events")
        print("2) Add Event")
        print("3) Update Event")
        print("4) Delete Event")
        print("5) Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            manager.view_events()
        elif choice == "2":
            manager.add_event()
        elif choice == "3":
            manager.update_event()
        elif choice == "4":
            manager.delete_event()
        elif choice == "5":
            print("Exiting Event Management system.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
