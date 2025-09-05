import os
from pdf_reader import PDFReader
from address_extractor import AddressExtractor
from spreadsheet_writer import SpreadsheetWriter

def main():
    # Initialize components
    pdf_reader = PDFReader()
    address_extractor = AddressExtractor()
    spreadsheet_writer = SpreadsheetWriter("output/extracted_addresses.xlsx")
    
    # Get list of PDF files in invoices directory
    invoice_dir = "invoices"
    if not os.path.exists(invoice_dir):
        print(f"Error: {invoice_dir} directory not found!")
        return
    
    pdf_files = [f for f in os.listdir(invoice_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in invoices directory!")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process...")
    
    # Process each PDF file
    for pdf_file in pdf_files:
        try:
            print(f"\nProcessing: {pdf_file}")
            
            # Get full path to PDF
            pdf_path = os.path.join(invoice_dir, pdf_file)
            
            # Extract text from PDF
            text = pdf_reader.extract_text(pdf_path)
            
            # Debug: Print the extracted text
            print("\nExtracted text from PDF:")
            print("-" * 50)
            print(text)
            print("-" * 50)
            
            # Extract address from text
            address = address_extractor.extract_address(text)
            
            if address:
                # Write to spreadsheet
                spreadsheet_writer.write_address(pdf_file, address)
                print(f"\nSuccessfully extracted address from {pdf_file}")
                print("\nExtracted address:")
                print("-" * 20)
                print(address)
                print("-" * 20)
            else:
                print(f"No address found in {pdf_file}")
                print("Debug: Looking for keywords:", address_extractor.start_keywords)
                
        except Exception as e:
            print(f"Error processing {pdf_file}: {str(e)}")
            continue
    
    print("\nProcessing complete! Check output/extracted_addresses.xlsx for results.")

if __name__ == "__main__":
    main()
