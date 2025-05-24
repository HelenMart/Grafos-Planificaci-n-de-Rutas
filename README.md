# 🚚 Planificador de Rutas Óptimas con Dijkstra

Esta aplicación permite planificar rutas óptimas para la entrega de paquetes utilizando grafos dirigidos y ponderados. Implementa el algoritmo de Dijkstra y visualiza la ruta más eficiente en un mapa interactivo.

## 🧠 Características

- Cálculo de rutas óptimas con el algoritmo de Dijkstra.
- Visualización de rutas en mapa usando Leaflet + OpenStreetMap.
- Interfaz web sencilla para ingresar puntos de origen y destino.
- Basado en coordenadas geográficas (latitud,longitud).
- Fácil de modificar y escalar.

## 🔧 Tecnologías utilizadas

- Backend: **Python + Flask**
- Algoritmo: **Dijkstra**
- Frontend: **HTML + JavaScript + Leaflet**
- Mapa: **OpenStreetMap**

## Requisitos

- Instala los requerimientos desde tu terminal : pip install -r requirements.txt
- Ejecuta el servidor: python app.py
- Abrir el navegador y visitar: http://127.0.0.1:5000

## 🗺️Pasos para usar la aplicación

- Ingresa un ID de nodo para el origen (ej. 14.6349,-90.5069).
- Ingresa un ID de nodo para el destino (ej. 14.6370,-90.5120).
- Haz clic en "Planificar Ruta".
- Verás la distancia y la ruta trazada en el mapa.

## 🧪 Datos de prueba

- Puedes usar estas combinaciones para probar:
- Origen: 14.6349,-90.5069
- Destino: 14.6370,-90.5120

- Otra opción:
- Origen: 14.6310,-90.5080
- Destino: 14.6370,-90.5120
