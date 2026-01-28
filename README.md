 🏦 Bank Account OOPS Project (Python)

This project demonstrates Object-Oriented Programming (OOP) concepts in Python using a simple banking system.
It covers inheritance, method overriding, custom exceptions, and inter-object communication through realistic banking operations.

📌 Features

Create bank accounts with an initial balance

Deposit and withdraw money

Transfer money between accounts

Custom exception handling for insufficient balance

Interest-based reward accounts

Savings accounts with withdrawal fees

Clear console output for every transaction

🧠 OOP Concepts Used

Classes & Objects

Inheritance

Method Overriding

Encapsulation

Custom Exceptions

super() usage

Code reusability

📁 Project Structure
├── bank_accounts.py     # Core banking classes and logic
├── oop_project.py       # Driver file (execution & testing)
└── README.md            # Project documentation

🏗️ Classes Explained
1️⃣ BankAccount

Base class representing a normal bank account.

Key Methods:

deposit(amount)

withdraw(amount)

transfer(amount, account)

getbalance()

viableTransaction(amount) → checks sufficient balance

Custom Exception:

BalanceException → raised when balance is insufficient

2️⃣ InterestRewardsAcct (Inherits BankAccount)

A reward account that gives 5% bonus on every deposit.

Deposit of ₹1000 → Balance increases by ₹1050


Overrides:

deposit()

3️⃣ SavingAcct (Inherits InterestRewardsAcct)

A savings account with:

5% deposit reward

₹5 withdrawal fee

Overrides:

withdraw()

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/bank-account-oop.git
cd bank-account-oop

2️⃣ Run the project
python oop_project.py

🧪 Sample Operations Demonstrated

Account creation (Ravi, Isha, Sara, Shasi)

Deposits and withdrawals

Transfers between accounts

Failed transactions due to insufficient balance

Interest and fee calculations

📌 Example Output (Snippet)
Account 'Ravi' created.
Balance = ₹5000.00

Deposit Completed
Account 'Isha' Balance = ₹8500.00

Withdraw interrupted: Sorry! account 'Ravi' only has a balance of ₹5000.00

🎯 Learning Objective

This project is ideal for:

Beginners learning Python OOP

Understanding real-world modeling using classes

Practicing exception handling

Preparing for interviews and mini-projects

🚀 Future Enhancements

Transaction history logging

User input–based menu system

File/database storage

Interest rate configuration

Unit testing

👩‍💻 Author

Tanvi Kumari
Python | OOP | Machine Learning Enthusiast
