import fitz  # PyMuPDF

class PDFReader:
    def __init__(self):
        pass

    def extract_text(self, pdf_path):
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
            
        Raises:
            Exception: If file is corrupted or unreadable
        """
        try:
            # Open the PDF file
            with fitz.open(pdf_path) as doc:
                # Initialize text variable
                text = ""
                
                # Extract text from each page
                for page in doc:
                    text += page.get_text()
                
                return text.strip()
                
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")
