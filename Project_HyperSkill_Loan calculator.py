import argparse
import math

parser = argparse.ArgumentParser(description="Welcome to your loan calculator! =)")

parser.add_argument("--type",
choices=['diff', 'annuity'],
help="Ingrese 'diff' para cálculo de los pagos diferenciados \ 'annuity' calcular el pago de la anualidad ")

parser.add_argument("--principal",
help="You have to enter your loan principal:")

parser.add_argument("--payment",
help="Enter the monthly or annual payment")

parser.add_argument("--periods",
help="Enter the periods in which you will make the payment.")

parser.add_argument("--interest",
help="Enter interest.")

args = parser.parse_args()

Parametros = 0
if args.type:
  Parametros += 1
if args.principal:
  P = int(args.principal)
  Parametros += 1
if args.payment:
  pp = int(args.payment)
  Parametros += 1
if args.periods:
  n = int(args.periods)
  Parametros += 1
if args.interest:
  i = float(args.interest) / (12 * 100)
  Parametros += 1

if args.type == 'diff' and args.payment:
  print("Incorrect parameters.")
elif args.type == 'diff':
  overpayment = P
  for o in range(1, n + 1):
    dm = math.ceil(P / n + i * (P - P * (o - 1) / n))
    print("Month {}: payment is {}".format(o, math.floor(dm)))
    overpayment -= dm
  print("\nOverpayment = {}".format(abs(overpayment)))
elif args.type == 'annuity' and args.payment and args.principal and Parametros == 4:
  # Operaciones:
  operation = pp / (pp - i * P)
  number_of_months = math.log(operation, 1 + i)
  convert_to = math.ceil(number_of_months)
  convert_to_years = math.floor(convert_to / 12)
  convert_to_months = number_of_months % 12
  overpayment = P
  for o in range(29):
    over = P / 29 + i * (P - P * (o - 1) / 29)
    overpayment -= over
  
  # Imprimir:
  if convert_to_years == 0:
    if convert_to_months == 0:
      print("You've repay the loan!")
    if convert_to_months == 1:
      print("It will take {} month to repay this loan!".format(round(convert_to_months)))
      print("Overpayment = {}".format(round(abs(overpayment))))
    if convert_to_months > 1:
      print("It will take {} months to repay this loan!".format(round(convert_to_months)))
      print("Overpayment = {}".format(round(abs(overpayment))))
  elif convert_to_years == 1:
    if convert_to_months == 0:
      print("It will take {} year to repay this loan!".format(round(convert_to_years)))
      print("Overpayment = {}".format(round(abs(overpayment))))
    elif convert_to_months == 1:
      print("It will take {} year and {} month to repay this loan!".format(round(convert_to_years), round(convert_to_months)))
      print("Overpayment = {}".format(round(abs(overpayment))))
    elif convert_to_months > 1:
      print("It will take {} year and {} months to repay this loan!".format(round(convert_to_years), round(convert_to_months)))
      print("Overpayment = {}".format(round(abs(overpayment))))
  elif convert_to_years != 1:
    if convert_to_months == 0:
      print("It will take {} years to repay this loan!".format(round(convert_to_years)))
      print("Overpayment = {}".format(round(abs(overpayment))))
    elif convert_to_months == 1:
      print("It will take {} years and {} month to repay this loan!".format(round(convert_to_years), round(convert_to_months)))
      print("Overpayment = {}".format(round(abs(overpayment))))
    elif convert_to_months > 1:
      print("It will take {} years and {} months to repay this loan!".format(round(convert_to_years), math.ceil(convert_to_months)))
      print("Overpayment = {}".format(round(abs(overpayment))))
      
elif args.type == 'annuity' and args.payment and Parametros == 4:
  # Calculos:
  loan_principal = pp // (i * (1 + i) ** n / ((1+i)**n - 1))
  overpayment = loan_principal
  for u in range(n):
    annuity_payment = loan_principal * (i * (1 + i)**n / ((1 + i) ** n - 1))
    overpayment -= annuity_payment
    
  floor = math.floor(overpayment)
  ceil = math.ceil(floor)
  
  # Imprimir:
  print("Your loan principal = {}!\nOverpayment = {}".format(round(loan_principal), abs(ceil)))
  
elif args.type == 'annuity' and args.principal and Parametros == 4:
  # Calculos:
  overpayment = P
  for m in range(n):
    annuity_payment = math.ceil(P * (i * (1 + i)**n / ((1 + i) ** n - 1)))
    overpayment -= annuity_payment
    
  # Imprimir:
  print("Your annuity payment = {}!\nOverpayment = {}".format(annuity_payment, abs(overpayment)))
elif Parametros < 4:
  print("Incorrect parameters.")