# DAY 21: 30 Days of python programming

#1
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1

        max_count = max(freq.values())
        mode = [k for k, v in freq.items() if v == max_count]

        return {'mode': mode[0], 'count': max_count}

    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return round(variance, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def percentile(self, p):
        sorted_data = sorted(self.data)
        k = (self.count() - 1) * (p / 100)
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return sorted_data[int(k)]
        d0 = sorted_data[int(f)] * (c - k)
        d1 = sorted_data[int(c)] * (k - f)
        return d0 + d1

    def freq_dist(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1

        total = self.count()
        freq_list = []

        for key, value in freq.items():
            percentage = (value / total) * 100
            freq_list.append((round(percentage, 1), key))

        # sort by frequency descending
        return sorted(freq_list, reverse=True)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27,
        24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24,
        33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())
print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Range:', data.range())
print('Mean:', data.mean())
print('Median:', data.median())
print('Mode:', data.mode())
print('Standard Deviation:', data.std())
print('Variance:', data.var())
print('Frequency Distribution:', data.freq_dist())

#2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}   # {amount: description}
        self.expenses = {}  # {amount: description}

    # Add income
    def add_income(self, amount, description):
        self.incomes[amount] = description

    # Add expense
    def add_expense(self, amount, description):
        self.expenses[amount] = description

    # Total income
    def total_income(self):
        return sum(self.incomes.keys())

    # Total expense
    def total_expense(self):
        return sum(self.expenses.keys())

    # Account balance
    def account_balance(self):
        return self.total_income() - self.total_expense()

    # Account info
    def account_info(self):
        return f"""
            Account Holder: {self.firstname} {self.lastname}
            Total Income: {self.total_income()}
            Total Expense: {self.total_expense()}
            Balance: {self.account_balance()}
        """

person = PersonAccount("Rohit", "Tiwari")
person.add_income(5000, "Salary")
person.add_income(2000, "Freelance")
person.add_expense(1500, "Rent")
person.add_expense(500, "Food")
print(person.account_info())