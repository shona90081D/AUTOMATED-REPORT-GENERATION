import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, "Student Marks Report", ln=True, align="C", fill=True)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def generate_report(data, output_path):
    marks = [int(row["Marks"]) for row in data]
    total = sum(marks)
    average = total / len(marks)

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Summary Section
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, f"Total Students: {len(marks)}", ln=True, fill=True)
    pdf.cell(0, 10, f"Total Marks: {total}", ln=True, fill=True)
    pdf.cell(0, 10, f"Average Marks: {average:.2f}", ln=True, fill=True)
    pdf.ln(10)

    # Table Header
    pdf.set_fill_color(180, 200, 255)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, "Name", border=1, fill=True)
    pdf.cell(60, 10, "Subject", border=1, fill=True)
    pdf.cell(40, 10, "Marks", border=1, ln=True, fill=True)

    # Table Data
    pdf.set_font("Arial", size=12)
    for row in data:
        pdf.cell(60, 10, row["Name"], border=1)
        pdf.cell(60, 10, row["Subject"], border=1)
        pdf.cell(40, 10, row["Marks"], border=1, ln=True)

    # Save PDF
    pdf.output(output_path)
    print(f"Creative PDF report generated: {output_path}")

# File paths
file_path = r"C:\code hut\BN's Intrnprjct\sample_data.csv"
output_path = r"C:\code hut\BN's Intrnprjct\report.pdf"

# Main execution
if __name__ == "__main__":
    data = read_data(file_path)
    generate_report(data, output_path)
