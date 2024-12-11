import pika

def consume_sms():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="localhost",
            virtual_host="exchanges_vhost",
            credentials=pika.PlainCredentials("GabrielP", "2146")
        )
    )
    channel = connection.channel()
    queue_name = "sms_queue"

    # Declarar la cola en caso de que no exista
    channel.queue_declare(queue=queue_name, durable=True)

    print(f"[SMS] Esperando mensajes en '{queue_name}'. Presiona Ctrl+C para salir.")

    # Callback para procesar los mensajes
    def callback(ch, method, properties, body):
        print(f"[SMS] Mensaje recibido: {body.decode()}")
        # Confirma que el mensaje fue procesado
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Consumir mensajes de la cola
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    # Iniciar el consumo
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\n[SMS] Consumidor detenido.")
        connection.close()

if __name__ == "__main__":
    consume_sms()
