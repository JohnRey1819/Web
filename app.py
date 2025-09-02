# app.py
import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from pdf2docx import Converter

# Initialize the Flask app for production
app = Flask(__name__)

# Enable CORS to allow requests from your frontend's domain
CORS(app)

# Render provides an ephemeral filesystem; this directory will be used for temp files.
UPLOAD_FOLDER = '/tmp/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # A simple health check route to confirm the server is running
    return "Python Backend is running!"

@app.route('/convert-pdf-to-docx', methods=['POST'])
def convert_pdf_to_docx():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.lower().endswith('.pdf'):
        pdf_filename = file.filename
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
        file.save(pdf_path)

        docx_filename = os.path.splitext(pdf_filename)[0] + '.docx'
        docx_path = os.path.join(app.config['UPLOAD_FOLDER'], docx_filename)
        
        try:
            # Perform the conversion
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()

            # Send the converted file back for download
            return send_file(docx_path, as_attachment=True)

        except Exception as e:
            return jsonify({"error": f"Conversion failed: {str(e)}"}), 500
            
        finally:
            # Clean up the temporary files from the server
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
            if os.path.exists(docx_path):
                os.remove(docx_path)
    else:
        return jsonify({"error": "Invalid file type, please upload a PDF."}), 400

# The following is only for local testing, Render will use Gunicorn to run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
