import base64
from io import BytesIO
from flask import Flask, jsonify, render_template, request
import pyautogui
from PIL import Image

# def getMousePosition():
#     return pyautogui.position()
materials = []
pixel_to_pos = {}


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-canvas', methods=['POST'])
def upload_canvas():
    dataURL = request.json['dataURL']
    image_data = base64.b64decode(dataURL.split(',')[1])

    # Load the image
    with open('image.png', 'wb') as f:
        f.write(image_data)

    # Get the color of each pixel in the image
    image = Image.open('image.png')
    pixels = image.load()
    colors = []
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            color = pixels[x, y]
            colors.append(color)

    # Get the size of the image
    width, height = image.size
    
    # Create an image from the colors array
    new_image = Image.new("RGBA", (width, height))
    new_image.putdata(colors)

    # Save the image to a PNG file
    output_buffer = BytesIO()
    new_image.save(output_buffer, format='PNG')
    image_data = output_buffer.getvalue()

    return jsonify({'message': 'Image uploaded successfully!'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
