class Invoice:
    def __init__ (self, client_name, service, total, deposit):
        self.client_name = client_name
        self.service = service
        self.total = total
        self.deposit = deposit

    def calculate_balance(self):
        return self.total - self.deposit 

def get_text_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("please enter a valid text")
        elif user_input.isdigit():
            print("please enter text, not numbers")
        else:
            return user_input
        

def get_positive_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            print("Please enter an amount greater than £0")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_deposit(total):
    while True:
        try:
            deposit = float(input("Enter deposit paid (£):"))
            if 0 <= deposit <= total:
                return deposit
            print(f"Deposit must be between £0 and £{total:.2f}.")
        except ValueError:
            print ("Invalid input. Please enter a number.")

client_name = get_text_input("Enter client name: ")

while not client_name:
    print("Client name can not be empty")
    client_name = input("Enter client name: ").strip()
    
service = get_text_input("Enter the service provided: ")
while not service:
    print("Service cannot be empty")
    service = input("Enter service provided: ").strip()

total = get_positive_amount("Enter total invoice amount (£):" )
deposit = get_deposit(total)

invoice = Invoice(client_name, service, total, deposit)


print("\n====== SHOTBYUG INVOICE ======" )
print(f"Client: {invoice.client_name}")
print(f"Service: {invoice.service}")
print(f"Total: {invoice.total:.2f}")
print(f"Deposit: {invoice.deposit:.2f}")
print(f"Outstanding Balance: {invoice.calculate_balance():.2f}")