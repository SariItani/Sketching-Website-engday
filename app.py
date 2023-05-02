import base64
import io
from flask import Flask, request, render_template
import subprocess
from PIL import Image
# import positionGetter

def decode_img(msg):
    # msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):
            # msg.find(b"<!plain_txt_msg>")]
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    return img

app = Flask(__name__)

@app.route('/')
def index():
    # print(positionGetter.getPos())
    return render_template('index.html')

@app.route('/upload_canvas', methods=['POST'])
def upload():
    file_base64 : str = request.form['file'] 
    # Save the uploaded sketch as an image file
    img = decode_img(file_base64)
    print(img)
    print(type(img))
    img.save('input.png')
    # Call the NVIDIA Canvas app to generate the sketch
    subprocess.call(['cat', 'input.png'])
    # subprocess.call(['path/to/nvidia-canvas', 'input.png', 'output.png'])
    # Load the generated sketch from the server and display it on the web page
    with open('output.png', 'rb') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
