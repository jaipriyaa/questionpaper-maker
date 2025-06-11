
# 📝 Question Paper Generator

A Python-based tool to automatically generate question papers in **PDF format** from a structured JSON question bank.

## 📌 Features

- Reads questions from a categorized `questions.json` file
- Allows you to specify mark distribution (1M, 2M, 3M, 5M)
- Validates total marks
- Randomly selects questions for each category
- Outputs a professionally formatted **PDF question paper**

---

## 📂 Project Structure

```
├── questions.json         # Question bank (organized by marks)
├── main.py        # Main script to generate the PDF
└── README.md              # You're here!
```

---

## 📥 Prerequisites

Make sure you have **Python 3.x** installed.  
Install the required library:

```bash
pip install reportlab
```

---

## 🧠 Input Format (JSON)

Example `questions.json`:

```json
{
  "data": {
    "One": ["What is a variable?", "Define CPU", "..."],
    "Two": ["Differentiate RAM and ROM", "..."],
    "Three": ["Explain OOP concepts", "..."],
    "Five": ["Write a program for calculator", "..."]
  }
}
```

You must have enough questions in each category to match your mark distribution.

---

## ▶️ How to Use

Edit the mark distribution in `generate_pdf.py`:

```python
totalMarks = 20
OneMarks = 4
TwoMarks = 2
ThreeMarks = 2
FiveMarks = 2
```

Then run:

```bash
python generate_pdf.py
```

It will generate a file: `Question_Paper.pdf`

---

## 📄 Output Sample

```text
Computer Science - Question Paper
Total Marks: 20

Section - 1 Mark
1. What does CPU stand for?
2. Define software.

Section - 2 Marks
...

Section - 5 Marks
...
```

---

## 💡 Future Improvements

- GUI for easier mark entry
- CSV or Excel import
- Tags for topics (DBMS, OOP, etc.)
- Print version formatting (page breaks, logo, etc.)

---

## 🧑‍💻 Author

**Jaipriyaa**  
Open for collaboration ✨

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

