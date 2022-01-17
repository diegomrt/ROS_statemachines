# -------------------------------------------------------------------
# EJEMPLO 3: LANZAR "ROSLAUNCH" + "ROSRUN" DESDE CODIGO PYTHON
#
# Importante: hay que lanzar "roscore" antes de ejecutar este código
# -------------------------------------------------------------------

import roslaunch
import rospy

# Como lanzar un archivo launch (roslaunch)
ruta = "/opt/ros/noetic/share/gazebo_ros/launch/empty_world.launch"

# NOTA: No es imprescindible lanzar un nodo previo! Si quisieramos:
#rospy.init_node('Nodo_lanzador', anonymous=False)

# 1. LANZAMIENTO ROSLAUNCH ------------------------------------------
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
launch1 = roslaunch.parent.ROSLaunchParent(uuid, [ruta])
launch1.start()
rospy.loginfo("ROSLAUNCH lanzado")

# Espera 5 segundos
rospy.loginfo("Esperando 5s para siguiente lanzamiento")
rospy.sleep(5)

# 2. LANZAMIENTO ROSRUN ---------------------------------------------
# Como lanzar un ejecutable (rosrun)
node2 = roslaunch.core.Node('rviz', 'rviz')
launch2 = roslaunch.scriptapi.ROSLaunch()
launch2.start()
process2 = launch2.launch(node2)
# Espera 5 segundos y lo acaba
rospy.loginfo("Esperando 8s")
rospy.sleep(8)

# 3. ACABAR AMBOS ---------------------------------------------
launch1.shutdown() # Matar Roslaunch
process2.stop()    # Matar Rosrun
rospy.loginfo("Cerrando ROSLAUNCH y ROSRUN")

# SIN PROBAR: Si necesitamos que permanezcan hasta Ctrl+C: 
#try:
#  launch.spin()
#finally:
#  After Ctrl+C, stop all nodes from running
# launch.shutdown()
