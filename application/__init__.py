# pip install pdf2docx
import os
from collections.abc import Iterable 
from pdf2docx import Converter
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    # Define the directories
    dir_source_pdfs = os.path.join(os.getcwd(), 'application', 'static')
    dir_output_docx = os.path.join(os.getcwd(), 'application', 'uploads')

    # Ensure the output directory exists
    if not os.path.exists(dir_output_docx):
        os.makedirs(dir_output_docx)

    file_to_download = None

    # Check if the source directory exists
    if os.path.exists(dir_source_pdfs):
        for file in os.listdir(dir_source_pdfs):
            if file.split('.')[-1].lower() in ('pdf'):  # Ensure case-insensitivity
                
                cv = Converter(os.path.join(dir_source_pdfs, file))
                pdf_filename = '{0}.docx'.format(file.split('.')[-2])
                cv.convert(os.path.join(dir_output_docx, pdf_filename))
                cv.close()
                
                # image = Image.open(os.path.join(dir_source_pdfs, file))
                # image_converted = image.convert('RGB')
                # image_converted.save(os.path.join(dir_output_docx, pdf_filename))

                # # Store the first file for download after conversion
                # file_to_download = os.path.join(dir_output_docx, pdf_filename)

        # # Send the first generated PDF file to the client
        # if file_to_download:
        #     return send_file(file_to_download, as_attachment=True)

    return "Done!"

if __name__ == "__main__":
    app.run(debug=True)
