# Requirements

You need to install the following tools to execute this sample

* [Vagrant 1.3](http://docs.vagrantup.com/v2/installation/index.html)
* [Ansible 1.3](http://www.ansibleworks.com/docs/gettingstarted.html)
* [Fabric 1.8](http://docs.fabfile.org/en/1.7/#installation)

# Setup

```
$ git clone https://github.com/nulab/fabric-sample.git
$ cd fabric-sample
$ vagrant up
$ vagrant ssh-config > ssh.config
```

# Run sample tasks

List defined tasks.
```
$ fab -l
Available commands:

    deploy              clean work directory before deploy
    nginx_restart       service nginx restart
    nginx_start         service nginx start
    nginx_stop          service nginx stop
    postgresql_restart  service postgresql restart
    postgresql_start    service postgresql start
    postgresql_stop     service postgresql stop
    show_args           show args
    simple              show uname -a
    switch              switch task
    tomcat7_restart     service tomcat7 restart
    tomcat7_start       service tomcat7 start
    tomcat7_stop        service tomcat7 stop
```

Run a specific task.
```
$ fab nginx_start
```

Login to vagrant host
```
$ vagrant ssh
```
