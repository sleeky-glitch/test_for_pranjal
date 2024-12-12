import streamlit as st
import fitz  # PyMuPDF
import tempfile

def main():
    st.title("PDF Viewer App")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Create a temporary file to save the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        try:
            # Open the PDF file
            pdf_document = fitz.open(tmp_file_path)
            
            # Display total pages
            st.write(f"Total Pages: {len(pdf_document)}")
            
            # Add a page selector
            page_number = st.number_input(
                "Select page number",
                min_value=1,
                max_value=len(pdf_document),
                value=1
            )
            
            # Display selected page
            page = pdf_document[page_number - 1]
            
            # Get page as an image
            pix = page.get_pixmap()
            
            # Convert to bytes
            img_bytes = pix.tobytes()
            
            # Display the page
            st.image(img_bytes, caption=f"Page {page_number}", use_column_width=True)
            
            # Close the PDF
            pdf_document.close()
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
