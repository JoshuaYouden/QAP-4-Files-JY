# Author: Joshua Youden
# Date edited: March 23rd, 2024

while True:
    # Enter required liberaries
    import sys
    import time
    from datetime import datetime, timedelta

    # Enter constants here
    f = open('Values.dat', 'r')
    POLICY_NUM = int(f.readline())
    BASIC_PREM = float(f.readline())
    ADD_CAR_DISCOUNT = float(f.readline())
    LIABILITY_COST = float(f.readline())
    GLASS_COVER_COST = float(f.readline())
    LOAN_COVER_COST = float(f.readline())
    HST = float(f.readline())
    PROCESS_FEE = float(f.readline())
    f.close()

    f = open('Claims List.dat', 'r')
    CLAIM_NUM = (f.readline())
    INVOICE_DATE = f.readline()
    TOTAL_COST = (f.readline())

    f.close()

    # Begin program

    while True:
        # Enter inputs + input IF statements here
        print()
        while True:
            Cust_First = input(
                "Enter customer's first name (END to quit): ").title()
            if Cust_First.upper() == "END":
                pass
            else:
                break

        Cust_Last = input("Enter customer's last name: ").title()

        Address = input("Enter customer's address: ")

        City = input("Enter customer's city: ").title()

        Prov_List = set({"NL", "PEI", "NS", "NB", "QC", "ON",
                        "MB", "SK", "AB", "BC", "YT", "NT", "NU"})
        while True:
            Province = input("Enter customer's province: ")
            if Province not in Prov_List:
                print("Data Entry Error - Invalid Province.")
            else:
                break

        Postal_Code = input("Enter customer's postal code: ")

        Phone_Num = input("Enter customer's phone number (999-999-9999): ")

        Car_Insure_Num = int(input("Enter number of cars insured: "))

        Liable_Insure = input(
            "Does customer want extra liability (Y or N): ").upper()

        Glass_Cover = input(
            "Does customer want optional glass coverage (Y or N): ").upper()

        Car_Loan = input(
            "Does customer want optional loaner car (Y or N): ").upper()

        Down_Pay = 0
        while True:
            Month_Pay_Type = input(
                "Does customer want pay Full, Monthly, or Down Pay: ").title()
            if Month_Pay_Type == "Down Pay":
                Down_Pay = float(input("Enter the Down Payment Amount: "))
                break
            else:
                break

        # Enter Calculation IF Statements here
        if Liable_Insure == "N":
            Extra_Liability_Cost = 0
        else:
            break
        if Glass_Cover == "N":
            Glass_Cover_Cost = 0
        else:
            break
        if Car_Loan == "N":
            Car_Loan_Cost = 0
            break
        else:
            break

        # Enter calculations here
    Insure_Prem_First = BASIC_PREM
    Insure_Prem_Add = (BASIC_PREM * ADD_CAR_DISCOUNT) * Car_Insure_Num
    Insure_Prem = Insure_Prem_First + Insure_Prem_Add
    Extra_Liability_Cost = LIABILITY_COST * Car_Insure_Num
    Glass_Cover_Cost = GLASS_COVER_COST * Car_Insure_Num
    Car_Loan_Cost = LOAN_COVER_COST * Car_Insure_Num
    Total_Extra_Cost = Extra_Liability_Cost + Glass_Cover_Cost + Car_Loan_Cost
    Insure_Prem_Total = Insure_Prem + Total_Extra_Cost
    Tax_Rate = HST * Insure_Prem_Total
    Total_Cost = Insure_Prem_Total + Tax_Rate
    while True:
        if Month_Pay_Type == "Full":
            Month_Pay = Total_Cost + PROCESS_FEE
            break
        elif Month_Pay_Type == "Monthly":
            Month_Pay = (Total_Cost + PROCESS_FEE) / 8
            break
        elif Month_Pay_Type == "Down Pay":
            Month_Pay = (Total_Cost - Down_Pay + PROCESS_FEE) / 8
            break
    Invoice_Date = datetime.now()
    Invoice_Date_New = Invoice_Date.replace(day=1)
    First_Pay_Date_Cal = Invoice_Date_New + timedelta(days=32)
    First_Pay_Date = First_Pay_Date_Cal.replace(day=1)
    Claim_Num = 0
    Claim_Num += 1
    POLICY_NUM += 1

    # Enter print statements here
    print()
    print("____________________________________________________________")
    print("         1         2         3         4         5         6")
    print("123456789012345678901234567890123456789012345678901234567890")
    print("____________________________________________________________")
    print("                  One Stop Insurance Policy                  ")
    print("                       Policy #", POLICY_NUM)
    print("    ------------------              ------------------")
    print(" ------- Current Invoice Date: ",
          Invoice_Date.strftime('%Y-%m-%d'), " -------")
    print(" -------   First Payment Date: ",
          First_Pay_Date.strftime('%Y-%m-%d'), " -------")
    print("____________________________________________________________")
    print("            -------- Customer Info --------")
    print()
    print("                Full Name: ", Cust_First, Cust_Last)
    print("             Phone Number: ", Phone_Num)
    print("                  Address: ", Address)
    print("                     City: ", City, ",", Province, ",", Postal_Code)
    print()
    print("____________________________________________________________")
    print("            -------- Premium Details --------")
    print()
    print("           Number of Cars: ", " ---- ",
          Car_Insure_Num, " ----  $", Insure_Prem)
    print("          Extra Liability: ", " ---- ",
          Liable_Insure, " ----  $", Extra_Liability_Cost)
    print("           Glass Coverage: ", " ---- ",
          Glass_Cover, " ----  $", Glass_Cover_Cost)
    print("               Loaner Car: ", " ---- ",
          Car_Loan, " ----  $", Car_Loan_Cost)
    print("____________________________________________________________")
    print()
    print("            Total Premium: $", Insure_Prem_Total)
    print("                      HST: $", round(Tax_Rate, 2))
    print("____________________________________________________________")
    print("               Total Cost: $", round(Total_Cost, 2))
    print("____________________________________________________________")
    print("            -------- Payment Details --------")
    print()
    print("             ------ Payment Method: ", Month_Pay_Type), "------"
    print("             ------   Down Payment:  $", Down_Pay), "------"
    print("             ------ Monthly Payment: $",
          round(Month_Pay, 2)), "------"
    print("____________________________________________________________")
    print("            -------- Claim(s) Details --------")
    print()
    print("          Claim #     Claim Date      Amount")
    print("------------------------------------------------------------")
    print("               ", "1", ", ", "2020-02-25", ", $1360.25")
    print("               ", "2", ", ", "2021-05-15", ", $2342.75")
    print("               ", "3", ", ", "2023-11-16", ", $2834.00")
    print()
    print("      Thank you for choosing One Stop Insurance Company!    ")
    print("____________________________________________________________")
    print()

    Claim_Num = CLAIM_NUM
    Invoice_Date = INVOICE_DATE
    Total_Cost = TOTAL_COST

    # Put the values back into the dat file
    f = open('Values.dat', 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREM)))
    f.write("{}\n".format(str(ADD_CAR_DISCOUNT)))
    f.write("{}\n".format(str(LIABILITY_COST)))
    f.write("{}\n".format(str(GLASS_COVER_COST)))
    f.write("{}\n".format(str(LOAN_COVER_COST)))
    f.write("{}\n".format(str(HST)))
    f.write("{}\n".format(str(PROCESS_FEE)))
    f.close()

    for _ in range(5):  # Change to control no. of 'blinks'
        print('Saving claim data ...', end='\r')
        time.sleep(.3)  # Used to create blinking effect
        # Clears entire line and the carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)

    f = open("Claims List.dat", "a")

    # All values written to file must be a string.  If you have a numeric
    # value, use the str() function to convert.
    f.write("{}\n".format(CLAIM_NUM))
    f.write("{}\n".format(INVOICE_DATE))
    f.write("{}\n".format(TOTAL_COST))

    f.close()

    # Now that is has written, display the message to indicate the data is saved.
    print()
    print("Claim data successfully saved ...", end='\r')
    time.sleep(1)  # To create the blinking effect
    # Clears the entire line and carriage returns
    sys.stdout.write('\033[2K\r')

    # Use the following to continue the loop or break the loop
    while True:
        Continue_Prompt = input(
            "Do you want to process another amortization (Y or N): ").upper()
        if Continue_Prompt == "Y":
            break
        elif Continue_Prompt == "N":
            break
        else:
            print("Data Entry Error - Prompt must be Y or N")

    # End program
