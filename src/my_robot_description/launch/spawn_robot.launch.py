import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Create the absolute path to the URDF file
    urdf_file_path = os.path.join(
        os.getenv('HOME'), 'ros2_ws', 'src', 'my_robot_description', 'urdf', 'example_robot.urdf'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'urdf_file',
            default_value=urdf_file_path,
            description='Absolute path to the URDF file'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'robot',
                '-file', LaunchConfiguration('urdf_file'),
                '-x', '0', '-y', '0', '-z', '1'
            ],
            output='screen'
        )
    ])

