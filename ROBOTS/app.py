from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/robots.txt')
def robots_txt():
    return  render_template('robots.html')




@app.route('/admin')
def admin_page():
    return render_template('admin.html')


@app.route('/admin/login', methods=['POST'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
   
    if username.lower() == "johnray" and password.lower() == "johnray":
        
        return "<h1>Congratulations! You've completed the challenge!</h1><p>This is the third part of the flag : @771449}</p> <p>"
    
    else:
        
        return "<h1>Incorrect login. Please try again!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

