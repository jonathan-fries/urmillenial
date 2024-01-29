from flask import Flask, render_template, request, make_response
import pdfkit  # for generating PDFs

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submission
@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Get data from the form
    user_data_1 = request.form.get('user_data_1')
    user_data_2 = request.form.get('user_data_2')
    user_data_3 = request.form.get('user_data_3')
    user_data_4 = request.form.get('user_data_4')

    # Generate PDF using the user data (you'll need to implement this)
    # For PDF generation, you can use a library like pdfkit, we'll install it later

    # Return the PDF as a response to the user
    pdf = generate_pdf_from_data(user_data_1, user_data_2, user_data_3, user_data_4)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=generated.pdf'
    return response

def generate_pdf_from_data(user_data_1, user_data_2, user_data_3, user_data_4):
    # Define HTML content with user data
    html_content = f"""
    <html>
    <head>
        <title>Certified Millenial</title>
    </head>
        <body>
            <h1>Certified Millenial</h1>
            <p>This document hereby certifies that {user_data_1} is a millenial.</p>
            <p>The following reasons prove that this is the case:</p>
            <p>1. {user_data_2}</p>
            <p>2. {user_data_3}</p>
            <p>3. {user_data_4}</p>
        </body>
    </html>
    """

    # Path to wkhtmltopdf executable (you need to install wkhtmltopdf separately)
    wkhtmltopdf_path = '/path/to/wkhtmltopdf'  # Replace with the actual path

    # Configure PDF options
    pdf_options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
    }

    # Generate PDF using pdfkit
    # pdfkit.from_string(html_content, 'generated.pdf', options=pdf_options, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))
    pdfkit.from_string(html_content, 'millenial_cert.pdf', options=pdf_options)

    # Read the generated PDF file and return its content
    with open('generated.pdf', 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    return pdf_content

if __name__ == '__main__':
    app.run()