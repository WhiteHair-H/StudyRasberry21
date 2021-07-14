from flask import Flask

app = Flask(__name__)

@app.route('/')  # controller
def index():
    return '''
            <!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <title>Node.js webpage</title>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
        </head>
        <body>
            <h1>Node.js 제목</h1> 
            <h3>부제목</h3>
            <p>Node.js를 배우고 있는 페이지입니다.</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)