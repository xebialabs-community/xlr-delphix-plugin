export PERL_LIBRARY=/u02/dxtoolkit/lib

perl dx_provision_vdb.pl -d {serverDelphix} -sourcename "{sourceDatabaseName}" -dbname {targetDatabaseName} -targetname {targetDatabaseName} -group {groupName} -environment {targetName} -type {databaseType} -envinst "{DB_HOME}"



