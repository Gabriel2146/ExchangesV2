import pika
from config.rabbitmq_config import get_connection

def send_notification_direct(message, routing_key):
    """Envía una notificación al exchange tipo 'direct'."""
    connection = get_connection()
    channel = connection.channel()

    # Publicar mensaje en el exchange 'canal_exchange' (Direct)
    channel.basic_publish(exchange='canal_exchange',
                          routing_key=routing_key,  # Clave de enrutamiento
                          body=message)  # Mensaje a enviar

    print(f"Mensaje enviado al exchange 'direct': {message} al canal: {routing_key}")
    connection.close()

if __name__ == "__main__":
    # Ejemplo de uso: enviar un mensaje con routing_key 'canal.sms'
    send_notification_direct("¡Tu mensaje SMS ha sido enviado!", "canal.sms")
