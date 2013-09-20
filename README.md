# Requirements

You need to install the following tools to execute this sample

* [Vagrant](http://docs.vagrantup.com/v2/installation/index.html)
* [Ansible](http://www.ansibleworks.com/docs/gettingstarted.html)
* [Fabric](http://docs.fabfile.org/en/1.7/#installation)

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
```

Run a specific task.
```
$ fab nginx_start
```

Login to vagrant host
```
$ vagrant ssh
```
