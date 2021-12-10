import pandas as pd
import sqlite3
import psycopg2
import pytest

class DBConnector:
    def __enter__(self):
        self.connect = psycopg2.connect()
        return self.connect
    
    def __exit__(self, ex_type, ex_value, trace):
        self.connect.close()


def get_record():
    with DBConnector() as conn:
        with conn.cursor() as cur:
            cur.execute('select * from sampledb')
            print(cur.fetchall())
    return None

@pytest.fixture()
def dummyConnector(mocker):
    mock_cur2 = mocker.Mock()
    mock_cur2.execute.return_value = True
    mock_cur2.fetchall.return_value = "abcdefghijk"

    cur_enter_mock = mocker.Mock()
    cur_enter_mock.__enter__ =  mocker.Mock(return_value=mock_cur2)
    cur_enter_mock.__exit__ = mocker.Mock()
    
    conn_enter_mock = mocker.Mock()
    conn_enter_mock.cursor.return_value = cur_enter_mock

    # https://docs.python.org/ja/3/library/unittest.mock.html
    conn_mock = mocker.Mock()
    conn_mock.__enter__ = mocker.Mock(return_value=conn_enter_mock)
    conn_mock.__exit__ = mocker.Mock()

    return conn_mock

def test_get_connection(dummyConnector, mocker):

    mocker.patch("test_mock2.DBConnector", return_value=dummyConnector)
    actual = get_record()

    assert actual == None