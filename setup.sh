echo 'NetShell Raffy Reader Installer';

echo 'Checking for "spi_bcm2835" using: lsmod | grep spi...';
lsmod | grep spi_bcm2835;

echo 'You must have enabled Interfaces -> SPI. Open configuration?';

select yn in "Yes" "No"; do
    case $yn in
        Yes ) read -p 'Rebooting afterwards. Press ENTER and re-run the script if SPI is enabled..'; sudo raspi-config; sudo reboot; break;;
        No )
		echo 'Skipping interface configuration.';

		echo 'Installing Python...';
		sudo apt-get install python3-dev python3-pip;

		echo 'Installing dependencies...';
		sudo pip3 install spidev;
		sudo pip3 install mfrc522;

		echo 'Done!';
    esac
done

