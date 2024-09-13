from modules.habit_tracker import HabitTracker
from modules.data_storage import DataStorage
from modules.statistics import Statistics
from modules.visualization import Visualization
from modules.reminder import Reminder



def main():
    habit_tracker = HabitTracker()
    data_storage = DataStorage()
    statistics = Statistics()
    visualization = Visualization()
    reminder = Reminder()

    while True:
        print("1. Add Habit")
        print("2. Log Progress")
        print("3. View Statistics")
        print("4. View Visualization")
        print("5. Set Reminder")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            habit_tracker.add_habit()
        elif choice == '2':
            habit_tracker.log_progress()
        elif choice == '3':
            statistics.show_statistics()
        elif choice == '4':
            visualization.show_visualization()
        elif choice == '5':
            reminder.set_reminder()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()