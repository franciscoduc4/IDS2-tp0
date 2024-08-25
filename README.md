# IDS2-tp0
# Proyecto de SnapMsg

<img src="logo.jpeg" alt="Logo de SnapMsg" width="400"/>

## Tabla de Contenido
1. [Introducción](#introducción)
2. [Desafíos del Proyecto](#desafíos-del-proyecto)
3. [Pre-requisitos](#pre-requisitos)
4. [Guía de Usuario](#guía-de-usuario)
5. [Construcción de la Imagen Docker](#construcción-de-la-imagen-docker)
6. [Ejecución de la Base de Datos](#ejecución-de-la-base-de-datos)
7. [Ejecución del Servicio](#ejecución-del-servicio)

## Introducción
SnapMsg es un proyecto de mensajería instantánea desarrollado como parte del curso IDS2. Esta aplicación permite a los usuarios enviar y recibir mensajes de forma rápida y eficiente.

## Desafíos del Proyecto
Durante el desarrollo de SnapMsg, nos enfrentamos a varios desafíos:
- Implementación de una arquitectura escalable
- Manejo eficiente de la base de datos
- Asegurar la privacidad y seguridad de los mensajes de los usuarios
- Optimización del rendimiento para manejar múltiples usuarios simultáneos

## Pre-requisitos
Antes de levantar el entorno de desarrollo, asegúrate de tener instalados los siguientes componentes:
- **Lenguaje**: Python 3.10
- **Manejador de paquetes**: pip 21.1 o superior
- **Docker**: Docker 20.10 o superior
- **Docker Compose**: Docker Compose 1.29 o superior

## Guía de Usuario
Para el testing de la aplicación se ha utilizado la librería [pytest](https://docs.pytest.org/en/stable/). Puedes consultar la documentación completa de pytest en el siguiente [link](https://docs.pytest.org/en/stable/).

Para ejecutar los tests, utiliza el siguiente comando de docker:
```bash
docker-compose up --build test
```	

## Posibles Mejoras (desafio opcional)

- Implementar WebSockets para que los usuarios reciban mensajes instantáneamente sin necesidad de hacer polling y se reduzca el tiempo de espera para recibir mensajes y actualizaciones.
- Optimizar la API con algun balanceador de cargas para distribuir el trafico, o implementar caching para reducir el tiempo de respuesta en la base de datos.
- Sistema de Monitoreo, podria usar herramientas como Prometheus y Grafana para monitorear el rendimiento y la disponibilidad de la API y ademas integrar herramientas de analisis para recoger datos sobre el uso de la API y el comportamiento de los usuarios.
