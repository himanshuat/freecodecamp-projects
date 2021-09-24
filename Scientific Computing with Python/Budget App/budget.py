class Category:

    def __init__(self, category):
        self.name = category
        self.balance = 0
        self.spent = 0
        self.ledger = []

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        
        self.balance -= amount
        self.spent += amount
        self.ledger.append({"amount": -(amount), "description": description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        left_stars = (30 - len(self.name)) // 2
        right_stars = 30 - len(self.name) - left_stars
        string = (left_stars * '*') + self.name + (right_stars * '*') + '\n'

        for line in self.ledger:
            string += f"{line['description'][:23]:23}{line['amount']:7.2f}\n"

        string += f'Total: {self.balance:.2f}'

        return string

def create_spend_chart(categories):
    string = 'Percentage spent by category\n'
    chart_rows = []
    length = len(categories)

    for i in range(0, 101, 10):
        row = [f'{i:3d}|']
        row += ['   ' for j in range (length)]
        chart_rows.append(row)

    total_spent = 0

    for category in categories:
        total_spent += category.spent

    for i in range(length):
        spent = (categories[i].spent / total_spent) * 100

        for j in range(len(chart_rows)):
            if j <= spent / 10:
                chart_rows[j][i + 1] = ' o '

    chart_rows.reverse()

    for row in chart_rows:
        string += row[0] + ''.join(row[1:]) + ' \n'

    string += '    ' + ('-' * len(''.join(row[1:]))) + '-'

    longest = max([len(category.name) for category in categories])

    category_names = []
    for category in categories:
        category_name = category.name + ' ' * (longest - len(category.name))
        category_names.append(category_name)

    for i in range(longest):
        string += '\n    '
        for j in range(length):
            string += f' {category_names[j][i]} '
        string += ' '

    return string
