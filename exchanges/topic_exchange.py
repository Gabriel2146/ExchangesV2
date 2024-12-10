import pika
from config.rabbitmq_config import get_connection

def create_topic_exchange():
    """Crea un exchange tipo 'topic'."""
    connection = get_connection()
    channel = connection.channel()

    # Declarar el exchange con tipo 'topic'
    channel.exchange_declare(exchange='notificaciones_exchange', exchange_type='topic')

    print("Exchange tipo 'topic' creado con éxito.")
    connection.close()

if __name__ == "__main__":
    create_topic_exchange()
