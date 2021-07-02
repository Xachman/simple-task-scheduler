# Simple Task Scheduler 

A simple way of running multiple tasks in crons one after the other for a particular time.

## How to use

Create tasks in your config directory like this

```
[task]
time = daily
command = echo "hi!"
```

Then add a cron with the executable

```
0 0 * * * simple-task-scheduler daily -d /home/to/my/configs
```

Configs should go in /home/to/my/configs/conf.d.

Each config that has the time daily will be run.
