class PiggyBank: 
    def __init__(self, owner): 
        self.owner = owner
        self.balance = 0
    def add_money(self, amount): 
        # 1. Add amount to balance
        self.balance += amount
        # 2. Print confirmation
        print(f"Added \({amount}. Balance:\){self.balance}")
    def spend_money(self, amount): 
        # 1. Check if balance >= amount 
        # 2. Subtract or show error
        if amount <= self.balance:
            self.balance -= amount
            print(f"Spent \({amount}. Remaining:\){self.balance}")
        else:
            print("Not enough money!")

#VERIFICATION & TEST CASES 

if __name__ == "__main__":
    # Test your code below: 
    bank = PiggyBank("Sarah") 
    bank.add_money(50)
    # Output: Added $50. Balance: $50 
    bank.spend_money(20) 
    # Output: Spent $20. Remaining: $30 
    bank.spend_money(40) 
    # Output: Not enough money!

    # Bonus: Independent instances check
    his_bank = PiggyBank("Alex")
    his_bank.add_money(100)
    print(f"{bank.owner}'s Balance: ${bank.balance}")       # Output: $10
    print(f"{his_bank.owner}'s Balance: ${his_bank.balance}") # Output: $100