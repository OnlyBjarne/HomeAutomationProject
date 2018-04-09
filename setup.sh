
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
echo "Installing required modules"

pip install flask
pip install python-yr
pip install paho-mqtt
pip install PyYAML
pip install python-crontab

echo "Modules installed! Press enter to exit..."
read
exit