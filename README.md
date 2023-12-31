# WellCome To Aptinet Cart

## Configs:
### Raspberry pi configs:
sudo raspi-config
enable auto login to console
enable ssh
enable legacy camera
enable i2c
enable serial

### DNS:
Set static DNS:
sudo nano /etc/dhcpcd.conf
add following line: (uncomment existing line and edit DNSs)
static domain_name_servers=8.8.8.8 4.2.2.4

cd /etc/wpa_supplicant/
sudo chown aptinet:aptinet wpa_supplicant/

## Install Required Packages:
sudo apt-get update

### Install Git:
sudo apt-get install git

### install pip:
sudo apt-get install python3-pip

### pyserial
sudo pip3 install pyserial

### smbus
pip3 install smbus

### install opencv

[//]: # (sudo apt-get install python3-opencv)
pip3 install opencv-python

### sound
sudo apt-get install alsa-utils pulseaudio

### email validator
pip3 install email-validator

[//]: # (### camera:)

[//]: # (sudo apt-get install gstreamer1.0-tools )

[//]: # (sudo apt-get install gstreamer1.0 )

[//]: # (sudo apt-get install libgstreamer-plugins-bad1.0-dev )

[//]: # (sudo apt-get install libgstreamer-plugins-base1.0-dev )

[//]: # (sudo apt-get install gstreamer1.0-plugins-bad )

[//]: # (sudo apt-get install python3-pyqt5.qtmultimedia)

[//]: # (pip install qimage2ndarray)

[//]: # (sudo apt install libqt5multimedia5-plugins)

[//]: # (sudo apt-get install libx264-dev libjpeg-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3)

[//]: # (sudo apt-get install vlc)

[//]: # ()
[//]: # (#### if you have Qt5 install this plugin)

[//]: # (sudo apt-get install gstreamer1.0-qt5)

[//]: # ()
[//]: # (#### install if you want to work with audio)

[//]: # (sudo apt-get install gstreamer1.0-pulseaudio)

### other required packages:
sudo apt-get install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns
sudo apt-get install qtdeclarative5-* qml-module-qtquick* qtquickcontrols5-* qml-module-qtquick2

### NFC
#### Bus 001 Device 003: ID 072f:226b Advanced Card Systems, Ltd WalletMate Dual Reader
#### look at:
https://www.mutek.com/mutek-pcsc-readers-pcsc-lite-linux/
#### and read readme file in DB/NFC

#### Install PC/SC-Lite and PCSC Tools on Raspberry Pi(Raspbian).
sudo apt-get install libusb-dev libusb++
sudo apt-get install libccid
sudo apt-get install pcscd
sudo apt-get install libpcsclite1
sudo apt-get install libpcsclite-dev
sudo apt-get install libpcsc-perl
sudo apt-get install pcsc-tools
sudo apt-get update

#### Update PC/SC Info.plist (Important!)
##### PCSC-Lite Info.plist file stores all verified PC/SC readers.
##### Readers from MUTEK or small vendors is not included in Info.plist, so vid/pid and reader description should be appended manually. This is the most ignoble
##### Firstly plug the reader to the USB port and:
##### lsusb to list all connected usb devices. MUTEK readers usually starts with 4143(vid) with a PID name(3901, 3500 etc.).
##### sudo find / -name Info.plist to find out the location of the Info.plist, which may be as /usr/local/lib/pcsc/drivers/ifd-ccid.bundle/Contents/Info.plist. File position may vary # for different Linux/Unix releases.
##### Edit the Info.plist and add the vid/pid/description under the respected key arrays, structure as in quoted text.
##### Reboot！
<key>ifdVendorID</key>
  <array>
      …
      <string>0x4143</string>
  </array>
<key>ifdProductID</key> 
  <array>
      …
      <string>0x3901</string>
  </array>
 <key>ifdFriendlyName</key>
  <array>
      …
      <string>MUTEK PT3901-2 PCSC Reader</string>
  </array>

# Info.plist with respective elements added to the end of each array. ifdVendorID and ifdProductID must follow the reader information from lsusb. ifdFriendlyName can be whatever # # strings you like.
# Testing
# Now you can start testing the PC/SC reader plugged. Two major commands are applied:

# pcsc_scan to list all readers and update reader status when card is inserted or removed.
# scriptor to operate card reader and transmit APDU commands.

sudo apt install -y python3-pip pcscd pcsc-tools libpcsclite-dev python3-pyscard python3-cmd2 libusb-1.0-0-dev


### LCD:
cd /home/
sudo git clone https://github.com/waveshare/Waveshare-DSI-LCD
cd Waveshare-DSI-LCD
cd 6.1.21
cd 64
sudo bash ./WS_xinchDSI_MAIN.sh 101C I2C1
sudo reboot






https://scribles.net/silent-boot-on-raspbian-stretch-in-console-mode/
https://www.youtube.com/watch?v=m3rfls00OtY