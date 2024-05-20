# G15kblight-cli

## Overview
G15kblight-cli is a command-line utility designed for controlling the keyboard backlight effects on Dell G15 laptops under Linux. **This project is forked from [cemkaya-mpi/Dell-G15-Controller](https://github.com/cemkaya-mpi/Dell-G15-Controller)**.  

The core code is consistent with the original project.  

Untested on any other laptop, but keyboard part can most likely be used with models that have the ```Bus *** Device ***: ID 187c:0550 Alienware Corporation LED controller```. 

By default, leds will flash red on low battery, and have half brightness on battery.

Only static color and morph is supported at this time. 

**Use at your own risk.**

## Installation

No installation necessary, besides installing python dependencies, and creating the udev rule ```/etc/udev/rules.d/00-aw-elc.rules```, and rebooting. Make sure the user is part of the ```plugdev``` group. Alternatively, run the script as root (not recommended).

```
/etc/udev/rules.d/00-aw-elc.rules

SUBSYSTEM=="usb", ATTRS{idVendor}=="187c", ATTRS{idProduct}=="0550", MODE="0660", GROUP="plugdev", SYMLINK+="awelc"
```

## Depandencies

- python-pyusb

## Usage

## License
GNU GENERAL PUBLIC LICENSE v3

## Contributions
Written using the information and code from https://github.com/trackmastersteve/alienfx/issues/41. 

Many thanks to @AlexIII and @T-Troll for their help with the ACPI calls.

