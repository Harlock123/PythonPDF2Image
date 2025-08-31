
import fitz  # PyMuPDF
import os
import sys
from pathlib import Path

def pdf_to_png(pdf_path, output_folder=None, dpi=150):
    """
    Convert each page of a PDF to separate PNG files.

    Args:
        pdf_path (str): Path to the input PDF file
        output_folder (str): Output folder path (optional, defaults to same directory as PDF)
        dpi (int): Resolution for PNG output (default: 150)

    Returns:
        list: List of created PNG file paths
    """

    # Validate input file
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError("Input file must be a PDF")

    # Get original filename without extension
    pdf_file = Path(pdf_path)
    orig_filename = pdf_file.stem

    # Set output folder
    if output_folder is None:
        output_folder = pdf_file.parent
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

    # Open PDF
    pdf_document = fitz.open(pdf_path)
    created_files = []

    try:
        # Extract each page
        for page_num in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_num]

            # Create transformation matrix for desired DPI
            mat = fitz.Matrix(dpi/72, dpi/72)

            # Render page to pixmap
            pix = page.get_pixmap(matrix=mat)

            # Create output filename
            output_filename = f"{orig_filename}_PAGE_{page_num + 1}.png"
            output_path = output_folder / output_filename

            # Save as PNG
            pix.save(str(output_path))
            created_files.append(str(output_path))

            print(f"Created: {output_filename}")

    finally:
        pdf_document.close()

    return created_files

def main():
    """Main function to handle command line usage"""
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_png.py <pdf_file> [output_folder] [dpi]")
        print("Example: python pdf_to_png.py document.pdf ./output 200")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 150

    try:
        created_files = pdf_to_png(pdf_path, output_folder, dpi)
        print(f"\nSuccessfully converted {len(created_files)} pages to PNG files")
        print(f"Files saved to: {Path(created_files[0]).parent}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
