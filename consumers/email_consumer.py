import pika
from config.rabbitmq_config import get_connection

def callback_email(ch, method, properties, body):
    """Procesa el mensaje recibido para notificaciones por email."""
    print(f"Recibido por email: {body.decode()}")

def consume_email():
    """Consume mensajes del exchange tipo 'topic' con routing key 'notificaciones.email'."""
    connection = get_connection()
    channel = connection.channel()

    # Declarar cola y enlace al exchange 'notificaciones_exchange'
    channel.queue_declare(queue='email_queue')
    channel.queue_bind(exchange='notificaciones_exchange', queue='email_queue', routing_key='notificaciones.email')

    # Consumiendo mensajes
    channel.basic_consume(queue='email_queue', on_message_callback=callback_email, auto_ack=True)

    print('Esperando mensajes por email. Para salir presiona Ctrl+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_email()
