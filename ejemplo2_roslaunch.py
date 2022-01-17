# -------------------------------------------------------------------
# EJEMPLO 2: COMO LANZAR UN "ROSLAUNCH" DESDE CODIGO PYTHON
#
# Importante: no es necesario lanzar "roscore" antes de ejecutar este código
# -------------------------------------------------------------------

import roslaunch
import rospy

# Ruta ABSOLUTA del archivo launch
ruta = "/opt/ros/noetic/share/gazebo_ros/launch/empty_world.launch"

# NOTA: No es imprescindible lanzar un nodo previo! Si quisieramos:
#rospy.init_node('Nodo_lanzador', anonymous=False)

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
launch = roslaunch.parent.ROSLaunchParent(uuid, [ruta])
launch.start()
rospy.loginfo("Archivo launch lanzado. Se cerrará en 15 segundos")

# 15 seconds later
rospy.sleep(15)
rospy.loginfo("Cerrando archivo launch")
launch.shutdown()