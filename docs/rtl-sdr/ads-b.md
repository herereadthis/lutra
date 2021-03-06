# ADS-B

* <strong>ADS-B (Automatic Dependent Surveillance-Broadcast)</strong> - modern aircraft have a transponder which broadcasts (at 1090Mhz frequency) location and altitude to air traffic controllers
* We can get this via RTL-SDR

### Repositories

* ~~[ADS-B Exchange](https://github.com/jprochazka/adsb-exchange)~~ - Don&rsquo;t trust this garbage
* [ADS-B Receiver](https://github.com/jprochazka/adsb-receiver)
* [PiAware](https://github.com/flightaware/piaware)

### Installation

* <em>(Up-to-date as of 2019-02-19)</em>
* Have a Raspberry Pi ready with Raspbian Buster
  ```bash
  wget -S https://downloads.raspberrypi.org/raspbian_latest -O raspbian.zip
  ```
* Get PiAware
  ```bash
  wget http://flightaware.com/adsb/piaware/files/packages/pool/piaware/p/piaware-support/piaware-repository_3.6.3_all.deb
  sudo dpkg -i piaware-repository_3.6.3_all.deb
  ```

* This gist seems very comprehensive:
  [rpi-adsb-feeder.md](https://gist.github.com/kanchudeep/2068aa149b1f787f8f77d7b785de304a)

https://discussions.flightaware.com/t/piaware-sd-card-image-3-7-1-quickstart-guide/48262

* these instructions not confirmed to be working

```bash
# Install 'lighttpd':
sudo apt install lighttpd
# Install 'dump1090-mutability' dependencies
sudo apt install libjs-excanvas libjs-jquery-ui libjs-jquery-ui-theme-smoothness librtlsdr0
# Download and install
# dump1090-mutability Debian packages at
# https://packages.debian.org/buster/dump1090-mutability
wget  http://ftp.us.debian.org/debian/pool/main/d/dump1090-mutability/dump1090-mutability_1.15~20180310.4a16df3+dfsg-6_armhf.deb
sudo dpkg -i dump1090-mutability_1.15~20180310.4a16df3+dfsg-6_armhf.deb
# Install prompt: Start automatically? Select YES
# Fix dump1090-mutability service not working by default, due to missing udev rules:
sudo wget -O /etc/udev/rules.d/rtl-sdr.rules "https://raw.githubusercontent.com/osmocom/rtl-sdr/master/rtl-sdr.rules"
# Enable dump1090-mutability site (may already be enabled)
sudo lighttpd-enable-mod dump1090
# Flightradar 24 Install (not working yet)
# sudo apt-get install fr24feed
# Flightaware Install
wget http://flightaware.com/adsb/piaware/files/packages/pool/piaware/p/piaware-support/piaware-repository_3.7.1_all.deb
sudo dpkg -i piaware-repository_3.7.1_all.deb
sudo apt update
sudo piaware-config flightaware-user "USERNAME"
piaware-config flightaware-password "PASSWORD"
sudo systemctl restart piaware
```

### potential shopping list

* The basic flow is:
  * power + ethernet > Raspberry Pi > USB extension cable > RTL-SDR dongle - grounding block / surge protector > antenna cable > antenna
* Any price listed was accurate at time of writing. Who knows now?

* (Optional) A POE Switch
  * [TRENDnet 4xPoE+ / 2xNon Switch, 60W](https://www.amazon.com/dp/B0152WZRBM/) - Amazon, $38
  * POE splitter, multiple options:
    [UCTRONICS Micro USB PoE Splitter](https://www.amazon.com/dp/B01MDLUSE7/) |
    [ANVISION 2-Pack 5V 2.4A PoE Splitter](https://www.amazon.com/dp/B079D5452Z/) |
    [PLUSPOE Micro USB PoE Splitter ](https://www.amazon.com/dp/B075CQRX2H/)
* Raspberry Pi 3B
* RTL-SDR Dongle: [FlightAware Pro Stick Plus ADS-B USB Receiver with Built-in Filter](https://www.amazon.com/dp/B01M7REJJW/) - $20
* The grounding block and SMA end of the antenna cable should be inside a junction box.
  * [Junction Box](https://www.amazon.com/dp/B0719TB8TM/) - various sizes and prices
  * [PG11 Waterproof Cable Glands Connectors](https://www.amazon.com/dp/B00843UH4O/) - these are for sending wires into the box
* If the cable is N-Type to N-Type:
  * Cable Option: [Times Microwave LMR400 Cable](https://www.amazon.com/dp/B01N3CA5Y7/) | [Custom Cable Connection Coaxial Cable LMR-400](https://www.amazon.com/dp/B01N4M0DMH/)
  * Surge protector: [Lightning arrestor N Female to Female 50 Ohm Lightning Surge Protector](https://www.amazon.com/dp/B0751CCQN7/)
  * Combine surge protector and cable: [400-Series N-Male to N-Male In-Line Lightning Protector Cable Assemblies](http://www.l-com.com/surge-protector-400-series-n-male-to-n-male-in-line-lightning-protector-cable-assemblies)
  * N-Male to N-SMA adapter. Options: [JEFA Tech Adapter](https://www.amazon.com/dp/B001GUSCH6/) | [Phonetone N male to SMA female](https://www.amazon.com/dp/B00KL6PXMI/)
* If the cable is N-Type to SMA:
  * Cable option: [MPD Digital LMR-400 Coaxial Antenna Cable Line with N Male & SMA Male Connectors](https://www.amazon.com/dp/B00H9II8I2/) - (1ft, can also be a jumper between n-type surge protector to dongle
  * Surge protector for the SMA end: [SMA Lightning Arrestor Surge Protector SMA Male to SMA Female](https://www.amazon.com/dp/B07K25Y1JW/)
* Antenna Mounting assembly
  * [CHANNEL MASTER CM-3090 Universal J-Mount](https://www.amazon.com/dp/B000BSIABM) - antenna mount along fascia of house
  * [Everbilt 1-3/4 in. Stainless-Steel Clamp](https://www.homedepot.com/p/202309386) - to manage wires on mast - $1.10 each
  * [10 Gauge Copper ground wire](https://www.amazon.com/dp/B008OILG5I)

* [FlightAware 1090 MHz ADS-B Antenna](https://www.amazon.com/dp/B00WZL6WPO/) - $40

## Sources

* [ADS-B FlightAware Enclosure Build](https://imgur.com/gallery/dpyGo) - and [reddit discussion](https://www.reddit.com/r/RTLSDR/comments/7pkso6/)
* [My ADS-B Setup - PiAware](https://www.reddit.com/r/ADSB/comments/akk01c/)
* [Do you want to build your own FlightAware PiAware ADS-B Ground Station?](https://flightaware.com/adsb/piaware/build)

