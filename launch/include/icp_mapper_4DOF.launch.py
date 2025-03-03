import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.substitutions import Command


def generate_launch_description():

    share_folder = get_package_share_directory('marmotte_mapping')
    config_file = os.path.join(share_folder, 'params', '_icp_mapper.yaml')

    mapper_node = Node(
        package='norlab_icp_mapper_ros',
        executable='mapper_node',
        name='mapper_node',
        output='screen',
        parameters=[
            config_file,
            {"mapping_config": os.path.join(share_folder, "params", "mapping", "_mapping_4DOF.yaml")},
            {"use_sim_time": True},
        ],
        remappings=[
            ('points_in', 'lslidar16/points'),
        ]
    )

    return LaunchDescription([
        mapper_node
    ])
