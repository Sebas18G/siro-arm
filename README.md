# Simulación de Robot en RViz

Este proyecto simula un robot en RViz utilizando **URDF** (Unified Robot Description Format) y modelos 3D creados en **Autodesk Inventor** en formato **STL**. La simulación permite visualizar y analizar el comportamiento del robot en un entorno virtual, facilitando el desarrollo y prueba de algoritmos de control y navegación.

## Descripción del Proyecto

El robot simulado en este proyecto está diseñado para realizar tareas específicas, como mover objetos, seguir trayectorias y evitar obstáculos. Los modelos 3D se han creado en Autodesk Inventor y se han exportado a formato STL, que es compatible con **ROS 2**.

## Instalación de ROS 2 Foxy

Para comenzar con el proyecto, primero necesitas instalar **ROS 2 Foxy**. Puedes seguir la guía oficial de instalación [aquí](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html).

### Pasos para instalar ROS 2 Foxy

1. **Actualiza tu sistema:**
   ```bash
   sudo apt update && sudo apt upgrade

    Instala las dependencias necesarias:

    bash

sudo apt install -y curl gnupg2 lsb-release

Configura las claves y repositorios de ROS 2:

bash

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list'

Instala ROS 2 Foxy:

bash

sudo apt update
sudo apt install ros-foxy-desktop

Configura tu entorno:

bash

    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
    source ~/.bashrc

Creación del Paquete

Después de instalar ROS 2, debes crear un paquete para tu proyecto. Aquí hay un ejemplo de cómo hacerlo:

    Crea un espacio de trabajo:

    bash

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

Crea un nuevo paquete:

bash

ros2 pkg create --build-type ament_cmake nombre_del_paquete

Navega a tu nuevo paquete:

bash

    cd nombre_del_paquete

Estructura de Archivos

En tu paquete, necesitarás crear archivos de lanzamiento (launch), URDF y modelos en STL. Aquí hay una descripción general de la estructura de archivos que debes crear:

go

nombre_del_paquete/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── tu_lanzador.launch.py
├── urdf/
│   └── modelo_robot.urdf
└── models/
    └── modelo_robot.stl

Archivos de Lanzamiento

En el directorio launch/, crea un archivo tu_lanzador.launch.py para iniciar tu simulación. Aquí hay un ejemplo básico:

python

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nombre_del_paquete',
            executable='nombre_del_nodo',
            output='screen',
        ),
    ])

Archivo URDF

Crea tu archivo modelo_robot.urdf en el directorio urdf/. Este archivo debe contener la descripción de tu robot, incluyendo los modelos en STL.
Modelos en STL

Asegúrate de que los modelos STL que has creado en Autodesk Inventor estén en el directorio models/.
Uso

    Lanza el nodo de RViz:

    bash

ros2 run rviz2 rviz2

Carga el archivo de configuración de RViz: En RViz, carga el archivo de configuración (.rviz) que se incluye en este repositorio para visualizar el robot.

Inicia la simulación:

bash

ros2 launch nombre_del_paquete tu_lanzador.launch.py

Interactúa con la simulación: Usa los controles en RViz para mover y controlar el robot. Puedes probar diferentes algoritmos de control o modificar la configuración del robot.
