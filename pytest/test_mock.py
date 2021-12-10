import pandas as pd
import sqlite3
import psycopg2

def get_dataframe():
    return pd.read_csv('./sample.csv')

def get_record():
    # with psycopg2.connect('./sample.db') as conn:
    # # with sqlite3.connect('./sample.db') as conn:
    #     cur = conn.cursor() # as cur:
    #     cur.execute('select * from sampledb')
    #     res = cur.fetchall()

    with psycopg2.connect('./sample.db') as conn:
    # with sqlite3.connect('./sample.db') as conn:
        with conn.cursor() as cur:
            cur.execute('select * from sampledb')
            res = cur.fetchall()
    return res

def test_get_dataframe(mocker):
    return_value = pd.DataFrame({'value':[1,2,3,4]})

    mocker.patch("pandas.read_csv", return_value=return_value)

    actual = get_dataframe()

    assert actual.values.tolist() == [[1],[2],[3],[4]]


def test_get_connection(mocker):

    # mock_cur2 = mocker.Mock()
    # mock_cur2.execute.return_value = True
    # mock_cur2.fetchall.return_value = [1,2,3,4]

    mock_cur = mocker.Mock()
    mock_cur.__enter__ = "a"
    mock_cur.execute.return_value = True
    mock_cur.fetchall.return_value = [1,2,3,4]    
    
    conn_enter_mock = mocker.Mock()
    conn_enter_mock.cursor.return_value = mock_cur

    # with sqlite.connect() as conn: の場合
    # https://docs.python.org/ja/3/library/unittest.mock.html
    conn_mock = mocker.Mock()
    conn_mock.__enter__ = mocker.Mock(return_value=conn_enter_mock)
    conn_mock.__exit__ = mocker.Mock(return_value=True)

    # mock_con = mocker.Mock()
    # mock_con.cursor.return_value = mock_cur


    mocker.patch("psycopg2.connect", return_value=conn_mock)
    # mocker.patch("sqlite3.connect", return_value=conn_mock)
    actual = get_record()

    assert actual == [1,2,3,4]