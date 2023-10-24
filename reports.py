#!/usr/bin/env python3

from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info, empty_line])



#today = date.today()
#title = today.strftime("%B %d, %Y")
#data = 'name:Apple'+"\n"+'weight:500 lbs'+"\n"+"\n"+'name:Avocado'+"\n"+'weight:200 lbs'+"\n"+"\n"+'name:Blackberry'+"\n"+'weight:150 lbs'+"\n"+"\n"+'name:Kiwifruit'+"\n"+'weight:250 lbs'+"\n"+"\n"+'name:Lemon'+"\n"+'weight:300 lbs'+"\n"+"\n"+'name:Plum'+"\n"+'weight:150 lbs'+"\n"+"\n"+'name:Strawberry'+"\n"+'weight:240 lbs'+"\n"+"\n"+'name:Watermelon'+"\n"+'weight:500 lbs'+"\n"


#generate('/home/karim/test.pdf',title)