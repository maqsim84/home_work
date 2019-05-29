from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

<head>
    <title>Python Flask Hello World App</title>
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="header">
            <h3 class="text-muted">Hello world</h3>
        </div>
        <div class="jumbotron">
            <h1>Образец задания для компании Megafon</h1>
            <p class="lead"></p>
        </div>

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
