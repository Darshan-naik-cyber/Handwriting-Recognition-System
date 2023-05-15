import streamlit as st
from PIL import Image
import pytesseract



def main():
    st.title("Handwritten Text Recognition")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Extract text from the image using Tesseract
        extracted_text = pytesseract.image_to_string(image)

        # Display the extracted text
        st.header("Extracted Text")
        st.write(extracted_text)


if __name__ == "__main__":
    main()
