# garbagecollector
test
[![Circle CI](https://circleci.com/gh/cleanerbot/garbagecollector.png?circle-token=89001b8338b393fc8199afcc6ffc9672511fd472)](https://circleci.com/gh/cleanerbot/garbagecollector/tree/master 'View CI builds')

### Dependency check

In order to use this script you will need to download:
http://xael.org/norman/python/python-nmap/

For simplicty, run the get-nmap-package.sh script to handle the pull and setup

step 1:
download python-nmap dependency and run setup.py 

step 2: 
add networks that you wish to scan to scripts/seeds/net_seed.txt
in format:
```
netblock1,192.168.1.0/24
netblock2,127.0.0.0/24
```
# Configuration

Populate configuration file in scripts/resources/config.yaml

Example:
```yaml
Credentials:       
        LDAP:
                User: jsmith
                Password: 123password
        Github:
                User: jsmith3000
                Password: password123
                
Git_Repo:
        Repo_Name: hello-world
        Repo_Owner: octocat
        
LDAP_Settings:
        Base_DN: 'OU=Org,DC=example,DC=com'
```

# Command Line Arguments

Flag | Usage | Description | Required 
---- | ----- |-------- | ---
-a, --adseed | -a /path/to/file.txt | optionally specify Active Directory seed file | No 
-b, --block | -b 127.0.0.0/24 | optionally scan a single network |No
-c, --csvfile | -c /path/to/file.csv| optionally output results to a csv file | No
-n, --netfile | -n /path/to/file.txt| optionally specify Network seed file |No

# Seeds

Seed files are used to identify networks to be scanned and Active Directory servers to check against

default seed files located in scripts/seeds

seed file format:
```
Description,Value
Description,Value
Description,Value
```

Examples:

net_seed.txt
```
local,127.0.0.0/24
random network,124.43.24.0/24
```

ad_seed.txt
```
server A,AD_Server01
server B,AD_Server02.example.server.com
```




