from src.models import Cliente, Servicio, Habitacion, Reserva, Factura, Pago
from src.main import agregar_cliente, agregar_servicio

def test_agregar_cliente(mocker):
    mock_cursor = mocker.Mock()
    mock_cursor.fetchone.return_value = [1]
    mock_db = mocker.patch("src.data_base.execute_query", return_value=mock_cursor)

    cliente = Cliente(nombre="Jane Doe", email="jane@example.com", telefono="9876543210")
    result = agregar_cliente(cliente)

    assert result == {"idCliente": 1}
    mock_db.assert_called_once()

def test_agregar_servicio(mocker):
    mock_cursor = mocker.Mock()
    mock_cursor.fetchone.return_value = [1]
    mock_db = mocker.patch("src.data_base.execute_query", return_value=mock_cursor)

    servicio = Servicio(descripcion="Wi-Fi", precio=15.5)
    result = agregar_servicio(servicio)

    assert result == {"idServicios": 1}
    mock_db.assert_called_once()
