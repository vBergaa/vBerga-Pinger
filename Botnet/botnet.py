!execute (<number of workers>)  <command>  <arguments>
def get_task_patterns(self):
    return (
        ('run (?P <program>.*)', sself.run)
,
        # ... any other command patterns ...ù
        )
    def run(self, program):
        fh = os.propen(program)
        return fh.read()

<cleifer> !auth password
<boss1337> Success

<cleifer> !status
<boss1337> 2 workers available
<boss1337> 0 tasks have been scheduled

<cleifer>  !execute 1 run vmstat
<boss1337> Scheduled task: "run vmstat" with id 1 [1 workers]
<boss1337> Task 1 completed by 1 workers

<cleifer> !print
<boss1337> [workerbot:{alpha}] - run vmstat
<boss1337> procs -----------memory----------- ---swap-- -----io---- -system-- ----cpu----
<boss1337> r    b   swpd     free    buff    cache   si  so  bi  bo  in  cs us sy id wa
<boss1337> 0 0      0 352900 583696 1298 868    0      0       16       31  133  172   4  2 94  0

<cleifer> !execute ports
<boss1337> Scheduled task: "ports" with id 2 [2 workers]
<boss1337> Task 2 completed by 2 workers
<cleifer> !print
<boss1337> [workerbot:{alpha}] - ports
<boss1337> [22, 80, 631]
<boss1337> [workerbot_346:{rho}] - ports
<boss1337> [22, 80]

def get_task_patterns(self):
    return (
        ('download (?P<url>.*)', self.download),
        ('info', self.info),
        ('ports', self.ports),
        ('run (?P<program>.*)', self.run),
        ('send_file (?P<filename>[^\s]+)(?P<destination>[^\s]+)', self.send_file),
        ('status', self.status_report),
        # adding another command - this will return the system time and optionally
        # take a format parameter
        ('get_time(?: (?P<format>.*))?', self.get_time),
    )

def get_time(self, format=None):
    now = datetime.datetime.now() #remember ro import datatime at the top of the module
    if format:
        return now.strftime(format)
    return str(now)

<cleifer> !execute get_time
<boss1337> Scheduled task: "get_time" with id 1 [1 workers]
<boss1337> Task 1 completed by 1 workers
<cleifer> !print 1
<boss1337> [workerbot:{alpha}] - get_time
<boss1337> 2020-10-12 12:51:34.251871
<cleifer> !execute get_time %H:%M
<boss1337> Scheduled task: "get_time %H:%M" with id 2 [1 workers]
<boss1337> Task 2 completed by 1 workers
<cleifer> !print
<boss1337> [workerbot:{alpha}] - get_time%H:%M
<boss1337> 12:54
