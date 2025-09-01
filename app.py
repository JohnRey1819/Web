# app.py
import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from pdf2docx import Converter

# Initialize the Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) to allow browser requests
# from your HTML file to this Python server.
CORS(app)

# Create a directory to temporarily store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/convert-pdf-to-docx', methods=['POST'])
def convert_pdf_to_docx():
    """
    API endpoint to handle PDF to DOCX conversion.
    Receives a PDF file, converts it, and returns the DOCX file.
    """
    # 1. Check if a file was sent in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # 2. Check if the filename is valid
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.lower().endswith('.pdf'):
        # 3. Save the uploaded PDF file temporarily
        pdf_filename = file.filename
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
        file.save(pdf_path)

        # 4. Define the output DOCX path
        docx_filename = os.path.splitext(pdf_filename)[0] + '.docx'
        docx_path = os.path.join(app.config['UPLOAD_FOLDER'], docx_filename)
        
        try:
            # 5. Perform the conversion using the pdf2docx library
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()

            # 6. Send the converted file back to the user for download
            return send_file(docx_path, as_attachment=True)

        except Exception as e:
            # Handle potential conversion errors
            return jsonify({"error": f"Conversion failed: {str(e)}"}), 500
            
        finally:
            # 7. Clean up the temporary files from the server
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
            if os.path.exists(docx_path):
                os.remove(docx_path)

    else:
        return jsonify({"error": "Invalid file type, please upload a PDF."}), 400

if __name__ == '__main__':
    # Run the app on localhost, port 5000
    app.run(debug=True, port=5000)
