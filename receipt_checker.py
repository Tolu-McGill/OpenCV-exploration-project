import cv2
import pytesseract
import re
import os


tesseract_path = os.environ['TESSERACT_OCR_PATH']
def extract_amount(image_path):
    """Extracts the final amount from a receipt image.

    Args:
        image_path (str): Path to the receipt image.

    Returns:
        str: The extracted amount, or None if not found.
    """

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


    text = pytesseract.image_to_string(thresh) 


    amount_pattern = r"(\d{1,3}(,\d{3})*(\.\d+)?|\d+(\.\d+)?)"
    matches = re.findall(amount_pattern, text)

    if matches:
        amount = matches[-1][0]  # Extract the last match
        # Handle decimal separator:
        amount = amount.replace(",", ".")
        return amount
    else:
        return None

if __name__ == "__main__":
    image_path = r"C:\Users\dudeo\Downloads\receipt_sample.jpeg"  # Replace with your image path
    amount = extract_amount(image_path)

    if amount:
        print("Extracted amount:", amount)
    else:
        print("Amount not found.")