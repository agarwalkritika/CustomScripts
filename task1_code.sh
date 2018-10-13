installed_status=`apt-cache policy apache2|grep "Installed: (none)" > /dev/null;echo $?`
#echo $installed_status
#installed_software=`apt-get install apache2; echo $?`
service_status=`service apache2 status|grep "Active: inactive" > /dev/null;echo $?`
#echo $service_status
ip1_address=`ifconfig enp0s8|grep "inet addr:" > /home/kritika/ip_addr;awk 'sub(/inet addr:/,""){print $1}' /home/kritika/ip_addr`
#echo $ip1_address
host_name=`hostname`
#echo $host_name
#echo $installed_software
if [ $installed_status -eq 0 ]
then
	apt-get install apache2
	echo "Apache2 is now installed"
else
	echo "apache2 is already installed"
fi
#if [ $installed_software ne  0 ]
#then
#	apt-get install apache2
#else
#	echo "apache2 is already installed"
if [ $service_status -ne 0 ]
then
	service apache2 stop
	echo "Apache2 is now stopped"
else 
	echo "Already in stop state"
fi
#Below command is used to change in code on runtime if particular string exists.
sed -i "s/x.x.x.x/${ip1_address}/g" /home/kritika/required_code/index.html
sed -i "s/####/${host_name}/g" /home/kritika/required_code/index.html
#awk -v "ip_address=$ip1_address" '{gsub(/x.x.x.x/,ip_address);print}' /home/kritika/required_code/index.html
#awk -v "host1_name=$host_name" '{gsub(/####/,host1_name);print}' /home/kritika/required_code/index.html
cp /home/kritika/required_code/index.html /var/www/html
service apache2 start	
