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
