from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Set the path to the custom world file
    world_file = os.path.join(
        os.getenv('HOME'), 'ros2_ws', 'src', 'my_robot_description', 'worlds', 'custom_world.world'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=world_file,
            description='Path to the custom Gazebo world file'
        ),

        ExecuteProcess(
            cmd=['gazebo', LaunchConfiguration('world'), '-s', 'libgazebo_ros_factory.so', '-s', 'libgazebo_ros_init.so'],
            output='screen'
        ),
    ])
