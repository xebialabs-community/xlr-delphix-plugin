import sys
from com.xebialabs.xlrelease.plugin.overthere import RemoteScript


mytemplate=open('ext/delphix/./run-pl-command.template.sh','r')
#data=mytemplate.readlines()
data = "".join(mytemplate.readlines()[0:])
print "------------------"
print mytemplate
print "-----------------"
print data
print "------------------"
config = {'serverDelphix':serverDelphix,
        'sourceDatabaseName':sourceDatabaseName,
        'targetDatabaseName':targetDatabaseName,
        'groupName':groupName,
        'targetName':targetName,
        'databaseType':databaseType,
        'DB_HOME':DB_HOME}

print config
print "--------"
print data.format(**config)
print "-assign"
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

