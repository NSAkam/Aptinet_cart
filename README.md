# WellCome To AptinetCart

## Configs:
### LCD:
cd /home/
git clone https://github.com/waveshare/Waveshare-DSI-LCD
cd Waveshare-DSI-LCD
cd 6.1.21
cd 64
sudo bash ./WS_xinchDSI_MAIN.sh 101C I2C0
sudo reboot

### DNS:
Set static DNS:
sudo nano /etc/dhcpcd.conf
add following line: (uncomment existing line and edit DNSs)
static domain_name_servers=8.8.8.8 4.2.2.4

### install pip:
sudo apt-get update
sudo apt-get install python3-pip

### install opencv
sudo apt-get install python3-opencv

### camera:
enable legacy camera through raspi-config

## required packages:
sudo apt-get install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns python3-pyside2uic
sudo apt-get install qtdeclarative5-* qml-module-qtquick* qtquick1-* qtquickcontrols5-* qml-module-qtquick2

pip3 install smbus
sudo pip3 install pyserial
