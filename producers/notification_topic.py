import pika
import logging
from config.rabbitmq_config import get_connection

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_notification_topic(message, routing_key):
    """Envía una notificación al exchange tipo 'topic'."""
    logging.info("Estableciendo conexión con RabbitMQ...")
    connection = get_connection()
    channel = connection.channel()

    try:
        logging.info(f"Conectado al exchange 'notificaciones_exchange' con tipo 'topic'")
        logging.info(f"Enviando mensaje: '{message}' con routing_key: '{routing_key}'")

        # Publicar el mensaje
        channel.basic_publish(exchange='notificaciones_exchange',
                              routing_key=routing_key,
                              body=message)

        logging.info(f"Mensaje enviado con éxito: {message}")
    except Exception as e:
        logging.error(f"Error al enviar el mensaje: {e}")
    finally:
        connection.close()
        logging.info("Conexión cerrada con RabbitMQ.")

if __name__ == "__main__":
    send_notification_topic("¡Prueba de notificación!", "notificaciones.emergencia")
