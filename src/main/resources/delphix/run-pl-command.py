import sys
from com.xebialabs.xlrelease.plugin.overthere import RemoteScript


mytemplate=open('ext/delphix/./run-pl-command.template.sh','r')
data = "".join(mytemplate.readlines()[0:])
config = {'serverDelphix':serverDelphix,
        'sourceDatabaseName':sourceDatabaseName,
        'targetDatabaseName':targetDatabaseName,
        'groupName':groupName,
        'targetName':targetName,
        'databaseType':databaseType,
        'dxToolkitHome':dxToolkitHome,
        'dxToolkitScript':dxToolkitScript,
        'DB_HOME':DB_HOME}

#print config
print data.format(**config)
task.pythonScript.setProperty('script', data.format(**config))

script = RemoteScript(task.pythonScript)
exitCode = script.execute()

output = script.getStdout()
err = script.getStderr()

if (exitCode == 0):
    print output
else:
    print "Exit code "
    print exitCode
    print
    print "#### Output:"
    print output

    print "#### Error stream:"
    print err
    print
    print "----"

    sys.exit(exitCode)

