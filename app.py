from flask import Flask , render_template , request , redirect , url_for
import os

app = Flask(__name__)  

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming.My first python project'
    return render_template('index.html', techs=techs, name = name, title = 'Home')
    

@app.route('/about')
def about():
    name = 'This is my first website , first project really, and im gonna make it big like big big HELLA FUCKING BIG'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post', methods= ['GET','POST'])

def post():
    name = 'Text Analyzer'
    
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
        
    if request.method == 'POST':
        content = request.form['content']
        words = len(content.split())
        
        return render_template('result.html', word_count=words, title="Results")
@app.route('/result')
def result():
    return render_template('result.html')
    

if __name__ == '__main__': 
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)