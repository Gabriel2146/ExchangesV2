import pika
import logging
from config.rabbitmq_config import get_connection

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def callback(ch, method, properties, body):
    """Procesa los mensajes recibidos."""
    logging.info(f"Mensaje recibido en la cola: {body.decode()}")
    logging.info(f"Routing Key: {method.routing_key}")
    logging.info(f"Procesando mensaje...")
    # Aquí puedes agregar lógica adicional para procesar el mensaje
    logging.info("Procesamiento completado.")

def consume_topic():
    """Consume mensajes del exchange tipo 'topic'."""
    logging.info("Estableciendo conexión con RabbitMQ...")
    connection = get_connection()
    channel = connection.channel()

    # Declarar el exchange
    channel.exchange_declare(exchange='notificaciones_exchange', exchange_type='topic')

    # Declarar una cola temporal para recibir mensajes
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Vincular la cola al exchange con un patrón de clave de enrutamiento
    binding_key = 'notificaciones.*'  # Puedes modificar esto según tus necesidades
    channel.queue_bind(exchange='notificaciones_exchange', queue=queue_name, routing_key=binding_key)

    logging.info(f"Esperando mensajes en la cola '{queue_name}' con patrón '{binding_key}'...")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    try:
        logging.info("Iniciando consumo de mensajes...")
        channel.start_consuming()
    except KeyboardInterrupt:
        logging.info("Consumo interrumpido manualmente.")
    finally:
        connection.close()
        logging.info("Conexión cerrada con RabbitMQ.")

if __name__ == "__main__":
    consume_topic()
