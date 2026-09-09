## Environment
The ROS2 environment is set up on a Ubuntu 26.04 VM running on my Zima OS homelab with ROS 2 Lyrical Luth installed, development is done through a Visual Studio Code tunnel connected via Tailscale

## UUV OpenLab Description
### Contexto del problema
El UUV opera en un entorno subacuático, por lo que es importante detectar de
manera temprana la presencia de agua dentro del enclosure para prevenir daños en
los componentes electrónicos.
Para este reto se utilizará un sistema simulado en ROS 2, donde un sensor
proporcionará información sobre la presencia de agua dentro del enclosure.
Objetivo del reto
Desarrollar un nodo en ROS 2 capaz de recibir información de un sensor de agua y
determinar si existe una posible fuga, publicando el estado del enclosure para que
otros componentes del sistema puedan utilizar esta información.
La prioridad no es desarrollar un sistema de detección altamente sofisticado, sino
aprender a trabajar con ROS 2, entender el flujo de información de un robot y
desarrollar una solución funcional.

### Recursos
- Virtual Machine con Ubuntu (VirtualBox + Oracle (Windows), UTM (Mac))
- ROS 2 instalado
- Workspace de ROS 2
- Repositorio base
- Nodo simulador del sensor
- Git/Github
- Documentación y ejemplos básicos de ROS 2

### Fase 1 — Investigación
1. Familiarizarse con ROS 2 y su estructura básica
2. Explorar los nodos y topics proporcionados
3. Identificar qué información publica el sensor de agua
4. Investigar cómo un nodo puede recibir y publicar información en ROS 2
5. Diseñar una solución para detectar una fuga

Entregable: Diagrama sencillo de flujo de información + descripción de la solución propuesta.

### Fase 2 — Implementación
Crear un nodo water_leak_detector que:
1. Se suscriba al topic del sensor
2. Reciba las mediciones
3. Determine si existe agua dentro del enclosure
4. Publique el resultado en un nuevo topic

Entregable: ROS 2 package funcional + README con instrucciones para ejecutarlo

### Fase 3 — Testing
Se proporcionarán diferentes escenarios para comprobar el funcionamiento del nodo. Después se les dará un pequeño cambio de requerimiento y tendrán que decidir cómo manejarlo.

Entregable: Pruebas realizadas + breve explicación de las decisiones tomadas

### Resultado esperado
Al finalizar, ustedes deberán tener un pequeño sistema funcional en ROS 2 capaz de recibir información de un sensor, procesarla y comunicar un resultado a otro componente del sistema.

**Se evaluará principalmente:**
- Capacidad de aprender ROS 2
- Comprensión de publishers/subscribers
- Lógica de programación
- Organización del código
- Uso de Git
- Capacidad para investigar y resolver problemas
- Documentación