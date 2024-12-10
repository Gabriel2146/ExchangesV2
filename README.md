Aquí tienes el contenido del `README.md` en texto plano:  

---

EXCHANGESV2  

Este proyecto implementa un sistema de mensajería basado en RabbitMQ utilizando dos tipos de exchanges: Topic y Direct. El propósito es demostrar el manejo de colas con un enfoque modular, siguiendo buenas prácticas y cumpliendo con el patrón arquitectónico Event-Driven Architecture (Broker Pattern).  

---  

## Estructura del Proyecto  

EXCHANGESV2/  
├── docker-compose.yml        # Configuración para levantar RabbitMQ con Docker.  
├── README.md                 # Documentación del proyecto.  
├── producers/                # Código para los productores.  
│   ├── __init__.py  
│   ├── notification_topic.py # Productor para el exchange tipo Topic.  
│   ├── notification_direct.py # Productor para el exchange tipo Direct.  
├── consumers/                # Código para los consumidores.  
│   ├── __init__.py  
│   ├── consumer_topic.py     # Consumidor para el exchange tipo Topic.  
│   ├── consumer_direct.py    # Consumidor para el exchange tipo Direct.  
├── tests/                    # Pruebas unitarias.  
│   ├── __init__.py  
│   ├── test_topic_exchange.py  # Pruebas para el exchange tipo Topic.  
│   ├── test_direct_exchange.py # Pruebas para el exchange tipo Direct.  
├── config/                   # Configuración general.  
│   ├── __init__.py  
│   ├── rabbitmq_config.py    # Configuración de RabbitMQ.  
├── main.py                   # Punto de entrada para iniciar productores/consumidores.  

---  

## Requisitos Previos  

1. Python 3.8+  
2. RabbitMQ (levantarlo con Docker Compose incluido o instalar manualmente).  
3. Dependencias de Python (especificadas en requirements.txt):  

```bash  
pip install -r requirements.txt  
```  

---  

## Uso  

### 1. Levantar RabbitMQ con Docker Compose  

Asegúrate de que Docker esté instalado y ejecutándose. Luego, en la raíz del proyecto, ejecuta:  

```bash  
docker-compose up -d  
```  

Esto iniciará RabbitMQ en localhost con:  
- Usuario: GabrielP  
- Contraseña: 2146  
- Management UI: http://localhost:15672  

---  

### 2. Ejecutar los Productores  

#### Exchange Tipo Topic  
Para enviar un mensaje utilizando el exchange topic_exchange:  

```bash  
python producers/notification_topic.py  
```  

#### Exchange Tipo Direct  
Para enviar un mensaje utilizando el exchange direct_exchange:  

```bash  
python producers/notification_direct.py  
```  

---  

### 3. Ejecutar los Consumidores  

#### Exchange Tipo Topic  
Para consumir mensajes del exchange topic_exchange:  

```bash  
python consumers/consumer_topic.py  
```  

#### Exchange Tipo Direct  
Para consumir mensajes del exchange direct_exchange:  

```bash  
python consumers/consumer_direct.py  
```  

---  

### 4. Ejecutar las Pruebas  

Para ejecutar las pruebas unitarias, utiliza unittest desde la raíz del proyecto:  

```bash  
python -m unittest discover tests  
```  

Esto ejecutará las pruebas definidas en `tests/test_topic_exchange.py` y `tests/test_direct_exchange.py`.  

---  

## Principios de Diseño Aplicados  

- Modularidad: Cada tipo de exchange tiene su propio productor y consumidor.  
- Principios SOLID: Las clases y funciones tienen una única responsabilidad.  
- Buenas prácticas: La estructura sigue un esquema limpio y comprensible.  

---  

## Futuras Mejoras  

1. Añadir soporte para más tipos de exchanges (e.g., fanout, headers).  
2. Implementar una interfaz gráfica para visualizar mensajes en tiempo real.  
3. Optimizar las pruebas con más casos de enrutamiento.  

---  

## Créditos  

Proyecto desarrollado por Gabriel utilizando Python y RabbitMQ.  

---  