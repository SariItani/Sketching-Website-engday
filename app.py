from flask import Flask, request, render_template
import requests
import base64
import socket

midjourney_api_url = 'https://api.midjourney.com/sketch'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # do something with the file
        # Encode the file as Base64
        encoded_file = base64.b64encode(file.read()).decode('utf-8')
        # Send the file to the midjourney API
        response = requests.post(midjourney_api_url, json={'image': encoded_file})
        # Extract the sketch image from the response
        sketch_image = response.json()['sketch']
        # Render the sketch image in the browser
        return f'<img src="data:image/png;base64,{sketch_image}">'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    ip_address = socket.gethostbyname(socket.gethostname())
    app.run(debug=True, host=ip_address, port=5000)
