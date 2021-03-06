<div align="center">

## Things I have learned in developer operation (devops) roles

### Some of these are obvious, but some aren't

</div>

### Version control
---------------------------------------------

- Revert files back to a previous state.
- Revert the entire project back to a previous state.
- Compare changes over time.
- See who last modified something that might be causing a problem.
- Who introduced an issue and when.

#### Branching styles:

##### Feature branching
A feature branch model keeps all of the changes for a particular feature inside of a branch. 
When the feature is fully tested and validated by automated tests, the branch is then merged into master.
##### Task branching
In this model each task is implemented on its own branch with the task key included in the branch name. 
It is easy to see which code implements which task, just look for the task key in the branch name.
##### Release branching
Once the develop branch has acquired enough features for a release, you can clone that branch to form a Release branch. 
Creating this branch starts the next release cycle, so no new features can be added after this point, only bug fixes, documentation generation, and other release-oriented tasks should go in this branch.
Once it is ready to ship, the release gets merged into master and tagged with a version number. In addition, it should be merged back into develop branch, which may have progressed since the release was initiated.

#### Commit Hooks:

There are three ways to configure a script to run every time a repository receives new commits through push, one needs to define either a pre-receive, update, or a post-receive hook depending on when exactly the script needs to be triggered.

**Pre-receive hook** in the destination repository is invoked when commits are pushed to it. Any script bound to this hook will be executed before any references are updated.
This is a useful hook to run scripts that help enforce development policies.

**Update hook** works in a similar manner to pre-receive hook, and is also triggered before any updates are actually made. However, the update hook is called once for every commit that has been pushed to the destination repository.

Finally, **post-receive hook** in the repository is invoked after the updates have been accepted into the destination repository. This is an ideal place to configure simple deployment scripts, invoke some continuous integration systems, dispatch notification emails to repository maintainers, etc.

**Hooks are local to every Git repository and are not versioned**. Scripts can either be created within the hooks directory inside the “.git” directory, or they can be created elsewhere and links to those scripts can be placed within the directory.

### Jenkins

#### Results
[HtmlPublisher](https://wiki.jenkins.io/display/JENKINS/HTML+Publisher+Plugin) plugin is useful to publish the html reports that your build generates to the job and build pages.

#### Backups
To create a backup, all you need to do is to periodically back up your JENKINS_HOME directory. This contains all of your build jobs configurations, your slave node configurations, and your build history. To create a back-up of your Jenkins setup, just copy this directory. You can also copy a job directory to clone or replicate a job or rename the directory.

### Ansible 

**Controller Machine**: The machine where Ansible is installed, responsible for running the provisioning on the servers you are managing.

**Inventory**: An initialization file that contains information about the servers you are managing.

**Playbook**: The entry point for Ansible provisioning, where the automation is defined through tasks using YAML format. At a basic level, playbooks can be used to manage configurations of and deployments to remote machines.

**Task**: A block that defines a single procedure to be executed, e.g. Install a package.

**Module**: A module typically abstracts a system task, like dealing with packages or creating and changing files. Ansible has a multitude of built-in modules, but you can also create custom ones.

**Role**: A pre-defined way for organizing playbooks and other files in order to facilitate sharing and reusing portions of a provisioning.

**Play**: A provisioning executed from start to finish is called a play. In simple words, execution of a playbook is called a play.

**Facts**: Global variables containing information about the system, like network interfaces or operating system.
Handlers: Used to trigger service status changes, like restarting or stopping a service.

#### Useful Ansible commands
```
ansible -m setup hostname
```

### Nagios
#### Active checks
Active checks are initiated and performed by Nagios

- Active checks are initiated by the Nagios process.
- Active checks are run on a regularly scheduled basis.

#### Passive checks
They are initiated and performed by external applications/processes and the Passive check results are submitted to Nagios for processing.

Useful when:
- Asynchronous in nature and cannot be monitored effectively by polling their status on a regularly scheduled basis.
- Located behind a firewall and cannot be checked actively from the monitoring host.

### Selenium
Supports II types of testing:

**Regression Testing**: It is the act of retesting a product around an area where a bug was fixed.

**Functional Testing**: It refers to the testing of software features (functional points) individually.
