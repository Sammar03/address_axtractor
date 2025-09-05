import os
import pandas as pd

class SpreadsheetWriter:
    def __init__(self, output_path):
        """
        Initialize SpreadsheetWriter with output file path.
        
        Args:
            output_path (str): Path to the output Excel file
        """
        self.output_path = output_path
        self.columns = ["Invoice File", "Extracted Address"]

    def write_address(self, invoice_file, address):
        """
        Write or append address data to Excel file.
        
        Args:
            invoice_file (str): Name of the invoice file
            address (str): Extracted address
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            
            # Keep the address format as is (with line breaks)
            # Prepare new data
            new_data = pd.DataFrame({
                "Invoice File": [invoice_file],
                "Extracted Address": [address]
            })
            
            # If file exists, append to it
            if os.path.exists(self.output_path):
                existing_df = pd.read_excel(self.output_path)
                updated_df = pd.concat([existing_df, new_data], ignore_index=True)
            else:
                updated_df = new_data
            
            # Save to Excel with formatting
            with pd.ExcelWriter(self.output_path, engine='openpyxl') as writer:
                updated_df.to_excel(writer, index=False)
                
                # Get the worksheet
                worksheet = writer.sheets['Sheet1']
                
                # Set column width
                worksheet.column_dimensions['B'].width = 50
                
                # Enable text wrapping and adjust row height for all rows
                for row in worksheet.iter_rows():
                    for cell in row:
                        cell.alignment = cell.alignment.copy(wrap_text=True)
                    worksheet.row_dimensions[cell.row].height = 90
            
        except Exception as e:
            raise Exception(f"Error writing to spreadsheet: {str(e)}")
