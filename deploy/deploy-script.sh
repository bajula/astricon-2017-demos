#!/bin/bash
echo "Running file: $0" > /tmp/startup_result.txt

echo """
#!/bin/bash
#### YOUR SCRIPT STARTS HERE ####
cd /tmp
yum install -y gcc

wget https://raw.githubusercontent.com/orpolaczek/Stanley/fix_silent_install/deploy-asterisk.sh # https://raw.githubusercontent.com/GreenfieldTech/Stanley/master/deploy-asterisk.sh
chmod +x deploy-asterisk.sh
./deploy-asterisk.sh > /tmp/asterisk_deploy_result.txt

#### YOUR SCRIPT ENDS HERE ####
""" > /tmp/one_time_deployment.sh
chmod +x /tmp/one_time_deployment.sh
/tmp/one_time_deployment.sh &

echo "" > $0
echo "Truncated file: $0" >> /tmp/startup_result.txt