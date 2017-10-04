#!/bin/bash
echo "Running file: $0" > /tmp/startup_result.txt

echo """
#!/bin/bash
#### YOUR SCRIPT STARTS HERE ####
cd /tmp
yum update -y
yum install -y gcc git

# install docker
tee /etc/yum.repos.d/docker.repo <<-'EOF'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF
yum update -y
yum install docker-engine -y
service docker start

# Enable docker on boot
chkconfig docker on
systemctl enable docker

mkdir /home/docker-asterisk
cd /home/docker-asterisk
git clone https://github.com/orpolaczek/seconf-2017-demo.git
cd seconf-2017-demo
git checkout work_in_progress
cd phonecalls
cd asterisk
chmod +x build.sh
./build.sh > /tmp/docker_build_result.txt

#### YOUR SCRIPT ENDS HERE ####
""" > /tmp/one_time_deployment.sh
chmod +x /tmp/one_time_deployment.sh
/tmp/one_time_deployment.sh > /tmp/one_time_deploy_result.txt &

echo "" > $0
echo "Truncated file: $0" >> /tmp/startup_result.txt