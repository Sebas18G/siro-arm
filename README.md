<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulación de Robot en RViz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        h2 {
            color: #444;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
        }
        code {
            background-color: #ddd;
            padding: 2px 5px;
            border-radius: 3px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Simulación de Robot en RViz</h1>

    <p>
        Este proyecto simula un robot en RViz utilizando URDF (Unified Robot Description Format) y modelos 3D creados en Autodesk Inventor. 
        La simulación permite visualizar y analizar el comportamiento del robot en un entorno virtual, facilitando el desarrollo y prueba de algoritmos de control y navegación.
    </p>

    <h2>Descripción del Proyecto</h2>
    <p>
        El robot simulado en este proyecto está diseñado para realizar tareas específicas, como mover objetos, seguir trayectorias y evitar obstáculos. 
        Los modelos 3D se han creado en Autodesk Inventor y se han exportado a formatos compatibles con ROS (Robot Operating System).
    </p>

    <h2>Requisitos</h2>
    <p>Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:</p>
    <ul>
        <li><strong>ROS</strong> (Robot Operating System) - Recomendado: <a href="http://wiki.ros.org/noetic">ROS Noetic</a></li>
        <li><strong>RViz</strong> - Para la visualización de la simulación.</li>
        <li><strong>URDF</strong> - Para la descripción del robot.</li>
        <li><strong>Catkin</strong> - Para construir el espacio de trabajo ROS.</li>
        <li><strong>Autodesk Inventor</strong> - Para crear y modificar los modelos 3D.</li>
    </ul>

    <h2>Instalación</h2>
    <ol>
        <li><strong>Clona el repositorio:</strong>
            <pre><code>git clone https://github.com/tu_usuario/nombre_del_repositorio.git
cd nombre_del_repositorio</code></pre>
        </li>
        <li><strong>Crea un espacio de trabajo de ROS (si no lo tienes):</strong>
            <pre><code>mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace</code></pre>
        </li>
        <li><strong>Copia el repositorio en el espacio de trabajo:</strong>
            <pre><code>cp -r ~/ruta/a/tu/repositorio ~/catkin_ws/src/</code></pre>
        </li>
        <li><strong>Compila el espacio de trabajo:</strong>
            <pre><code>cd ~/catkin_ws
catkin_make</code></pre>
        </li>
        <li><strong>Configura el entorno:</strong>
            <pre><code>source devel/setup.bash</code></pre>
        </li>
    </ol>

    <h2>Uso</h2>
    <ol>
        <li><strong>Lanza el nodo de RViz:</strong>
            <pre><code>rosrun rviz rviz</code></pre>
        </li>
        <li><strong>Carga el archivo de configuración de RViz:</strong>
            <p>En RViz, carga el archivo de configuración (<code>.rviz</code>) que se incluye en este repositorio para visualizar el robot.</p>
        </li>
        <li><strong>Inicia la simulación:</strong>
            <pre><code>roslaunch tu_paquete tu_lanzador.launch</code></pre>
        </li>
        <li><strong>Interactúa con la simulación:</strong>
            <p>Usa los controles en RViz para mover y controlar el robot. Puedes probar diferentes algoritmos de control o modificar la configuración del robot.</p>
        </li>
    </ol>

    <h2>Estructura del Proyecto</h2>
    <pre><code>tu_repositorio/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── tu_lanzador.launch
├── urdf/
│   └── modelo_robot.urdf
└── rviz/
    └── configuracion.rviz
</code></pre>

    <h2>Contribuciones</h2>
    <p>
        Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio y crea una pull request con tus mejoras o correcciones.
    </p>

    <h2>Licencia</h2>
    <p>
        Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo <code>LICENSE</code> para más detalles.
    </p>

    <h2>Contacto</h2>
    <p>
        Para más información o preguntas, puedes contactarme en <a href="mailto:tu_email@example.com">tu_email@example.com</a>.
    </p>
</body>
</html>
