import webbrowser

from fpdf import FPDF


class PDFReport:

    """
    This class is for generating the PDF file based on Amount to be paid by each flatmate
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay= round(flatmate1.pays(bill, flatmate2))
        flatmate2_pay= round(flatmate2.pays(bill, flatmate1))
        pdf = FPDF(orientation='P', unit = 'pt', format= 'A4')
        pdf.add_page()
        pdf.image(name='house.jpg', w=30,h=30)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0,h=80, txt='Flatmate Bill', border=1, align='C', ln=1)
        pdf.cell(w=100,h=40, txt='Period: ', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=str(flatmate1.name), border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1_pay), border=1, ln=1)


        pdf.cell(w=100, h=40, txt=str(flatmate2.name), border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate2_pay), border=1, ln=1)
        pdf.output(self.filename)

        webbrowser.open(self.filename)