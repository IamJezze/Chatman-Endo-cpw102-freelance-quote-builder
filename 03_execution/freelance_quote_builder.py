name = input("What's your name? ")

s = name
capitalized = s.title().strip()


Hours = input("Estimated work hours")

Hourly = input("Hourly rate")


Total = float(Hours) * float(Hourly)

Expenses = input("expenses?")
Total = Total + float(Expenses)
print("Project Estimate")
print("Client: "+capitalized)  # Output: "Alex Taylor"
print("Labor cost: $"+str(float(Hours)* float(Hourly)))
print("Direct expenses: $"+Expenses)
print("Total quote: $" + str(Total))