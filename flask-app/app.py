from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Flask Server</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 40px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            h1 { color: #fff; }
            .info { 
                background: rgba(255,255,255,0.2); 
                padding: 15px; 
                margin: 15px 0; 
                border-radius: 8px; 
            }
            .back-link {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            .back-link:hover { background: #ff5252; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐍 Flask サーバー</h1>
            <div class="info">
                <p><strong>サーバー:</strong> Python Flask</p>
                <p><strong>ポート:</strong> 5000</p>
                <p><strong>時刻:</strong> ''' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '''</p>
                <p><strong>プロセスID:</strong> ''' + str(os.getpid()) + '''</p>
            </div>
            <p>このページはPython Flaskサーバーから配信されています。</p>
            <a href="/" class="back-link">メインページに戻る</a>
        </div>
    </body>
    </html>
    '''

@app.route('/api/status')
def api_status():
    return jsonify({
        'server': 'Flask',
        'port': 5000,
        'timestamp': datetime.datetime.now().isoformat(),
        'python_version': os.sys.version,
        'process_id': os.getpid()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)