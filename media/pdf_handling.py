import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PageObject

def merge_pdfs_to_one_page():
    input_path = "input"
    if not os.path.exists(input_path):
        os.mkdir(input_path)
        print(f"Directory '{input_path}' does not exist. Automatically created. Please place your PDF files in it.")
        input("When finished, press any key to continue.")

    # Find all PDF files in the input directory
    pdf_files = [f for f in os.listdir(input_path) if f.endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the 'input' directory.")
        return

    used_files = set()
    writer = PdfWriter()

    while True:
        # List available PDF files excluding already used ones
        available_files = [f for f in pdf_files if f not in used_files]
        if not available_files:
            print("No more available PDF files to insert.")
            break

        print("\nAvailable PDF files:")
        for idx, file in enumerate(available_files, start=1):
            print(f"{idx}. {file}")

        try:
            choice = int(input("Select a PDF file to insert (0 to finish): "))
            if choice == 0:
                break
            selected_file = available_files[choice - 1]
        
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        # Mark the selected file as used
        used_files.add(selected_file)

        # Read the selected PDF and add its pages to the writer
        selected_path = os.path.join(input_path, selected_file)
        reader = PdfReader(selected_path)
        for page in reader.pages:
            # Create a new page with the same size as the current page
            new_page = PageObject.create_blank_page(width=page.mediabox.width, height=page.mediabox.height)
            new_page.merge_page(page)
            writer.add_page(new_page)

    # Save the merged PDF
    output_path = input("Enter the output file name (without extension): ")
    if not output_path:
        print("Output file name cannot be empty. Automatically using 'merged_output.pdf'.")
        output_path = "merged_output"
    if not output_path.endswith('.pdf'):
        output_path += '.pdf'
    if not os.path.exists('output'):
        os.mkdir('output')
        print("Directory 'output' did not exist and was created.")
    output_path = os.path.join('output', output_path)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Merged PDF saved as '{output_path}'")


if __name__ == "__main__":
    print("Welcome to pdf_tools by Rosalind!")
    
    while True:
        choice = input("Select an option:\n1. Merge PDFs to one page\nx. Exit\n")
        if choice.lower() == 'x':
            break
        if choice == '1':
            merge_pdfs_to_one_page()
        else:
            print("Invalid choice.")
            continue
