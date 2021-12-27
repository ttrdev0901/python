# Boto3
------------------------------------------------
## リポジトリ
- https://github.com/noahgift/pragai-aws

## API
- s3.resource
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#object

## メモ
- create_bucket
    - リージョンが"us-east-1"ではない場合、LocationConstraintが必要。
        - デフォルトが"us-east-1"の為、それ以外は指定する必要がある。
        - 指定しない場合: IllegalLocationConstraintExceptionがスローされる。
    - 参考Qiita: https://qiita.com/eyuta/items/3f39536aae51cdf0d197
    - boto3リファレンス
        ```
        LocationConstraint (string) --
        Specifies the Region where the bucket will be created. If you don't specify a Region, the bucket is created in the US East (N. Virginia) Region (us-east-1).

        LocationConstraint (string) -- 。
        バケットを作成するリージョンを指定します。Region を指定しない場合、Bucket は US East (N. Virginia) Region (us-east-1) に作成されます。
        ```
- pytest: 組み込みフィクスチャ
    - tmpdir 
        - 1時ディレクトリを作成する

## シェバン行
- 解説 https://wa3.i-3-i.info/word14689.html