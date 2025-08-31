
# Example usage of the PDF to PNG converter

from pdf_to_png_converter import pdf_to_png

# Basic usage - extracts to same folder as PDF
#created_files = pdf_to_png("COB_TEST_PROF.pdf")

# Specify output folder
#created_files = pdf_to_png("COB_TEST_PROF.pdf", "./extracted_images")

# Specify output folder and higher DPI for better quality
created_files = pdf_to_png("COB_TEST_PROF.pdf", "./high_quality", dpi=300)

print(f"Created {len(created_files)} PNG files")
