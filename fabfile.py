#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import env, run, sudo, task, execute
from fabric.tasks import Task
from fabric.colors import red, yellow

import time

env.use_ssh_config = True
env.ssh_config_path = 'ssh.config'
env.hosts = ['default']

@task
def simple():
    """
    show uname -a
    """
    run('uname -a')

class DeployTask(Task):
    """
    deploy application
    """
    name = 'deploy'

    def run(self, *args, **kwargs):
        execute('tomcat7_stop')
        self.pre_deploy()        
        print yellow('do deploy')
        self.post_deploy()
        execute('tomcat7_start')        

    def pre_deploy(self):
        pass

    def post_deploy(self):
        pass

class CleanAndDeployTask(DeployTask):
    """
    clean work directory before deploy
    """
    def pre_deploy(self):
        print yellow('clean up /var/lib/tomcat7/work/')
        sudo('rm -fr /var/lib/tomcat7/work/*')

deploy = CleanAndDeployTask()

class Service(object):

    def __init__(self, name):
        self.name = name

    def start(self):
        sudo('service %s start' % self.name)

    def stop(self):
        sudo('service %s stop' % self.name)

    def restart(self):
        sudo('service %s restart' % self.name)

    def get_methods(self):
        return [self.start, self.stop, self.restart]


def create_tasks(name, namespace):

    service = Service(name)
    for f in service.get_methods():
        fname = f.__name__
        # task description
        f.__func__.__doc__ = 'service %s %s' % (name, fname)
        # task name
        task_name = '%s_%s' % (name, fname)
        wrapper = task(name=task_name)
        rand = '%d' % (time.time() * 100000)
        namespace['task_%s_%s' % (task_name, rand)] = wrapper(f)

create_tasks('nginx', globals())
create_tasks('postgresql', globals())
create_tasks('tomcat7', globals())

class FactoryTask(Task):

    def __init__(self, runners, desc=None, *args, **kwargs):
        super(FactoryTask, self).__init__(*args, **kwargs)
        self.runners = runners
        if desc is not None:
            self.__doc__ = desc  

    def run(self, *args, **kwargs):

        if not env.has_key('run_environment'):
            print red('this task should be run under some environment')
            return

        runner = self.runners.get(env.run_environment)
        if runner is None:
            print red('%s is not supported this task' % env.run_environment)
        else :
            print yellow('run %s under %s environment' % (self.name, env.run_environment))
            runner(*args, **kwargs)

def prod_run(a, b):
    print '%s %s' % (a, b)

def stage_run(a):
    print '%s' % a

@task
def switch(production=None):
    """
    switch task
    """
    if production is not None:
        env.run_environment = 'production'
    else:
        env.run_environment = 'stage'

show_args = FactoryTask({
    'production' : prod_run,
    'stage' : stage_run
}, 'show args', name='show_args')


