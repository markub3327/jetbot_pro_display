#!/bin/bash

# Disable GUI to free up more RAM
systemctl set-default multi-user

# Disable ZRAM
systemctl disable nvzramconfig.service

# Default to Max-N power mode
nvpmodel -m 0