class AddressExtractor:
    def __init__(self):
        # Keywords to identify the start of address section
        self.start_keywords = ["Invoice To:", "Invoice To"]

        # Header fields to skip (usually appear before the address)
        self.header_fields = [
            "Invoice Date", "Due Date", "Invoice Number",
            "Purchase Order", "Sales Person"
        ]

        # Keywords that indicate we've gone past the address section
        self.end_keywords = [
            "Barcode", "Description", "Price", "Amount",
            "Phone:", "Email:", "VAT", "EORI"
        ]

    def extract_address(self, text):
        """
        Extract address from PDF text content.
        
        Args:
            text (str): Raw text extracted from PDF
            
        Returns:
            str: Extracted address or None if not found
        """
        try:
            # Split into lines and remove empty ones
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            # Find where the address section starts
            start_index = -1
            for i, line in enumerate(lines):
                if any(keyword in line for keyword in self.start_keywords):
                    start_index = i
                    break

            if start_index == -1:
                return None

            # Find the actual start of address (after header fields)
            current_index = start_index + 1
            while current_index < len(lines):
                line = lines[current_index]
                # Skip header fields
                if any(field in line for field in self.header_fields):
                    current_index += 1
                    continue
                # Found first line that looks like a name/address
                if any(c.isalpha() for c in line):
                    break
                current_index += 1

            if current_index >= len(lines):
                return None

            # Collect the address lines
            address_lines = []
            while current_index < len(lines):
                line = lines[current_index].strip()

                # Stop if we hit any end marker
                if any(keyword in line for keyword in self.end_keywords):
                    break

                # Skip phone numbers only
                if "Phone:" not in line:
                    # Only add lines that contain text
                    if any(c.isalpha() for c in line) or any(c.isdigit() for c in line):
                        address_lines.append(line)

                current_index += 1

            # Clean up and validate
            if not address_lines:
                return None

            # Join all lines into final address
            address = '\n'.join(address_lines)
            return address.strip()

        except Exception as e:
            raise Exception(f"Error extracting address: {str(e)}")
