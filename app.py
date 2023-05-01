from flask import Flask, request, render_template
import subprocess
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['sketch']
    # Save the uploaded sketch as an image file
    img = Image.open(file.stream)
    img.save('input.png')
    # Call the NVIDIA Canvas app to generate the sketch
    subprocess.call(['path/to/nvidia-canvas', 'input.png', 'output.png'])
    # Load the generated sketch from the server and display it on the web page
    with open('output.png', 'rb') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
