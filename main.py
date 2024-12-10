import sys
from exchanges.topic_exchange import create_topic_exchange
from exchanges.direct_exchange import create_direct_exchange
from producers.notification_topic import send_notification_topic
from producers.notification_direct import send_notification_direct
from consumers.email_consumer import consume_email
from consumers.sms_consumer import consume_sms

def main():
    # Crear exchanges
    create_topic_exchange()
    create_direct_exchange()

    # Enviar mensajes (prueba de productor)
    send_notification_topic("¡Notificación de emergencia!", "notificaciones.emergencia")
    send_notification_direct("Notificación SMS", "canal.sms")

    # Consumir mensajes (puedes ejecutar estas funciones en diferentes terminales)
    consume_email()  # En un terminal separado
    consume_sms()    # En otro terminal separado

if __name__ == "__main__":
    main()
