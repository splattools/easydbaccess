# easydbaccess
Python 3.12.8

pip install -r requirements.txt

以下のような環境変数が必要
```
USERNAME='ユーザ名'
PASSWORD='パスワード'
HOST='ホスト名(AWSでいえばRDSのDNS)'
DB_NAME='接続DB名'
DB_TYPE='mysql' # or 'postgresql'
```

flaskは5000番ポートで受け付けるようにしているので注意してください
