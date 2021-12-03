import os
from flask import Flask
from flask import send_from_directory, send_file


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'


@app.route('/download/<filename>', methods=['GET'])
def download(filename: str):
    app_path = app.root_path
    uploads_path = app.config['UPLOAD_FOLDER']
    full_path = os.path.join(app_path, uploads_path, filename)
    return send_file(full_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
