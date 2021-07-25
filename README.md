参考: https://www.dataquest.io/blog/sql-intermediate/
元データ: https://data.world/dataquest/bank-and-credit-card-complaints

ローカルにデータを用意して、SQLを実行できるようにする。
元データは同じなので、dataworld上のクエリコンソールから実行することも可能。

実行SQLと実行結果をテキストで出力して、どちらもバージョン管理に入れることができる。

### 実行方法

`python query.py`

`make export` → 実行結果をファイルにエクスポートする。https://github.com/kijimaD/sqlpod/blob/master/test.org

### postgresの用意
db名とuser名は接続スクリプトでベタ書きされているので固定する必要がある。

```shell
$ sudo passwd postgres
$ su postgres
# psql

# role作成も必要そう
# userとdb作成
postgres=# createuser kijima
postgres=# createdb kijima

# 元のコンソールに戻って、ログインできる
$ psql -U kijima
```
### データの用意

https://data.world/dataquest/bank-and-credit-card-complaints からpostgresにCSVインポートする。
ほかのファイルは参考リンクを参照。

```shell
#=> \copy credit_card_complaints (date_received, product, sub_product, issue, sub_issue, consumer_complaint_narrative, company_public_response, company, state, zip_code, tags, consumer_consent_provided, submitted_via, date_sent, company_response_to_consumer, timely_response, consumer_disputed, complaint_id)
FROM './Downloads/Credit_Card_Complaints.csv'
WITH CSV HEADER;
```

CSVの日付形式が`07/20/2000`みたいなので、エラーが出た。変更する。
```sql
#=> SHOW datestyle; # 現在の値を確認する
#=> SET datestyle TO MDY;
```

### python環境の用意

```shell
pip install pandas sqlalchemy psycopg2 sqlparse
```

### pandaエラー

実行時、pandaで`UserWarning: Could not import the lzma module.`エラーが出たとき。devをインストールして、再度pyenvを作成し直す。

```shell
sudo apt-get install lzma liblzma-dev
pyenv install --list
pyenv install 3.5.4
pyenv global 3.5.4
python --version # 確認

pip install pandas sqlalchemy psycopg2
```
