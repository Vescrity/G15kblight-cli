# G15kblight-cli

## Overview
G15kblight-cli is a command-line utility designed for controlling the keyboard backlight effects on Dell G15 laptops under Linux. **This project is forked from [cemkaya-mpi/Dell-G15-Controller](https://github.com/cemkaya-mpi/Dell-G15-Controller)**.  

The core code is consistent with the original project.  

Untested on any other laptop, but keyboard part can most likely be used with models that have the ```Bus *** Device ***: ID 187c:0550 Alienware Corporation LED controller```. 

By default, leds will flash red on low battery, and have half brightness on battery.

Only static color and morph is supported at this time. 

**Use at your own risk.**

## Installation

### Arch Linux

[`pkg/PKGBUILD`](pkg/PKGBUILD)

```bash
cd pkg
makepkg -si
```

### Others

No installation necessary, besides installing python dependencies.

## Dependencies

- python-pyusb

## Usage

```
G15kblight-cli -h
```

#### Example

```
# set static color
G15kblight-cli -s 0x7733FF
# set morth color
G15kblight-cli -m 0x7733FF
# set static and morth color and duration
G15kblight-cli -s 0x7733FF -m 0x7733FF -t 555
```

## License
GNU GENERAL PUBLIC LICENSE v3

## Contributions
Written using the information and code from https://github.com/trackmastersteve/alienfx/issues/41. 

Many thanks to @AlexIII and @T-Troll for their help with the ACPI calls.

