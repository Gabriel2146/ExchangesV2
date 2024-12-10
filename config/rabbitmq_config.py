import pika

def get_connection():
    """Establece una conexión a RabbitMQ con las credenciales definidas en docker-compose."""
    credentials = pika.PlainCredentials('GabrielP', '2146')  # Usuario y clave definidos
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost',  # RabbitMQ se ejecuta en el mismo host
        port=5672,
        credentials=credentials
    ))
    return connection
