Here’s a structured `README.md` file for your project:

```markdown
# OCR Techniques Comparison: Classical vs LLM

This project demonstrates the comparison between classical OCR techniques and the usage of an LLM (Language Learning Model) to extract text from images, specifically focusing on handwritten content like medical prescriptions.

## Project Structure

```
.
├── assets/                # Folder containing the image files used for OCR
│   └── receta_farmacia.png # Example prescription image
├── src/                   # Folder containing Python scripts for OCR and LLM tasks
│   ├── classical_ocr.py    # Script implementing classical OCR techniques (Tesseract & EasyOCR)
│   └── llm_ocr.py          # Script implementing OCR with an LLM model
├── requirements.txt        # Dependencies for the project
└── README.md               # Project overview and instructions
```

### Folders and Files

- **assets/**: Contains the image file `receta_farmacia.png` used for testing the OCR techniques.
- **src/**: Contains two Python scripts:
  - `classical_ocr.py`: Applies Tesseract and EasyOCR to extract text from the image.
  - `llm_ocr.py`: Encodes the image as base64 and sends it to an LLM (like GPT-4) for text extraction.
- **requirements.txt**: Lists all the Python libraries required to run the project.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iamgarcia/ocr-techniques.git
   cd ocr-techniques
   ```

2. **Install the required dependencies:**
   Make sure you have Python 3.8+ installed. Then, install the dependencies from the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys:**
   - For the LLM (OpenAI API), add your API key to the `llm_ocr.py` file:
     ```python
     api_key = 'your-api-key'
     ```

## Running the Project

1. **Classical OCR Techniques:**
   To run the classical OCR techniques using Tesseract and EasyOCR:
   ```bash
   python src/classical_ocr.py
   ```
   This script will output the extracted text from Tesseract and EasyOCR.

2. **LLM-based OCR:**
   To run the LLM-based OCR:
   ```bash
   python src/llm_ocr.py
   ```
   This script encodes the image in base64 and sends it to the LLM (GPT-4) for extraction. The result will be printed on the console.

## Example Output

**Classical OCR Results:**
```bash
Final OCR Results:
{'tesseract': 'Prescercie [En de madicamenta soma, doc por Un aro radar or envase):',
 'easyocr': 'Ahlcastilla Lcon ENFEKMEUAU CUMUN U ACC PRESCRIPCION...'}
```

**LLM OCR Results:**
```bash
Paracetamol 1 gr.
en base grande
```

## Conclusion

This project demonstrates the ease and effectiveness of using an LLM for complex OCR tasks such as extracting handwritten text, compared to classical OCR techniques which often struggle with unstructured or unclear inputs.

Feel free to contribute, raise issues, or share your thoughts!

## License

This project is licensed under the MIT License.
```

---

### Key Points:
- **Installation** and **Running the Project** sections give clear instructions on how to set up and run both classical OCR and LLM-based OCR.
- **Example Output** shows what users can expect when they run the scripts, making it more user-friendly.
- You may want to customize the GitHub URL and any relevant sections based on your preferences.

Let me know if you'd like any more adjustments!