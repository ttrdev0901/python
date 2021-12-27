import os
import base64
import sys
from io import BytesIO

import flask
from flask import (
    Flask,
    send_from_directory,
    redirect,
    jsonify
)
from flask import request
from flask_api import status
from flasgger import Swagger

from logging import (
    getLogger, 
    StreamHandler, 
    DEBUG, INFO,
    Formatter
)


_logger = getLogger(__name__)
sh = StreamHandler()
fmt = Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
sh.setFormatter(fmt)
sh.setLevel(DEBUG)

app = Flask(__name__)
Swagger(app)

def _b64decode_helper(request_object:flask.Request):
    """Base64デコードしたデータと元のデータサイズを返す関数

    Parameters:
    ---------------
    request_object: 

    Returns:
    ---------------
    data: data
        デコードしたデータ
    size: int
        デコードしたデータサイズ
    """

    size = sys.getsizeof(request_object.data)
    decode_msg = f"Decoding data of size {size}"
    _logger.info(decode_msg)

    decoded_data = BytesIO(base64.b64decode(request.data))
    return decoded_data, size

@app.route("/")
def home():
    """/ API文書にリダイレクト: /apidocs
    """
    return redirect("/apidocs")

@app.route("favicon.ico")
def favicon():
    """Faviconの表示
    """
    return send_from_directory(
                    os.path.join(app.root_path, 'static'), 
                    'favicon.ico', 
                    mimetype='image/vnd.microsoft.icon'
                )

@app.route('/api/funcs', methods=['GET'])
def list_apply_funcs():
    """使用可能な関数のリストを返す関数

        GET /api/funcs
        ---
        responses:
            200:
                description: Returns list of appliable functions.


    """
    appliable_list = utils.appliable_functions()
    return jsonify({"funcs": appliable_list})

@app.route('/api/<groupbyop>', methods=['PUT'])
def csv_aggreagate_columns(groupbyop):
    """アップロードしたCSVの列を集約

    ---
        consumes: application/json
        parameters:
            -   in: path
                name: Appliable Function (i.e. npsum, npmedian)
                type: string
                required: True
                description: appliable function,
                 which must be registered (check /api/funcs)
            -   in: query
                name: column
                type: string
                description: The column to process in an aggregation
                required: True
            -   in: query
                name: group_by
                type: string
                description: The column to group_by in an aggregation
                required: True
            -   in: header
                name: Content-Type
                type: string
                description:
                    Requires "Content-Type:application/json" to be set
                required: True
            -   in: body
                name: payload
                type: string
                description: base64 encoded csv file
                required: True

resoponses:
    200:
                description: Returns an aggregated CSV.
    """
    # Content-Type: 
    # Getは存在しない: https://qiita.com/Sekky0905/items/dff3d0da059d6f5bfabf
    content_type = request.header.get('Content-Type')
    content_type_log_msg = f"Content-Type is set to: {content_type}"
    if not content_type == "application/json":
        wrong_method_log_msg = f"Wrong Content-Type in request: {content_type} sent, but requires application/json"
        _logger.info(wrong_method_log_msg)
        return jsonify({
                        "content_type": content_type,
                        "error_msg": wrong_method_log_msg,
                        }), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    
    # クエリパラメータをパースして値を取得
    query_string = request.query_string # バイト文字列
    query_string_msg = f"Request Query String: {query_string}"
    _logger.info(query_string)
    column = request.args.get("column")
    group_by = request.args.get("group_by")

    # クエリパラメータのログと処理
    query_parameters_log_msg = f"column: [{column}] and group_by: [{group_by}] Query Parameter values"
    _logger.info(query_parameters_log_msg)
    if not column or not group_by:
        error_msg = "Query Parameter column or group_by not set"
        _logger.info(error_msg)
        return jsonify({
                        "column": column, 
                        "group_by": group_by, 
                        "error_msg": error_msg
                    }), status.HTTP_400_BAD_REQUEST
    
    # プラグイン群を読み込み、使用可能なものを収集
    plugins = utils.plugins_map()
    appliable_func = plugins[group_by]

    # データをデコードして処理
    data, _ = _b64decode_helper(request)

    # Pandas.Seriesで返す
    res = csvops.group_by_operations(
                    data,
                    groupby_column_name=group_by,
                    apply_column_name=column,
                    func=appliable_func
                    )
    _logger.info(res)
    return res.to_json(), status.HTTP_200_OK

if __name__ == "__main__":
    _logger.info("Start Flask")
    app.debug = True
    app.run(host="0.0.0.0", port=5001)
    _logger.info("SHUTDOWN Flask")
        
