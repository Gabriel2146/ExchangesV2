import pika
from config.rabbitmq_config import get_connection

def send_notification_topic(message, routing_key):
    """Envía una notificación al exchange tipo 'topic'."""
    connection = get_connection()
    channel = connection.channel()

    # Publicar mensaje en el exchange 'notificaciones_exchange'
    channel.basic_publish(exchange='notificaciones_exchange',
                          routing_key=routing_key,  # Clave de enrutamiento
                          body=message)

    print(f"Mensaje enviado: {message} con routing key: {routing_key}")
    connection.close()

if __name__ == "__main__":
    send_notification_topic("¡Alerta! Nueva notificación importante.", "notificaciones.emergencia")
