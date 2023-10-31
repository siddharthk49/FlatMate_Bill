from Flat import Bill, Flatmate
from Reports import PDFReport

bill_amount = input("Enter the Bill amount: ")
time_period = input("Enter the time period: ")
flatmate_1 = input("Enter the Name of first flatmate: ")
days_in_house_1 = input(f"Enter the number of days {flatmate_1} was in the house: ")
flatmate_2 = input("Enter the Name of other flatmate: ")
days_in_house_2 = input(f"Enter the number of days {flatmate_2} was in the house: ")



"""the_bill = Bill(120,"April 2023")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 30)
pdf = PDFReport(filename='PdfReport.pdf')
pdf.generate(flatmate1=john,flatmate2=mary,bill=the_bill)
"""
the_bill = Bill(bill_amount, time_period)
flatmate1 = Flatmate(flatmate_1, days_in_house_1)
flatmate2 = Flatmate(flatmate_1, days_in_house_2)
pdf = PDFReport(filename='PDF_Report.pdf')
pdf.generate(flatmate1,flatmate2,the_bill)


