import argparse
import configparser
import os
import io

parser = argparse.ArgumentParser(description='Simple Task Scheduler')
parser.add_argument('time', type=str,
                    help='task time that you are using')
parser.add_argument('-d', '--directory', type=str,
                    help='directory that configs are loaded from')

args = parser.parse_args()

task_time = args.time
start_directory = args.directory

if start_directory is None:
    start_directory = "/etc/task-scheduler"



directory = start_directory+"/conf.d"
for filename in os.listdir(directory):
    if filename.endswith(".conf"):
        config = configparser.RawConfigParser()
        config.read(directory+"/"+filename)

        if config.get('task', 'time') == task_time:
            os.system(config.get('task', 'command'))
        