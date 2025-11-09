# UML Diagram Explorer

An interactive, attractive website to explain UML diagrams including Use Case, Activity, Class, and Sequence diagrams.

## Features

- Modern, responsive design
- Interactive diagram exploration
- Detailed explanations of each diagram type
- Visual examples
- Smooth animations and transitions
- Mobile-friendly layout
- Dark mode support
- Persistent theme preference

## Diagrams Covered

1. **Use Case Diagrams** - Illustrate the functionality of a system from a user's perspective
2. **Activity Diagrams** - Represent workflows and business processes
3. **Class Diagrams** - Show the structure of a system by displaying classes and relationships
4. **Sequence Diagrams** - Depict interactions between objects in a sequential order

## Technologies Used

- HTML5
- CSS3 (with animations, gradients, and dark mode support)
- JavaScript (with DOM manipulation, event handling, and localStorage)
- Flask (Python web framework for deployment)
- Gunicorn (WSGI server for production deployment)
- Responsive design principles
- Font Awesome icons

## How to Run Locally

1. Clone or download this repository
2. Navigate to the project directory
3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python app.py
   ```
6. Open your browser and go to `http://localhost:5000`
7. Toggle dark mode using the moon/sun icon in the navigation bar

## Deployment to Render (Production)

### Automated Deployment (Recommended)

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect it to your forked repository
4. Render will automatically detect the configuration from `render.yaml`
5. The application will be deployed at a URL like: `https://your-app-name.onrender.com`

### Manual Deployment Steps

1. Create a Render account at https://render.com
2. Connect your GitHub account to Render
3. Create a new Web Service
4. Connect to your repository
5. Configure the following settings:
   - Name: uml-diagram-explainer
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn wsgi:application`
6. Click "Create Web Service"

### Environment Variables

No environment variables are required for basic deployment. The application will automatically use the PORT environment variable provided by Render.

## Troubleshooting Deployment Issues

### Issue: Application not deploying properly

1. **Check the build logs** in Render dashboard for any error messages
2. **Verify all files are in the repository**:
   - Ensure `app.py`, `wsgi.py`, and `requirements.txt` exist
   - Check that all image files are present
3. **Check the start command**:
   - Should be `gunicorn wsgi:application`
4. **Verify dependencies**:
   - Check that `requirements.txt` includes `gunicorn` and `Flask`

### Issue: Images not loading

1. **Verify image file names match exactly**:
   - `use-case-diagram-elements.png`
   - `activity-diagram.jpg`
   - `class-diagram.png`
   - `Sequence-Diagram-Place-Order.png`
2. **Check file permissions** on the image files
3. **Verify images are included in the repository**:
   ```
   git ls-files | grep -E "\.(png|jpg)$"
   ```

### Issue: Application crashes on startup

1. **Check the application logs** in Render
2. **Verify Python version compatibility**:
   - The project uses Python 3.11 (specified in render.yaml)
3. **Check for missing dependencies** in `requirements.txt`

## Project Structure

```
uml-diagram-explainer/
├── index.html          # Main HTML file
├── styles.css          # Stylesheet with responsive design
├── script.js           # Interactive JavaScript functionality
├── app.py              # Flask application for deployment
├── wsgi.py             # WSGI entry point for Gunicorn
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment configuration
├── server.js           # Node.js server (optional)
├── package.json        # Project metadata and scripts
├── 404.html            # Custom 404 page
└── README.md           # This file
```

## Customization

You can easily customize this project by modifying:
- `index.html` - To change content or structure
- `styles.css` - To adjust colors, fonts, or layouts
- `script.js` - To modify interactions or add new features

## License

This project is open source and available under the MIT License.

## Author

UML Diagram Explorer - An educational project for software engineering students and professionals.