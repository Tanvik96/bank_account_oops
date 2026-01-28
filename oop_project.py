from bank_accounts import*

Ravi = BankAccount(5000,"Ravi")
Isha = BankAccount(8000,"Isha")

Ravi.getbalance()
Isha.getbalance()

Isha.deposit(500)

Ravi.withdraw(8000)
Ravi.withdraw(1000)

Ravi.transfer(5000,Isha)
Ravi.transfer(3000,Isha)

Sara = InterestRewardsAcct(10000,"Sara")

Sara.getbalance()

Sara.deposit(1000)

Sara.transfer(9000,Ravi)


Shasi = SavingAcct(5000,"Shasi")

Shasi.getbalance()

Shasi.deposit(20000)

Shasi.transfer(100000,Sara)

Shasi.transfer(10000,Sara)

Ravi.getbalance()
Isha.getbalance()
Sara.getbalance()
Shasi.getbalance()