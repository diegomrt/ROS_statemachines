# -------------------------------------------------------------------
# EJEMPLO 1: COMO LANZAR UN "ROSRUN" DESDE CODIGO PYTHON
#
# Importante: primero lanzar "roscore" antes de ejecutar este código
# -------------------------------------------------------------------

import roslaunch
import rospy

# NOTA: No es imprescindible lanzar un nodo previo! Si quisieramos:
# rospy.init_node('Nodo_lanzador', anonymous=False)

# 1. LANZAMIENTO RVIZ ---------------------------------------------
# Primer argumento: paquete. Segundo argumento: ejecutable
node = roslaunch.core.Node('rviz', 'rviz')
launch = roslaunch.scriptapi.ROSLaunch()
launch.start()
process = launch.launch(node)
# Espera 10 segundos y lo acaba
rospy.loginfo("Esperando 8s")
rospy.sleep(8)
process.stop()

# 2. LANZAMIENTO RQT_IMAGE VIEW -------------------------------------
node = roslaunch.core.Node('rqt_image_view', 'rqt_image_view')
launch = roslaunch.scriptapi.ROSLaunch()
launch.start()
process = launch.launch(node)
# Espera 5 segundos y lo acaba
rospy.loginfo("Esperando 5s")
rospy.sleep(5)
process.stop()

# 3. LANZAMIENTO DOS ROSRUN A LA VEZ ---------------------------------
node1 = roslaunch.core.Node('rqt_image_view', 'rqt_image_view')
launch1 = roslaunch.scriptapi.ROSLaunch()
node2 = roslaunch.core.Node('rviz', 'rviz')
launch2 = roslaunch.scriptapi.ROSLaunch()

launch1.start()
process1 = launch1.launch(node1)

launch2.start()
process2 = launch2.launch(node2)

# Espera 30 segundos y los acabas
rospy.loginfo("Esperando 10s")
rospy.sleep(10)
process1.stop()
process2.stop()

