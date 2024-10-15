## Descripción del Proyecto

El robot simulado en este proyecto está diseñado para realizar tareas específicas, como mover objetos, seguir trayectorias y evitar obstáculos. Los modelos 3D se han creado en Autodesk Inventor y se han exportado a formato STL, que es compatible con **ROS 2**.

Para este proyecto se esta utilizando ROS2 Foxy

# Explicación del Código de Lanzamiento en ROS 2

Este documento describe un script de lanzamiento en ROS 2 diseñado para cargar un modelo de robot definido en un archivo URDF y para iniciar varios nodos necesarios para su funcionamiento. Estos nodos incluyen el `robot_state_publisher`, el `joint_state_publisher`, el `joint_state_publisher_gui`, y `rviz2`.

## Estructura del Código

### Importaciones

El script comienza importando las bibliotecas necesarias. Se utilizan módulos de lanzamiento y ROS 2 para crear y gestionar el lanzamiento de nodos, así como herramientas para manejar rutas de archivos. También se importa una función que permite obtener la ruta compartida de un paquete específico en ROS.

### Función Principal

La función principal, denominada `generate_launch_description`, se encarga de generar y devolver una descripción de lanzamiento. Esta descripción define qué nodos se ejecutarán y cómo se configurarán.

### Cargar el Archivo URDF

Dentro de la función principal, se define el nombre del archivo URDF que describe el modelo del robot. Luego, se construye la ruta a este archivo utilizando la función que obtiene la ruta compartida del paquete correspondiente. Posteriormente, se abre el archivo y se lee su contenido, que se almacena en una variable que representa la descripción del robot.

### Nodos de Lanzamiento

El script define varios nodos que se iniciarán al ejecutar el lanzamiento:

1. **Nodo `robot_state_publisher`:** Este nodo es responsable de publicar el estado del robot en el sistema. Utiliza la descripción del robot que fue leída del archivo URDF para transmitir información sobre su estado actual.

2. **Nodo `joint_state_publisher`:** Este nodo se encarga de publicar los estados de las articulaciones del robot. Se activa solo si no se ha especificado un argumento que permita activar una interfaz gráfica.

3. **Nodo `joint_state_publisher_gui`:** Este nodo proporciona una interfaz gráfica que permite a los usuarios manipular y publicar los estados de las articulaciones del robot de manera más intuitiva. Se activa únicamente si se especifica el argumento que indica que se desea utilizar la interfaz gráfica.

4. **Nodo `rviz2`:** Este nodo inicia RViz, que es una herramienta de visualización en 3D para ROS. Permite la visualización del robot y de sus estados, lo que es fundamental para la interacción y el análisis del comportamiento del robot en un entorno visual.

### Retorno de la Descripción de Lanzamiento

Al final de la función, se devuelve una descripción de lanzamiento que incluye el argumento para activar o desactivar la interfaz gráfica, junto con los nodos definidos anteriormente. Esto permite una configuración flexible y fácil de usar al momento de iniciar el sistema.
# Explicación del Archivo URDF para el Robot "Seguidor_linea_robot"

Este documento describe el archivo URDF (Unified Robot Description Format) que define la estructura y los componentes del robot llamado "Seguidor_linea_robot". Este URDF fue generado automáticamente por SolidWorks utilizando un exportador específico. A continuación, se explican las distintas secciones y elementos que componen el archivo.

## Estructura General

El archivo comienza con la definición del robot, nombrado "Seguidor_linea_robot". A continuación, se enumeran los componentes del robot, incluidos los enlaces (links) y las articulaciones (joints). Estos elementos describen tanto la geometría visual del robot como su funcionalidad mecánica.

### Links

1. **Link del Mundo**: Se define un enlace denominado "world" que actúa como referencia global para el robot. Este enlace sirve como el entorno de referencia para todos los demás componentes del robot.

2. **Base Link**: Este es el enlace principal del robot. Incluye:
   - Un modelo 3D cargado desde un archivo STL, que define la geometría visual del enlace.
   - Un color que lo representa en el entorno de visualización, definido como rojo y opaco.

3. **Link_1**: Este es el primer enlace del robot que se conecta al enlace base. Sus características incluyen:
   - Un modelo 3D cargado desde un archivo STL.
   - Un color azul, opaco, y su geometría de colisión se define utilizando el mismo modelo.

4. **Link_2**: Este es el segundo enlace del robot. Al igual que Link_1, incluye:
   - Un modelo 3D de su geometría.
   - Un color verde, semi-transparente, y su geometría de colisión se define con el mismo modelo.

5. **Link_3**: Este es el tercer enlace del robot. Sus características son similares a las de Link_2, con:
   - Un modelo 3D cargado desde un archivo STL.
   - Un color verde, semi-transparente, y una geometría de colisión definida con el mismo modelo.

### Joints

1. **Joint Fijo**: Este joint conecta el mundo con el `base_link`. No permite movimiento, y su posición y orientación se definen en coordenadas XYZ y roll, pitch y yaw. El eje de rotación se establece en el eje Z.

2. **Joint Eslabon_Base**: Este joint permite el movimiento entre el `base_link` y `Link_1`. Es un joint de tipo revoluto que permite rotación alrededor del eje Z. Sus límites de rotación están definidos para permitir movimientos de -90 a 90 grados.

3. **Joint Eslabon_1**: Este joint conecta `Link_1` y `Link_2`. También es un joint de tipo revoluto, pero permite rotación alrededor del eje X. Sus límites de rotación son de 90 a 270 grados.

4. **Joint Eslabon_2**: Este joint permite el movimiento entre `Link_2` y `Link_3`. Similar a Eslabon_1, es un joint de tipo revoluto que permite rotación alrededor del eje X. Sus límites de rotación van de -90 a 90 grados.

# Simulación de Robot en RViz

Este proyecto simula un robot en RViz utilizando **URDF** (Unified Robot Description Format) y modelos 3D creados en **Autodesk Inventor** en formato **STL**. La simulación permite visualizar y analizar el comportamiento del robot en un entorno virtual, facilitando el desarrollo y prueba de algoritmos de control y navegación.

## Requisitos

- ROS2 instalado (preferiblemente la distribución más reciente)
- RViz
- Dependencias de ROS2 para trabajar con URDF y STL

## Instrucciones de Compilación y Ejecución

1. Compila el paquete utilizando el comando `colcon build`.
2. Arranca el entorno de ROS2 ejecutando `source install/setup.bash`.
3. Lanza la simulación en RViz con el comando `ros2 launch modelo_robot display_robot.py`.

## Descripción del Proyecto

- **URDF**: El formato URDF se utiliza para describir la estructura del robot, sus enlaces, uniones y características físicas.
- **Modelos 3D**: Los modelos en formato STL creados en Autodesk Inventor se utilizan para proporcionar una representación visual detallada del robot en RViz.
- **Análisis del Comportamiento**: La simulación permite observar el comportamiento del robot y realizar pruebas de navegación y control en un entorno virtual antes de la implementación en el mundo real.


## Adecuacion del RVIZ

1. Al ejecutar el archivo de lanzamiento, es común que aparezcan errores en la interfaz de RViz. Para solucionarlos, primero nos dirigimos a la sección "Display" y configuramos la opción "Fixed Frame". En este campo, seleccionamos "world", que indica la posición inicial en el entorno.
2. A continuación, agregamos el modelo de nuestro robot haciendo clic en el botón "Add" y seleccionando "RobotModel".
3. Al expandir las opciones de "RobotModel", configuramos la opción "Description Source" estableciéndola en "Topic". Luego, en "Description Topic", seleccionamos la opción "/robot_description".
4. Con estos pasos, deberíamos poder visualizar correctamente las piezas del robot y tener la interfaz de RViz configurada adecuadamente.
