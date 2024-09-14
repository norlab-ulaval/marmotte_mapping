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
    altimeter_calib_config_folder = os.path.join(get_package_share_directory('altimeter_calibration'))
    description_config_folder = os.path.join(get_package_share_directory('marmotte_description'), 'launch')

    icp_mapper_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(mapper_config_folder, 'icp_mapper_3DOF.launch.py')
        ])
    )

    imu_and_wheel_odom_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(imu_odom_config_folder, 'marmotte_imu_and_wheel_odom_with_altitude_launch.xml')
        ])
    )

    altimeter_calib_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(altimeter_calib_config_folder, 'altimeter_calibration_alti_marmotte.launch.py')
        ])
    )
    
    altitude_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(imu_odom_config_folder, 'marmotte_altitude_computation_launch.xml')
        ])
    )
    
    description_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(description_config_folder, 'description.launch.py')
        ])
    )

    return LaunchDescription([
        icp_mapper_launch,
        imu_and_wheel_odom_launch,
        altimeter_calib_launch,
        altitude_launch,
        description_launch
    ])