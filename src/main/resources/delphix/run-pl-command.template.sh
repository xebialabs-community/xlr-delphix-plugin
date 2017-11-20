export PERL_LIBRARY={dxToolkitHome}/lib

perl {dxToolkitHome}/bin/{dxToolkitScript} -d {serverDelphix} -sourcename "{sourceDatabaseName}" -dbname {targetDatabaseName} -targetname {targetDatabaseName} -group {groupName} -environment {targetName} -type {databaseType} -envinst "{DB_HOME}"



