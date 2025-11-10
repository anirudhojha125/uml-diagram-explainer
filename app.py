from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # Handle all static files properly
    try:
        return send_from_directory('.', filename)
    except FileNotFoundError:
        # If file not found, check if it's a route that should be handled by the frontend
        if '.' not in filename:
            # Likely a frontend route, serve index.html
            return send_from_directory('.', 'index.html')
        return "File not found", 404

# Add a health check endpoint for Render
@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)