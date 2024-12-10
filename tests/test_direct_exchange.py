import unittest
from unittest.mock import patch, MagicMock

import pika
from producers.notification_direct import send_notification_direct


class TestDirectExchangeProducer(unittest.TestCase):

    @patch('pika.BlockingConnection')
    def test_send_message_direct(self, MockBlockingConnection):
        # Mock de la conexión y el canal
        mock_connection = MagicMock()
        mock_channel = MagicMock()

        # Configuración para devolver el mock_channel cuando se establece la conexión
        MockBlockingConnection.return_value = mock_connection
        mock_connection.channel.return_value = mock_channel

        # Definir el mensaje y routing_key
        message = "Test SMS message"
        routing_key = "canal.sms"

        # Llamar a la función que estamos probando
        send_notification_direct(message, routing_key)

        # Verificar que la conexión y el canal se hayan abierto correctamente
        MockBlockingConnection.assert_called_once_with(pika.ConnectionParameters('localhost'))
        mock_connection.channel.assert_called_once()

        # Verificar que el mensaje se haya enviado correctamente con el exchange 'direct_exchange'
        mock_channel.basic_publish.assert_called_once_with(
            exchange='direct_exchange',
            routing_key=routing_key,
            body=message
        )

if __name__ == '__main__':
    unittest.main()
