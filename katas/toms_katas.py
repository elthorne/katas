# Value class. "Money", "Date", "EmailAddress", etc. Immutable
class EmailAddress:
    def __init__(self, address):
        self.address = address


# Entity class. Has an identity, i.e Customers have different names, address,
# contact numbers, etc. Mutable - details can change.
class Customer:
    def __init__(self, account_number, name, email_address):
        self.account_number = account_number
        self.name = name
        self.email_address = email_address

    def update_email_address(self, email_address):
        self.email_address = email_address


# Describes what it does. Mostly noun but sort of a verb.
class CustomerEmailer:
    def send_welcome_email(self):
        print("do the thing")

    def send_order_received_email(self):
        print("do the other thing")


# Command design pattern. The name of action
class CreateOrder:
    def __init__(self, customer_emailer, database):
        self.customer_emailer = customer_emailer
        self.database = database

    def execute(self):
        print(f"do this thing with {self.customer_emailer} and {self.database}")


# Represents an event. Name it an action in the past tense. Another value object
class CustomerCreatedOrder:
    def __init(self, customer_id):
        self.customer_id = customer_id

    def get_details(self):
        print(f"do that thing with {self.customer_id}")