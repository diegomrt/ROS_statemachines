# -------------------------------------------------------------------
# EJEMPLO MAQUINA SMACH CON DOS ESTADOS
#      ESTADO 1: LANZA "ROSLAUNCH"
#      ESTADO 2: LANZA "ROSRUN"
#
# Importante: hay que lanzar "roscore" antes de ejecutar este código
#             
#             Si la máquina de estados se interrumpe antes de terminar
#             suele ser necesario cerrar y abrir roscore de nuevo 
# ----------------------------------------------------------------- -

import rospy
import smach
import roslaunch

# Estado 1: lanza Gazebo mediante un ROSLAUNCH
class estado1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['salida1','salida2'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Ejecutando estado 1')
        
        # LANZAMIENTO ROSLAUNCH ----------------------------------
        ruta = "/opt/ros/noetic/share/gazebo_ros/launch/empty_world.launch"
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        launch1 = roslaunch.parent.ROSLaunchParent(uuid, [ruta])
        launch1.start()
        rospy.loginfo("ROSLAUNCH lanzado")

        # Espera y cierra el launch
        rospy.loginfo("Esperando 7 s")
        rospy.sleep(7)
        launch1.shutdown() # Matar Roslaunch
        
        # Cambio estado: Codigo para ejecutar 2 veces antes de terminar
        if self.counter < 2:
            self.counter += 1
            return 'salida1'
        else:
            return 'salida2'


# Estado 2: lanza RViz mediante un ROSRUN
class estado2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['salida1'])

    def execute(self, userdata):
        rospy.loginfo('Ejecutando estado 2: Lanzamiento de RVIZ durante 10s')
        
        # LANZAMIENTO ROSRUN --------------------------
        node2 = roslaunch.core.Node('rviz', 'rviz')
        launch2 = roslaunch.scriptapi.ROSLaunch()
        launch2.start()
        process2 = launch2.launch(node2)

        # Espera 8 segundos, para RVIZ y da salida 1
        rospy.loginfo("Esperando 8 s")
        rospy.sleep(8)
        process2.stop()    # Matar Rosrun
        return 'salida1'
        
# main
def main():
    rospy.init_node('estados_con_launch')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['fin', 'outcome5'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('ESTADO1', estado1(), 
                               transitions={'salida1':'ESTADO2', 
                                            'salida2':'fin'})
        smach.StateMachine.add('ESTADO2', estado2(), 
                               transitions={'salida1':'ESTADO1'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
