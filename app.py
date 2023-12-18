Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template
>>> 
>>> app = Flask(__name__)
>>> 
>>> @app.route('/')
... def index():
...     return render_template('index.html')
... 
>>> if __name__ == '__main__':
...     app.run(debug=True)
... 
...     
 * Serving Flask app '__main__'
 * Debug mode: on
[31m[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.[0m
 * Running on http://127.0.0.1:5000
[33mPress CTRL+C to quit[0m
 * Restarting with stat
