# app/run.py

from app.views.cli.appointment_cli import list_appointments, create_appointment
from app.views.cli.user_cli import list_users, create_user

def main():
    print("Welcome to ThootTrack CLI!")

    while True:
        print("\nChoose an option:")
        print("1. List Appointments")
        print("2. Create Appointment")
        print("3. List Users")
        print("4. Create User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_appointments()
        elif choice == '2':
            create_appointment()
        elif choice == '3':
            list_users()
        elif choice == '4':
            create_user()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
