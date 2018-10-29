# pi
Smart home 

## Documentation



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

## Install Influxdb

https://docs.influxdata.com/influxdb/v1.6/introduction/installation/

sudo apt-get update && sudo apt-get install influxdb

