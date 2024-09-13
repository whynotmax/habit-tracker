import matplotlib.pyplot as plt

class Visualization:
    
    def plot_habit_data(habit_data):
        """
        Plots the habit data using matplotlib.

        Parameters:
        habit_data (dict): A dictionary where keys are habit names and values are lists of completion data.
        """
        for habit, data in habit_data.items():
            plt.plot(data, label=habit)
        
        plt.xlabel('Time')
        plt.ylabel('Completion')
        plt.title('Habit Tracker Visualization')
        plt.legend()
        plt.show()