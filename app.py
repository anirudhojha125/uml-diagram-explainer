from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # Special handling for image files to ensure they're served correctly
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.css', '.js')):
        return send_from_directory('.', filename)
    # For other files, try to serve them or return 404
    try:
        return send_from_directory('.', filename)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)