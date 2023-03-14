#!/usr/bin/env python3

# router object some values with default values, some without
class dc_switch(object):
    def __init__(self, hostname=None, os=None, device_type='cisco_ios'):
        self.hostname = hostname
        self.os = os
        self.device_type = device_type
        self.interfaces = 48


def test_defaults():
    d1 = dc_switch()
    assert d1.hostname == None
    assert d1.os == None
    assert d1.device_type == 'cisco_ios'
    assert d1.interfaces == 48


def test_non_defaults():
    d2 = dc_switch(hostname='lax-cor-r1', os='nxos', device_type='cisco_nxos')
    assert d2.hostname == 'lax-cor-r1'
    assert d2.os == 'nxos'
    assert d2.device_type == 'cisco_nxos'
    assert d2.interfaces == 48
