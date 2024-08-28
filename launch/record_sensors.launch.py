import os, yaml
from pathlib import Path
from datetime import datetime

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    config_folder = os.path.join(get_package_share_directory('marmotte_mapping'), 'params')
    topics_file = os.path.join(config_folder, 'topics_to_record.yaml')

    bag_time = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    bag_output_dir = os.path.join(Path.home(), 'rosbags', ('rosbag2_' + bag_time))

    topics_list = yaml.safe_load(open(topics_file, 'r'))["topics"]
    command = ['ros2', 'bag', 'record', '-s', 'mcap', '-o', bag_output_dir]
    command.extend(topics_list)

    sensors_record_process = ExecuteProcess(
        name="rosbag_record",
        cmd=command,
        output='screen'
    )

    return LaunchDescription([
        sensors_record_process
    ])