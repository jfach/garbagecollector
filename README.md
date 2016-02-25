# garbagecollector

[![Circle CI](https://circleci.com/gh/cleanerbot/garbagecollector?circle-token=89001b8338b393fc8199afcc6ffc9672511fd472)](https://circleci.com/gh/cleanerbot/garbagecollector/tree/master 'View CI builds')

### Dependency check

In order to use this script you will need to download:
http://xael.org/norman/python/python-nmap/

For simplicty, run the get-nmap-package.sh script to handle the pull and setup

step 1:
download python-nmap dependency and run setup.py 

step 2: 
add networks that you wish to scan to networks.txt
in format:
```
netblock1,192.168.1.0/24
netblock2,127.0.0.0/24
```

optionally specify file to use instead of networks.txt with --netfile flag:
```
python asset_collect.py -n netfile.txt
```

output results to csv with the --csvfile flag:
```
python asset_collect.py -c csv_file.csv
```
