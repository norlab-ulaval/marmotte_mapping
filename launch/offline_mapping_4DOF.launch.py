import os

import yaml
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import (
    AnyLaunchDescriptionSource,
    PythonLaunchDescriptionSource,
)


def generate_launch_description():

    
    mapper_config_folder = os.path.join(get_package_share_directory('marmotte_mapping'), 'launch', 'include')
    imu_odom_config_folder = os.path.join(get_package_share_directory('norlab_imu_tools'), 'launch')
    
    pcl_desk_config_folder = os.path.join(get_package_share_directory('pointcloud_motion_deskew'), 'launch')
    
    icp_mapper_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(mapper_config_folder, 'icp_mapper_4DOF.launch.py')
        ])
    )

    imu_and_wheel_odom_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(imu_odom_config_folder, 'marmotte_imu_and_wheel_odom_without_altitude_launch.xml')
        ])
    )

    pcl_deskew_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(pcl_desk_config_folder, 'deskew.launch.xml')
        ])
    )
    
    altitude_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(imu_odom_config_folder, 'marmotte_altitude_computation_launch.xml')
        ])
    )

    return LaunchDescription([
        icp_mapper_launch,
        imu_and_wheel_odom_launch,
        pcl_deskew_launch,
        altitude_launch
    ])