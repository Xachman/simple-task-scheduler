import argparse
import configparser
import os
import subprocess
import io
import datetime

now = datetime.datetime.now()

parser = argparse.ArgumentParser(description='Simple Task Scheduler')
parser.add_argument('time', type=str,
                    help='task time that you are using')
parser.add_argument('-d', '--directory', type=str,
                    help='directory that configs are loaded from')

parser.add_argument('-l', '--log', type=str,
                    help='log file to output logs to')
args = parser.parse_args()

task_time = args.time
start_directory = args.directory
log_file = args.log

if start_directory is None:
    start_directory = "/etc/simple-task-scheduler"

if log_file is None:
    log_file = '/var/simple-task-scheduler.log'

def log(type, message):
    f = open(log_file, 'a+')
    l_time = now.strftime("%Y-%m-%d %H:%M:%S")
    for line in message.splitlines():
        if line.strip() == "":
            continue
        f.write('['+type+' '+l_time+'] '+line+"\n")
    f.close()


directory = start_directory+"/conf.d"
for filename in os.listdir(directory):
    if filename.endswith(".conf"):
        config = configparser.RawConfigParser()
        config.read(directory+"/"+filename)

        if config.get('task', 'time') == task_time:
            result = subprocess.run(config.get('task', 'command').split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.stderr:
                log('error', result.stderr.decode('utf-8'))
            else:
                log('info', result.stdout.decode('utf-8'))



