from flask import Flask, request, jsonify
import os
from few import final

app = Flask(__name__)

# Set up a directory to save images
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload-image', methods=['POST'])
def upload_image():
    print(11)
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']
    if file.filename == '':
        print(11)
        return jsonify({'error': 'No image selected for uploading'}), 400

    if file:
        # Save the file to the uploads directory
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # You can process the image here and generate a response based on your requirements

        return jsonify({'data': final(filepath),'message': 'Image successfully uploaded', 'filename': file.filename}), 200

    else:
        return jsonify({'error': 'Allowed image types are -> png, jpg, jpeg, gif'}), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
