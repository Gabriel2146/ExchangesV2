import pika
from config.rabbitmq_config import get_connection

def callback_sms(ch, method, properties, body):
    """Procesa el mensaje recibido para notificaciones por SMS."""
    print(f"Recibido por SMS: {body.decode()}")

def consume_sms():
    """Consume mensajes del exchange tipo 'direct' con routing key 'canal.sms'."""
    connection = get_connection()
    channel = connection.channel()

    # Declarar cola y enlace al exchange 'canal_exchange'
    channel.queue_declare(queue='sms_queue')
    channel.queue_bind(exchange='canal_exchange', queue='sms_queue', routing_key='canal.sms')

    # Consumiendo mensajes
    channel.basic_consume(queue='sms_queue', on_message_callback=callback_sms, auto_ack=True)

    print('Esperando mensajes por SMS. Para salir presiona Ctrl+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_sms()
