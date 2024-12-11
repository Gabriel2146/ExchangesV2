import subprocess
import platform
from exchanges.topic_exchange import create_topic_exchange
from exchanges.direct_exchange import create_direct_exchange
from producers.notification_topic import send_notification_topic
from producers.notification_direct import send_notification_direct

def start_consumer(module_name):
    """Inicia un consumidor como subproceso."""
    command = ["python", "-m", module_name]
    return subprocess.Popen(command)

def main():
    # Crear exchanges
    create_topic_exchange()
    create_direct_exchange()

    # Enviar mensajes (prueba de productor)
    send_notification_topic("¡Notificación de emergencia!", "notificaciones.emergencia")
    send_notification_direct("Notificación SMS", "canal.sms")

    # Iniciar consumidores
    consumers = []
    try:
        consumers.append(start_consumer("consumers.email_consumer"))
        consumers.append(start_consumer("consumers.sms_consumer"))

        print("Consumidores iniciados. Presiona Ctrl+C para detenerlos.")
        for process in consumers:
            process.wait()  # Espera a que el proceso termine
    except KeyboardInterrupt:
        print("Deteniendo consumidores...")
        for process in consumers:
            process.terminate()
    finally:
        print("Finalizado.")

if __name__ == "__main__":
    main()
