import os
from fpdf import FPDF

# Function to create a PDF file and add QR code image files
def create_pdf(path, output_filename, num_columns, num_rows):
    pdf = FPDF(format='A4')
    pdf.set_auto_page_break(auto=True, margin=0)

    # Define the size of an individual QR code on the page
    qr_code_width = 50  # In millimeters
    qr_code_height = 50  # In millimeters

    # Search for PNG files in the specified path
    qr_code_filenames = []
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            qr_code_filenames.append(os.path.join(path, filename))

    # Calculate the number of QR codes per page
    qr_codes_per_page = num_columns * num_rows

    # Add a page to the PDF for each QR code image
    for i in range(0, len(qr_code_filenames), qr_codes_per_page):
        pdf.add_page()
        page_filenames = qr_code_filenames[i:i+qr_codes_per_page]

        # Add QR codes in columns and rows on the page
        for row in range(num_rows):
            for col in range(num_columns):
                index = row * num_columns + col
                if index < len(page_filenames):
                    x = col * qr_code_width
                    y = row * qr_code_height
                    pdf.image(page_filenames[index], x=x, y=y, w=qr_code_width, h=qr_code_height)

    # Save the PDF file
    pdf.output(output_filename)

# Example call to the function to create the PDF file with multiple columns and rows of QR codes
path = "/home/ubuntu"
num_columns = 4
num_rows = 5
output_filename = "qr_codes.pdf"
create_pdf(path, output_filename, num_columns, num_rows)
