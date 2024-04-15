import fitz  # PyMuPDF

def extract_sentences_from_pdf(pdf_path):
    sentences = []
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)

        # Iterate through each page
        for page_num in range(len(document)):
            page = document.load_page(page_num)

            # Extract text from the page
            text = page.get_text()

            # Remove newline characters from the text
            text = text.replace("\n", "")

            # Split text into sentences using full stop as delimiter
            sentences.extend(text.split(". "))

        # Close the PDF file
        document.close()
    except Exception as e:
        print(f"Error: {e}")

    return sentences

# Example usage
pdf_path = "../sample.pdf"
sentences = extract_sentences_from_pdf(pdf_path)
for sentence in sentences:
    print(sentence)
