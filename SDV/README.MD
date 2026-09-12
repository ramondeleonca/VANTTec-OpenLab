## SDV OpenLab Description
Software | Implementación de Dijkstra / Programación Orientada a Objetos

### Tarea principal:
Implementación del algoritmo de Dijkstra usando programación orientada a objetos, utilizando **Python o C++**.

### Actividades secundarias:
- Implementación de una interfaz de usuario que permita crear y modificar el grafo, seleccionar un punto de inicio y un punto de destino, y solicitar la ruta óptima. (opcional hacerla gui)
- Implementación del algoritmo de Dijkstra desde cero para encontrar la ruta de menor costo.
- Uso de programación orientada a objetos para representar los elementos del sistema, como nodos, conexiones y el grafo.
- Documentación del código, explicando cada clase, sus atributos, métodos y responsabilidades.
- Representación visual de la estructura de datos utilizada y explicación de cómo se relacionan sus componentes.
- Realización de pruebas con diferentes grafos, puntos de inicio y destino.
- Manejo de casos en los que no exista una ruta disponible.
- Explicación de las decisiones tomadas durante la implementación y del funcionamiento del algoritmo.

**Entregables sugeridos:**
- Código fuente funcional.
- Interfaz para la creación y consulta del grafo.
- Documentación de las clases y estructura del programa.
- Representación visual de la estructura de datos.
- Ejemplos de pruebas y resultados.

### Dijkstra requirements
1. Starts from a chosen node
2. Ends at a chosen node
3. Terminates if there is no possible path
4. A node can have multiple edges connecting to other nodes at specified distances

### Dijkstra procedure
1. Starts at the chosen node
2. Checks all connected node's distances (current distance from start + edge distance)
3. Repeat recursively at the smallest node until there are no forward edges (not a solution) or the end node is reached
4. If the path for the current node is not a solution, continue with the next smallest

## Features
- Multithreading / parallelism
- Python data-class and heapq based implementation
- Timer profiling
- Template typing
- Node independence