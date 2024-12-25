import PyPDF2
from fpdf import FPDF


def pdf_to_text(file, save: bool = True, output: str = "output.txt"):
    try:
        # Open the PDF file
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        # Extract text from each page
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        if save:
            with open(output, "w") as f:
                f.write(text)
        return text
    except Exception as e:
        return str(e)
    
def text_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(0, text)
    pdf.output("output.pdf")
    text = pdf_to_text("output.pdf", save=False)
    return text