#!/usr/bin/env python3
#
# derived from https://devnet-pubhub-site.s3.amazonaws.com/media/pyats/docs/getting_started/index.html
#
from pyats.topology import loader

# load testbed
testbed = loader.load('testbed_1.yml')

# access the device
testbed.devices
s1 = testbed.devices['lax-edg-r1']

# establish connectivity
s1.connect()

# issue command
print(s1.execute('show version'))

# disconnect
s1.disconnect()

