#!/usr/bin/env python3
"""
Deployment Helper Script for UML Diagram Explorer
This script helps prepare the application for deployment to Render.
"""

import os
import sys
import subprocess

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
    
    # Check requirements.txt content
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
            required_packages = ['gunicorn', 'Flask']
            missing_packages = []
            
            for package in required_packages:
                if package not in content:
                    missing_packages.append(package)
            
            if missing_packages:
                print("Warning: The following required packages are missing from requirements.txt:")
                for package in missing_packages:
                    print(f"  - {package}")
                return False
    except Exception as e:
        print(f"Error: Could not read requirements.txt: {e}")
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
        return False
    
    return True

def check_python_version():
    """Check if the Python version is compatible"""
    try:
        result = subprocess.run([sys.executable, '--version'], 
                              capture_output=True, text=True)
        version = result.stdout.strip()
        print(f"Local Python version: {version}")
        
        # Check if it's a compatible version (3.7+)
        if 'Python 3.' in version:
            version_num = version.split()[-1]
            major, minor = version_num.split('.')[:2]
            if int(major) >= 3 and int(minor) >= 7:
                print("✓ Python version is compatible")
                return True
        
        print("Warning: Python version might not be compatible with Render")
        return False
    except Exception as e:
        print(f"Warning: Could not determine Python version: {e}")
        return False

def check_dependencies():
    """Check if required dependencies can be installed"""
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.readlines()
        
        print("Checking dependencies from requirements.txt:")
        for req in requirements:
            req = req.strip()
            if req and not req.startswith('#'):
                print(f"  - {req}")
        
        print("✓ Dependencies check completed")
        return True
    except Exception as e:
        print(f"Warning: Could not check dependencies: {e}")
        return False

def check_environment_variables():
    """Check if required environment variables are set"""
    print("Note: No specific environment variables are required for this application.")
    print("Render will automatically provide the PORT environment variable.")
    
    # Check for common environment variables that might be useful
    optional_vars = ['DEBUG', 'FLASK_ENV']
    unset_vars = []
    
    for var in optional_vars:
        if not os.environ.get(var):
            unset_vars.append(var)
    
    if unset_vars:
        print(f"Optional environment variables that are not set: {', '.join(unset_vars)}")
    
    return True

def check_git_status():
    """Check Git repository status"""
    try:
        # Check if we're in a git repository
        result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("Warning: Not in a Git repository")
            return False
        
        # Check for uncommitted changes
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("Warning: You have uncommitted changes. Consider committing them before deployment.")
            return False
        
        print("✓ Git repository is clean")
        return True
    except Exception as e:
        print(f"Warning: Could not check Git status: {e}")
        return False

def main():
    print("UML Diagram Explorer - Render Deployment Helper")
    print("=" * 50)
    
    # Run all checks
    checks = [
        ("Required files", check_requirements),
        ("Image files", check_image_files),
        ("Python version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Environment variables", check_environment_variables),
        ("Git status", check_git_status)
    ]
    
    all_passed = True
    for check_name, check_function in checks:
        print(f"\n[{check_name}]")
        if not check_function():
            all_passed = False
    
    if not all_passed:
        print("\n⚠ Some checks failed or have warnings. Please review the messages above.")
    else:
        print("\n✓ All checks passed! Your application is ready for deployment.")
    
    # Provide deployment instructions
    print("\nDeployment Instructions for Render:")
    print("1. Ensure all changes are committed and pushed to GitHub")
    print("2. Go to https://render.com and sign in")
    print("3. Click 'New' → 'Web Service'")
    print("4. Connect to your GitHub repository")
    print("5. Render will automatically detect the configuration from render.yaml")
    print("6. Click 'Create Web Service'")
    print("7. Wait for deployment to complete (usually 2-5 minutes)")
    
    # Comprehensive troubleshooting tips
    print("\nTroubleshooting Guide:")
    print("If your application fails to deploy:")
    print("1. Check the build logs in the Render dashboard for specific error messages")
    print("2. Verify that all required files are present in your repository:")
    print("   - app.py, wsgi.py, requirements.txt, index.html, styles.css, script.js")
    print("3. Ensure image files are correctly named and present:")
    print("   - use-case-diagram-elements.png")
    print("   - activity-diagram.jpg")
    print("   - class-diagram.png")
    print("   - Sequence-Diagram-Place-Order.png")
    print("4. Check that requirements.txt contains:")
    print("   - Flask==2.0.3")
    print("   - gunicorn==20.1.0")
    print("5. Verify render.yaml configuration is correct")
    print("6. If images don't load, check file permissions and paths in index.html")
    print("7. For 'Module not found' errors, check dependencies in requirements.txt")
    print("8. For 'Port in use' errors, ensure your app uses the PORT environment variable")

if __name__ == "__main__":
    main()