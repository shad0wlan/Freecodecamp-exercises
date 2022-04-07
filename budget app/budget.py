class Category:
    def __init__(self, ledger):
        self.ledger = [ledger]
        self.balance = 0
        self.withdraws = 0
        self.category_name = self.ledger.pop(0)

    def __str__(self):
        first_line = self.category_name.center(30, "*")
        final_string = [first_line]
        for k in range(len(self.ledger)):
            get_string_length = 30 - len(self.ledger[k]["description"][:23]) - 7
            final_string.append('{}{}{:>7.2f}'.format(self.ledger[k]["description"][:23], " " * get_string_length,
                                                      self.ledger[k]["amount"]))
        total = f'Total: {self.get_balance()}'
        final_string.append(total)
        returned_print_string = "\n".join(final_string)

        return returned_print_string


    def deposit(self, amount, description=""):
        object_deposit = {
            "amount": amount,
            "description": description
        }
        self.ledger.append({"amount" : amount, "description" : description})
        self.balance += amount
        return object_deposit

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount" : -amount, "description" : description})
            self.withdraws += -amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance + self.withdraws

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category_name}')
            category.deposit(amount, f'Transfer from {self.category_name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        calculation_fund = self.balance - amount
        if amount > self.get_balance() or calculation_fund < 0:
            return False
        else:
            return True



def create_spend_chart(main_category):

    percentages = []
    category_withdraws = []
    category = []
    maximum_string_length = 0
    name_string = []
    percentages_string = []
    total_withdraws = 0

    for i in main_category:
        if maximum_string_length < len(i.category_name):
            maximum_string_length = len(i.category_name)
        total_withdraws += i.withdraws * -1
        category_withdraws.append(i.withdraws * -1)
        category.append(i.category_name)

    for i in range(len(category_withdraws)):
        percentages.append(round((category_withdraws[i] / total_withdraws) * 100))

    for i in range(100 , -1, -10):
        percentages_string.append("{:>3}{}".format(i,'| '))
        for j in range(len(percentages)):
            if percentages[j] >= i :
                percentages_string.append("o  ")
            else:
                percentages_string.append('{:3}'.format(" "))
        percentages_string.append("\n")

    for i in range(maximum_string_length):
        name_string.append('{:5}'.format(" "))
        for j in category:
            try:
                name_string.append('{:3}'.format(j[i]))
            except IndexError:
                name_string.append('{:3}'.format(" "))
        name_string.append("\n")

    name_string = "".join(name_string).rstrip()
    dashes_string = "{}{:10}".format(" " * 4,"-" * ((len(percentages) * 2) + 4))
    percentages_string = "".join(percentages_string)
    final_string = f'Percentage spent by category\n{percentages_string}{dashes_string}\n{name_string}  '
    return final_string






