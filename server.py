import base64
from io import BytesIO
from flask import Flask, jsonify, render_template, request
import pyautogui
from PIL import Image
from math import sqrt


COLORS = [
    (121, 231, 245, 0), (97, 126, 123, 0), (59, 222, 138, 0), (138, 122, 92, 0), (172, 194, 254, 0), (147, 53, 13, 0), (74, 198, 178, 0), (135, 216, 255, 0), (131, 206, 207, 0), (141, 171, 251, 0), (134, 0, 142, 0), (70, 202, 0, 0), (125, 231, 99, 0), (88, 115, 43, 0), (144, 212, 50, 0), (161, 83, 52 ,0), (152, 148, 0 ,0), (131, 84, 84, 0), (117, 74, 26, 0), (171, 174, 119, 0)
]
MATERIALS = [
    (1635, 170), (1700, 170), (1760, 170), (1825, 170), (1890, 170), (1635, 230), (1700, 230), (1760, 230), (1825, 230), (1890, 230), (1635, 290), (1700, 290), (1760, 290), (1825, 290), (1890, 290), (1635, 355), (1700, 355), (1760, 355), (1825, 355), (1890, 355)
]
pixel_to_pos = {}
for i, color in enumerate(COLORS):
    # color (rbga) at index i will point to position (x, y) at position i
    pixel_to_pos[color] = MATERIALS[i]

def color_picker(color:tuple):
    distances = []
    for i in range(len(COLORS) - 1):
        sum = 0
        for component in range(len(color) - 1):
            sum += (color[component] - COLORS[i][component])**2
        distances.append(sqrt(sum))
    # now that i have the distances i have to pick the index of the minimum element
    min_distance = min(distances)
    min_index = distances.index(min_distance)
    return COLORS[min_index]


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
    colors = []
    image = Image.open('image.png')
    pixels = image.load()
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
