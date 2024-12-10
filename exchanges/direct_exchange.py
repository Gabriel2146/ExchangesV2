import pika
from config.rabbitmq_config import get_connection

def create_direct_exchange():
    """Crea un exchange tipo 'direct'."""
    connection = get_connection()
    channel = connection.channel()

    # Declarar el exchange con tipo 'direct'
    channel.exchange_declare(exchange='canal_exchange', exchange_type='direct')

    print("Exchange tipo 'direct' creado con éxito.")
    connection.close()

if __name__ == "__main__":
    create_direct_exchange()
