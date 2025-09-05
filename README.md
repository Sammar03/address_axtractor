# Invoice Address Extractor

A Python-based tool designed to streamline the process of extracting delivery addresses from PDF invoices. This tool automatically identifies "Invoice To" sections, extracts complete addresses including postal codes, and exports them to a well-formatted Excel spreadsheet. Perfect for businesses handling multiple invoices and needing to compile address data efficiently.

## Directory Structure
```
invoice_address_extractor/
│  
├── main.py                # Entry point, orchestrates the workflow
├── pdf_reader.py          # Handles PDF text extraction
├── address_extractor.py   # Processes and extracts addresses
├── spreadsheet_writer.py  # Manages Excel output
│  
├── invoices/             # Place your PDF invoices here
│     └── *.pdf          # PDF invoice files
│  
└── output/              # Generated output
      └── extracted_addresses.xlsx
```

## Getting Started

### Prerequisites
- Python 3.x
- Virtual Environment (recommended)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/invoice-address-extractor.git
cd invoice-address-extractor
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

### Usage

1. Place your PDF invoices in the `invoices/` directory
2. Run the program:
```bash
python main.py
```
3. Find extracted addresses in `output/extracted_addresses.xlsx`

## Features
- Batch processes multiple PDF invoices
- Maintains original address formatting
- Automatically formats Excel output for readability
- Modular design for easy extension
- Handles various invoice formats (must contain "Invoice To" section)

## Contributing

This project is open for collaboration! Here are some ways you can contribute:

- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📚 Improve documentation

### Future Enhancement Ideas
- OCR support for scanned invoices
- Additional field extraction (phone, email, etc.)
- Support for different invoice formats
- GUI interface
- Database integration

## License
This project is open source and available under the MIT License.

## Contact
If you have any questions or suggestions, feel free to open an issue or submit a pull request.
