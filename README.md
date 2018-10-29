# pi
Smart home 

## Documentation

http://docs.grafana.org/guides/getting_started/

https://docs.influxdata.com/influxdb/v1.6/introduction/getting-started/


## Setup

### Raspberry Pi

OS: Ubuntu Mate (https://ubuntu-mate.org/raspberry-pi/)

$ sudo apt update 
$ sudo apt upgrade -y

## Install grafana

http://docs.grafana.org/installation/debian/

APT Repository
Add the following line to your /etc/apt/sources.list file.

deb https://packagecloud.io/grafana/stable/debian/ stretch main

Then add the Package Cloud key. This allows you to install signed packages.

curl https://packagecloud.io/gpg.key | sudo apt-key add -

Update your Apt repositories and install Grafana

sudo apt-get update
sudo apt-get install grafana

Connect to http://localhost:3000/
and login as admin / admin

## Install Influxdb

https://docs.influxdata.com/influxdb/v1.6/introduction/installation/

sudo apt-get update && sudo apt-get install -y influxdb influxdb-client

Connect to http://localhost:8083

## Python libraries

Note: do no run following command
pip3 install --upgrade pip

In case you run it, run command below to revert to revert to pip 8.1.1
python3 -m pip install --user --upgrade pip==8.1.1

pip3 install pyHS100
pip3 install phue
pip3 install influxdb
pip3 install schedule

TPLink smart plugs/switches and smart bulbs 
https://github.com/GadgetReactor/pyHS100

Philips Hue
https://github.com/studioimaginaire/phue

Influxdb
https://github.com/influxdata/influxdb-python

Schedule
https://github.com/dbader/schedule



