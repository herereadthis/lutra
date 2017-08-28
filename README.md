# LUTRA!

[![Build Status](https://travis-ci.org/herereadthis/lutra.svg?branch=master)](https://travis-ci.org/herereadthis/lutra)

![Raspberry Pi](https://raw.githubusercontent.com/herereadthis/lutra/master/resources/images/raspberry_pi_64x64.png)

This repo is for me to keep track of whatever I'm doing with my Raspberry Pi.

## Run this first

```bash
# get a bunch of files
python3 download_stuff.py
```

## Documentation

### Coding and Software

* [Do these things first](https://github.com/herereadthis/lutra/blob/master/docs/do_first.md) when you get a Raspberry Pi
* [Useful terminal commands](https://github.com/herereadthis/lutra/blob/master/docs/terminal_commands.md) - including how to turn off a Pi
* [How to schedule tasks](https://github.com/herereadthis/lutra/blob/master/docs/scheduling.md) when booting up or periodically (cron)
* [Advanced Configuration](https://github.com/herereadthis/lutra/blob/master/docs/advanced_config.md)
* [SD Cards](https://github.com/herereadthis/lutra/blob/master/docs/sd_cards.md) - Flashing Raspbian, and restoring an image
* [Set up Github](https://github.com/herereadthis/lutra/blob/master/docs/github_setup.md) to get and share code
* [Docker](https://github.com/herereadthis/lutra/blob/master/docs/docker.md) containers for shipping code
* [NodeJS and NPM](https://github.com/herereadthis/lutra/blob/master/docs/node_js.md) installation and usage
* [Python Virtual Environments](https://github.com/herereadthis/lutra/blob/master/docs/virtualenv.md) for isolating dependencies
* [RTL-SDR](https://github.com/herereadthis/lutra/blob/master/docs/rtl_sdr.md) - Software Defined Radio

### Sensors and Circuitry

* [GPIO Pinout](https://github.com/herereadthis/lutra/blob/master/docs/GPIO.md) - diagram of all the pins on the RPi
* [How to wire MCP3008](https://github.com/herereadthis/lutra/blob/master/docs/MCP3008.md) - analogue-to-digital converter (ACD)
  * [HC-SR04](https://github.com/herereadthis/lutra/blob/master/objectives/hc_sr04) - an ultrasonic distance sensor
* [PIR](https://github.com/herereadthis/lutra/blob/master/objectives/PIR_motion_sensor) - passive infrared motion sensor
* [I<sup>2</sup>C](https://github.com/herereadthis/lutra/blob/master/docs/I2C.md) - communication protocol using `SDA` and `SCL` pins
  * [MPU-6050 Gyroscope + Accelerometer](https://github.com/herereadthis/lutra/blob/master/objectives/MPU6050_accelerometer) - 3-axis
  * [LCD Screen](https://github.com/herereadthis/lutra/blob/master/objectives/i2c_lcd) - includes 16x2 and 20x4
* [DS18B20](https://github.com/herereadthis/lutra/blob/master/objectives/DS18B20_thermometer) thermometer sensor
* [ST7735 SPI LCD](https://github.com/herereadthis/lutra/blob/master/docs/st7735.md), a 1.8" TFT display module
* [Antenna Appendix](https://github.com/herereadthis/lutra/blob/master/docs/antennas.md) supplemental info for setting up antennas
* [MAX98357](https://github.com/herereadthis/lutra/blob/master/docs/MAX98357.md) class D amplifier
* [Relay Modules](https://github.com/herereadthis/lutra/blob/master/objectives/relay) to control AC powered devices