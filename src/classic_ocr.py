import cv2
import pytesseract
from PIL import Image
import easyocr
import numpy as np

# Function to run Tesseract OCR
def ocr_with_tesseract(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale for better OCR accuracy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(gray)
    print("Tesseract OCR Output:")
    print(text)
    print("-" * 50)
    return text

# Function to run EasyOCR
def ocr_with_easyocr(image_path, languages=['en']):
    reader = easyocr.Reader(languages)
    results = reader.readtext(image_path)
    
    # Extract and print the text
    text = ' '.join([result[1] for result in results])
    print("EasyOCR Output:")
    print(text)
    print("-" * 50)
    return text

# Preprocessing function to improve OCR accuracy
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Optionally, you can try other preprocessing techniques here
    return thresh

def run_ocr_on_image(image_path):
    # Preprocess the image (for better OCR results)
    preprocessed_image = preprocess_image(image_path)
    
    # Save the preprocessed image for use
    processed_image_path = "preprocessed_image.png"
    cv2.imwrite(processed_image_path, preprocessed_image)
    
    # Run OCR techniques
    tesseract_result = ocr_with_tesseract(processed_image_path)
    easyocr_result = ocr_with_easyocr(image_path)
    
    # Combine results
    combined_result = {
        'tesseract': tesseract_result,
        'easyocr': easyocr_result
    }
    
    return combined_result

# Specify the image path
image_path = './assets/receta_farmacia.png'

# Run the OCR process
ocr_results = run_ocr_on_image(image_path)

# You can further process the results if needed
print("Final OCR Results:")
print(ocr_results)
