#!/usr/bin/python3

# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Copyright (c) 2024 UPTI FPV UCM
# Author: Martin Kubovcik

import subprocess
import getpass
import os
import shutil

STATS_SERVICE_TEMPLATE = """
[Unit]
Description=JetBot Pro display service

[Service]
Type=simple
User=%s
ExecStart=/bin/sh -c "python3 /opt/jetbot_pro_display/display.py"
WorkingDirectory=%s
Restart=always

[Install]
WantedBy=multi-user.target
"""

STATS_SERVICE_NAME = "jetbot_pro_display"

# Pre-install steps
subprocess.check_output("apt install python3-smbus python3-pil", shell=True)

def get_stats_service():
    return STATS_SERVICE_TEMPLATE % (getpass.getuser(), os.environ["HOME"])


if __name__ == "__main__":
    FILE_NAME = "jetbot_pro_display.service"

    with open(FILE_NAME, "w") as f:
        f.write(get_stats_service())

    # move to systemd
    shutil.move(FILE_NAME, os.path.join("/etc/systemd/system", FILE_NAME))

    # enable service at startup
    subprocess.check_output("systemctl enable jetbot_pro_display", shell=True)

    # start service
    subprocess.check_output("systemctl start jetbot_pro_display", shell=True)
