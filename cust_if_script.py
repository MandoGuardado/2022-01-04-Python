#!/usr/bin/env python3

def federal_tax():
    string_income = input("Please enter you yearly income tax: ")
    int_income = int(string_income)
    federal_taxes = 0
    if int_income > 523600:
        print("$157,804.25 plus 37% of the excess over $523,600")
        difference = int_income - 523600
        federal_taxes = 157804.25 + (difference * 0.37)
    elif int_income > 209425:
        print("$47,843 plus 35% of the excess over $209,425")
        difference = int_income - 209425
        federal_taxes = 47843 + (difference * 0.35)
    elif int_income > 164925:
        print("$33,603 plus 32% of the the excess over $164,925")
        difference = int_income - 164925
        federal_taxes = 33603 + (difference * 0.32)
    elif int_income > 86375:
        print("$14,751 plus 24% of the excess over $86,375")
        difference = int_income - 86375
        federal_taxes = 14751 + (difference * 0.24)
    elif int_income > 40525:
        print("$4,664 plus 22% of the excess over $40,525")
        difference = int_income - 40525
        federal_taxes = 4664 + (difference * 0.22)
    elif int_income > 9950:
        print("$995 plus 12% of not over the excess over $9,950")
        difference = int_income - 9950
        federal_taxes = 995 + (difference * 0.12)
    else:
        print("10% of the taxable income")
        federal_taxes = int_income * 0.10

    print("Your total income: $" + string_income + ", Your Federal Tax responsibility is: $" + str(federal_taxes))


federal_tax()
