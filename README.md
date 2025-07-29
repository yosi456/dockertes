# Docker練習 - 複数Webサーバ構成

このプロジェクトは、Dockerを使って複数のWebサーバを連携させる構成を学習するためのものです。

## 構成

- **Nginx**: リバースプロキシサーバ（ポート80）
- **Node.js**: Express サーバ（内部ポート3000）
- **Flask**: Python サーバ（内部ポート5000）

## プロジェクト構造

```
docker練習/test2/
├── docker-compose.yml     # Docker Compose設定
├── nginx/
│   └── nginx.conf        # Nginx設定ファイル
├── node-app/
│   ├── Dockerfile        # Node.js用Dockerfile
│   ├── package.json      # Node.js依存関係
│   └── app.js           # Node.jsアプリケーション
└── flask-app/
    ├── Dockerfile        # Flask用Dockerfile
    ├── requirements.txt  # Python依存関係
    └── app.py           # Flaskアプリケーション
```

## 使用方法

### 1. Docker Composeでコンテナを起動

```bash
docker-compose up -d
```

### 2. アプリケーションにアクセス

- **メインページ**: http://localhost/
- **Node.jsアプリ**: http://localhost/node
- **Flaskアプリ**: http://localhost/flask

### 3. APIエンドポイント

- **Node.js API**: http://localhost/node/api/status
- **Flask API**: http://localhost/flask/api/status

### 4. コンテナの停止

```bash
docker-compose down
```

## 学習ポイント

1. **Docker Compose**: 複数のコンテナを一括管理
2. **リバースプロキシ**: Nginxによる複数サービスへの振り分け
3. **ネットワーク**: コンテナ間通信
4. **マルチステージビルド**: 軽量なプロダクションイメージ

## トラブルシューティング

### ログの確認
```bash
docker-compose logs [service-name]
```

### コンテナの状態確認
```bash
docker-compose ps
```

### 個別コンテナの再起動
```bash
docker-compose restart [service-name]
```"# dockertes" 
