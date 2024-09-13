class Statistics:
    def calculate_average(data):
        """
        Calculate the average of a list of numbers.
        
        :param data: List of numbers
        :return: Average of the numbers
        """
        if not data:
            return 0
        return sum(data) / len(data)

    def calculate_median(data):
        """
        Calculate the median of a list of numbers.
        
        :param data: List of numbers
        :return: Median of the numbers
        """
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def calculate_mode(data):
        """
        Calculate the mode of a list of numbers.
        
        :param data: List of numbers
        :return: Mode of the numbers
        """
        if not data:
            return 0
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_count = max(frequency.values())
        modes = [num for num, count in frequency.items() if count == max_count]
        return modes if len(modes) > 1 else modes[0]
