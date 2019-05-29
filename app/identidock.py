from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   name = Hello Word
   header = '<html><head><title>Hello World</title></head><body>'
   body = '''<form method="POST">
             Hello <input type="text" name="name" value="{}">
             <input type="submit" value="submit">
             </form>'''.format(name)
footer = '</body></html>'
return header + body + footer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
