#!/usr/bin/env python
#########################################################
# Copyright 2021 Cisco Systems, Inc.
# All rights reserved.
#
# CLI Extensions for show command
#########################################################

try:
    import click
    import yaml
    from show import platform
    from sonic_py_common import device_info
    import utilities_common.cli as clicommon
except ImportError as e:
    raise ImportError("%s - required module not found" % str(e))

PLATFORM_PY = '/opt/cisco/bin/platform.py'

@click.command()
def inventory():
    """Show Platform Inventory"""
    args = '{} inventoryshow'.format(PLATFORM_PY)
    clicommon.run_command(args)

@click.command()
def idprom():
    """Show Platform Idprom Inventory"""
    args = '{} idprom'.format(PLATFORM_PY)
    clicommon.run_command(args)

def register(cli):
    version_info = device_info.get_sonic_version_info() 
    if (version_info and version_info.get('asic_type') == 'cisco-8000'):
        cli.commands['platform'].add_command(inventory)
        cli.commands['platform'].add_command(idprom)
