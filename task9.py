print("================================")
print("    Currency Exchange Desk      ")
print("================================")

USD_Amount = float(input("Enter the amount in USD: "))
Exchange_Rate = float(input("Enter the exchange rate (USD to local currency): "))
Local_Currency_Amount = USD_Amount * Exchange_Rate
print("Amount in local currency:", Local_Currency_Amount)
