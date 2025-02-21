# S and E's Phonics and Letters Learning App

A fun, interactive web application for children to learn phonics and letter sounds. Features two modes:
1. Word Building - Build words by clicking letters
2. Letter Sounds - Learn individual letter sounds

## File Location

The deployment zip file `S_and_E_phonics_and_letters.zip` is located at:
```
/Users/joelstitt/CascadeProjects/webapp/S_and_E_phonics_and_letters.zip
```

To find it in Finder:
1. Open Finder
2. Go to your home folder (⌘ + Shift + H)
3. Navigate to `CascadeProjects/webapp`
4. Look for `S_and_E_phonics_and_letters.zip`

## Deployment Instructions (PythonAnywhere)

1. Create a free account at [PythonAnywhere](https://www.pythonanywhere.com)

2. Once logged in:
   - Click on "Web" tab
   - Click "Add a new web app"
   - Choose "Flask" as your framework
   - Select Python 3.9 or later

3. Set up your files:
   - Go to "Files" tab
   - Upload all files from this directory
   - Ensure the following structure:
     ```
     /home/yourusername/mysite/
     ├── app.py
     ├── wsgi.py
     ├── requirements.txt
     ├── static/
     │   └── audio/
     │       └── Sienna's files/
     └── templates/
         ├── index.html
         └── voice2.html
     ```

4. Install requirements:
   - Go to "Consoles" tab
   - Start a new Bash console
   - Run: `pip install -r requirements.txt`

5. Configure the web app:
   - Go back to "Web" tab
   - In "Code" section, set:
     - Source code: /home/yourusername/mysite
     - Working directory: /home/yourusername/mysite
     - WSGI configuration file: /home/yourusername/mysite/wsgi.py

6. Reload your web app

Your app should now be live at: yourusername.pythonanywhere.com

## Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Visit http://localhost:5000 in your browser
