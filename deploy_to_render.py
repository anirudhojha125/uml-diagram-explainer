#!/usr/bin/env python3
"""
Deployment Helper Script for UML Diagram Explorer
This script helps prepare the application for deployment to Render.
"""

import os
import sys

def check_requirements():
    """Check if all required files exist for Render deployment"""
    required_files = [
        'requirements.txt', 
        'wsgi.py', 
        'app.py',
        'index.html',
        'styles.css',
        'script.js'
    ]
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("Error: Missing required files for deployment:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    return True

def check_image_files():
    """Check if all required image files exist"""
    required_images = [
        'use-case-diagram-elements.png',
        'activity-diagram.jpg',
        'class-diagram.png',
        'Sequence-Diagram-Place-Order.png'
    ]
    missing_images = []
    
    for image in required_images:
        if not os.path.exists(image):
            missing_images.append(image)
    
    if missing_images:
        print("Warning: The following image files are missing:")
        for image in missing_images:
            print(f"  - {image}")
        print("The application will use fallback URLs for these images.")
    
    return True

def check_environment_variables():
    """Check if required environment variables are set"""
    print("Note: No specific environment variables are required for this application.")
    print("Render will automatically provide the PORT environment variable.")
    
    return True

def main():
    print("UML Diagram Explorer - Render Deployment Helper")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        print("Deployment check failed. Please fix the issues above.")
        sys.exit(1)
    
    # Check image files
    check_image_files()
    
    # Check environment variables
    check_environment_variables()
    
    # Provide deployment instructions
    print("\nDeployment Instructions for Render:")
    print("1. Fork this repository to your GitHub account")
    print("2. Create a new Web Service on Render")
    print("3. Connect it to your forked repository")
    print("4. Render will automatically use the configuration from render.yaml")
    print("5. The application will be deployed at a URL like:")
    print("   https://your-app-name.onrender.com")
    print("\nYour application should now be ready for deployment!")

if __name__ == "__main__":
    main()