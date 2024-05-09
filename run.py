# app/run.py

from app import create_app
from app.views.cli.appointment_cli import list_appointments, create_appointment, get_appointment, update_appointment
from app.views.cli.user_cli import list_users, create_user, get_user
from app.views.cli.patient_cli import list_patients, create_patient, get_patient
from app.services.reporting_service import ReportingService

def main():
    print("Welcome to ThootTrack CLI!")

    while True:
        print("\nChoose an option:")
        print("1. List Appointments")
        print("2. Get Appointment")
        print("3. Create Appointment")
        print("4. Update Appointment")
        print("5. List Users")
        print("6. Get User")
        print("7. Create User")
        print("8. List Patients")
        print("9. Get Patient")
        print("10. Create Patient")
        print("11. Generate Report")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_appointments()
        elif choice == '2':
            get_appointment()
        elif choice == '3':
            create_appointment()
        elif choice == '4':
            update_appointment()
        elif choice == '5':
            list_users()
        elif choice == '6':
            get_user()
        elif choice == '7':
            create_user()
        elif choice == '8':
            list_patients()
        elif choice == '9':
            get_patient()
        elif choice == '10':
            create_patient()
        elif choice == '11':
            print(ReportingService.generate_report())
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Create the Flask application
    app = create_app()

    # Run the CLI
    with app.app_context():
        main()