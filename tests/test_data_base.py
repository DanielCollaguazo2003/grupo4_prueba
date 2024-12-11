from src.data_base import get_db_connection, execute_query

def test_get_db_connection():
    conn = get_db_connection()
    assert conn is not None

def test_execute_query(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.return_value = None

    mocker.patch("src.data_base.get_db_connection", return_value=mock_conn)

    query = "SELECT 1"
    result = execute_query(query)

    assert result == mock_cursor
    mock_cursor.execute.assert_called_with(query, ())
