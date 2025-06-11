import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Load data and marks from JSON file
with open("question.json", "r") as file:
    content = json.load(file)

data = content["data"]

import random


totalMarks=int(input("enter total marks:"))
OneMarks=int(input("enter how many 1 marks:"))
TwoMarks=int(input("enter how many 2 marks:"))
ThreeMarks=int(input("enter how many 3 marks:"))
FiveMarks=int(input("enter how many 5 marks:"))
global crt
crt=1

if totalMarks!=OneMarks+TwoMarks*2+ThreeMarks*3+FiveMarks*5:
   print("invalid input")
else:
    print("---------------One Marks------------------")
    for i in random.sample(data["One"], OneMarks):
        print(crt, '. ',i)
        crt+=1
    crt=1
    print("----------------Two Marks------------")
    for i in random.sample(data["Two"], TwoMarks):
        print(crt, '. ',i)
        crt+=1
    crt=1
    print("-----------Three Marks---------------")
    for i in random.sample(data["Three"], ThreeMarks):
        print(crt, '. ',i)
        crt+=1
    crt=1
    print("-----------Five Marks--------------")
    for i in random.sample(data["Five"], FiveMarks):
        print(crt, '. ',i)
        crt+=1
    crt=1

    selected = {
    "1 Mark": random.sample(data["One"], OneMarks),
    "2 Marks": random.sample(data["Two"], TwoMarks),
    "3 Marks": random.sample(data["Three"], ThreeMarks),
    "5 Marks": random.sample(data["Five"], FiveMarks)
}

# Create PDF
pdf_file = "Question_Paper.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(width / 2, height - 50, "Computer Science - Question Paper")

c.setFont("Helvetica", 10)
c.drawRightString(width - 40, height - 70, f"Total Marks: {totalMarks}")

y = height - 100
question_no = 1

for section, questions in selected.items():
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Section - {section}")
    y -= 20

    c.setFont("Helvetica", 10)
    for q in questions:
        if y < 100:  # Start new page if needed
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 10)
        c.drawString(60, y, f"{question_no}. {q}")
        question_no += 1
        y -= 20

c.save()
print(f"PDF generated successfully: {pdf_file}")
