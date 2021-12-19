### pytest-docker
-----------------------------
pytestでテスト時に、dockerでテスト環境を自動作成してくれる。
- 参考
    - https://github.com/avast/pytest-docker

### pytest-postgresql
-----------------------------
pytest時にpostgresqlに接続してくれる
- 参考
    - https://pypi.org/project/pytest-postgresql/
```
postgresql - これはクライアントフィクスチャで、機能的なスコープを持っています。各テストの後、残っているすべての接続を終了させ、再現性を確保するために PostgreSQL からテスト用データベースを削除します。このフィクスチャは、すでに接続されている psycopg 接続を返します。
postgresql_proc - セッションスコープのフィクスチャで、PostgreSQL インスタンスを最初に使用するときに起動し、テストの終了時に停止します。
postgresql_noproc - ノンプロセスフィクスチャで、すでに動作している postgresql インスタンスに接続します。例えば、Docker化されたテスト環境や、postgresqlのサービスを提供するCIなどです。
```