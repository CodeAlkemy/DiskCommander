#!/usr/bin/python3
# Copyright (c) 2017 CodeAlkemy
"""Main file of the diskcmd"""
import datetime as dt
import platform as plat
import argparse
import sys
import json
import os
import disk
import msgpack

def main():
    # Setup
    file_handle = open('app_data.json', mode='r+')
    contents = file_handle.read(-1)
    app_data = json.loads(contents)
    parser = argparse.ArgumentParser(description='Commandant de disque (dc) - '+app_data['version'])
    parser.add_argument('mount', help='Mount a volume if not specified by -p mounting point will be /mnt/dev#', nargs='?')
    parser.add_argument('-d', '--disk', type=str, help='Action will be performed on this disk')
    parser.add_argument('-p', '--partition', type=int, help='Actions will be performed on this partition')
    parser.add_argument('-m', '--point', help="Specify a diferent parsering point", type=str)
    parser.add_argument('--flags', help='Flags to pass to the mounting command', type=str)
    parser.add_argument('--add-to-fstab', help='Add mounting to fstab to make this action persistent', action='store_true')
    parser.add_argument('unmount', help='Unmount a volume', nargs='?')
    parser.add_argument('format', help='Format the disk with the specified filesystem', nargs='?')
    parser.add_argument('-s0', '--file-system', choices=['ext4'], help='Format the partition specified')
    args = parser.parse_args()
    bitness = '64' if sys.maxsize > 2**32 else '32'
    now = dt.datetime.now()
    operating_system = plat.uname()
    mnt_list = []

    #Logic
    print('Commandant de disque -', app_data['version'] + ' ~ build ' + app_data['build'], 'on', operating_system[0], operating_system[2], bitness+'bits','\nCopyright (c) CodeAlkemy', now.year)
    if os.path.exists(app_data['mount_bank']):
        db = open(app_data['mount_bank'], mode='a+')

if __name__ == '__main__':
    main()