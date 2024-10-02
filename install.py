#!/usr/bin/python3

# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Copyright (c) 2024 UPTI FPV UCM
# Author: Martin Kubovcik

import argparse
import getpass
import os

STATS_SERVICE_TEMPLATE = """
[Unit]
Description=JetBot Pro display service

[Service]
Type=simple
User=%s
ExecStart=/bin/sh -c "python3 /opt/jetbot_pro/display.py"
WorkingDirectory=%s
Restart=always

[Install]
WantedBy=multi-user.target
"""

STATS_SERVICE_NAME = "jetbot_pro_display"

# Pre-install steps
# apt install python3-smbus python3-pil

def get_stats_service():
    return STATS_SERVICE_TEMPLATE % (getpass.getuser(), os.environ['HOME'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='jetbot_pro_display.service')
    args = parser.parse_args()

    with open(args.output, 'w') as f:
        f.write(get_stats_service())