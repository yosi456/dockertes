const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Node.js Server</title>
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
            <h1>🟢 Node.js サーバー</h1>
            <div class="info">
                <p><strong>サーバー:</strong> Node.js + Express</p>
                <p><strong>ポート:</strong> ${port}</p>
                <p><strong>時刻:</strong> ${new Date().toLocaleString('ja-JP')}</p>
                <p><strong>プロセスID:</strong> ${process.pid}</p>
            </div>
            <p>このページはNode.jsサーバーから配信されています。</p>
            <a href="/" class="back-link">メインページに戻る</a>
        </div>
    </body>
    </html>
  `);
});

app.get('/api/status', (req, res) => {
  res.json({
    server: 'Node.js',
    port: port,
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage()
  });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Node.js server running on port ${port}`);
});