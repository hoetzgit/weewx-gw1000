"""
This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

                        Installer for GW1000 Driver

Version: 0.2.0b1                                      Date: 3 October 2020

Revision History
    3 October 2010      v0.2.0
        - added extractor for sensor signal level fields
        - use multiline string for [GW1000] config to allow comments to be
          included
    1 September 2020    v0.1.0b1
        - initial implementation
"""

# python imports
import configobj
from distutils.version import StrictVersion
from setup import ExtensionInstaller
try:
    # python 3
    from io import StringIO
except ImportError:
    # python 2
    from StringIO import StringIO

# WeeWX imports
import weewx


REQUIRED_VERSION = "3.7.0"
GW1000_VERSION = "0.2.0b1"
# define our config as a multiline string so we can preserve comments
gw1000_config = """
[GW1000]
    # This section is for the GW1000 WiFi gateway driver.

    # The driver to use:
    driver = user.gw1000
"""

# construct our config dict
gw1000_dict = configobj.ConfigObj(StringIO(gw1000_config))


def loader():
    return Gw1000Installer()


class Gw1000Installer(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires WeeWX %s or greater, found %s" % (''.join(('GW1000 driver ', GW1000_VERSION)),
                                                                 REQUIRED_VERSION,
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(Gw1000Installer, self).__init__(
            version=GW1000_VERSION,
            name='GW1000',
            description='WeeWX driver for GW1000 WiFi gateway.',
            author="Gary Roderick",
            author_email="gjroderick<@>gmail.com",
            files=[('bin/user', ['bin/user/gw1000.py'])],
            config={
                'GW1000': {
                    'driver': 'user.gw1000'
                },
                'Accumulator': {
                    'daymaxwind': {
                        'extractor': 'last'
                    },
                    'lightning_distance': {
                        'extractor': 'last'
                    },
                    'lightning_strike_count': {
                        'extractor': 'sum'
                    },
                    'lightning_last_det_time': {
                        'extractor': 'last'
                    },
                    'stormRain': {
                        'extractor': 'last'
                    },
                    'hourRain': {
                        'extractor': 'last'
                    },
                    'dayRain': {
                        'extractor': 'last'
                    },
                    'weekRain': {
                        'extractor': 'last'
                    },
                    'monthRain': {
                        'extractor': 'last'
                    },
                    'yearRain': {
                        'extractor': 'last'
                    },
                    'totalRain': {
                        'extractor': 'last'
                    },
                    'pm2_51_24hav': {
                        'extractor': 'last'
                    },
                    'pm2_52_24hav': {
                        'extractor': 'last'
                    },
                    'pm2_53_24hav': {
                        'extractor': 'last'
                    },
                    'pm2_54_24hav': {
                        'extractor': 'last'
                    },
                    'wh40_batt': {
                        'extractor': 'last'
                    },
                    'wh26_batt': {
                        'extractor': 'last'
                    },
                    'wh25_batt': {
                        'extractor': 'last'
                    },
                    'wh65_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch1_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch2_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch3_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch4_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch5_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch6_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch7_batt': {
                        'extractor': 'last'
                    },
                    'wh31_ch8_batt': {
                        'extractor': 'last'
                    },
                    'wh41_ch1_batt': {
                        'extractor': 'last'
                    },
                    'wh41_ch2_batt': {
                        'extractor': 'last'
                    },
                    'wh41_ch3_batt': {
                        'extractor': 'last'
                    },
                    'wh41_ch4_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch1_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch2_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch3_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch4_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch5_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch6_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch7_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch8_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch9_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch10_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch11_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch12_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch13_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch14_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch15_batt': {
                        'extractor': 'last'
                    },
                    'wh51_ch16_batt': {
                        'extractor': 'last'
                    },
                    'wh55_ch1_batt': {
                        'extractor': 'last'
                    },
                    'wh55_ch2_batt': {
                        'extractor': 'last'
                    },
                    'wh55_ch3_batt': {
                        'extractor': 'last'
                    },
                    'wh55_ch4_batt': {
                        'extractor': 'last'
                    },
                    'wh57_batt': {
                        'extractor': 'last'
                    },
                    'wh68_batt': {
                        'extractor': 'last'
                    },
                    'ws80_batt': {
                        'extractor': 'last'
                    },
                    'wh40_sig': {
                        'extractor': 'last'
                    },
                    'wh26_sig': {
                        'extractor': 'last'
                    },
                    'wh25_sig': {
                        'extractor': 'last'
                    },
                    'wh65_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch1_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch2_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch3_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch4_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch5_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch6_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch7_sig': {
                        'extractor': 'last'
                    },
                    'wh31_ch8_sig': {
                        'extractor': 'last'
                    },
                    'wh41_ch1_sig': {
                        'extractor': 'last'
                    },
                    'wh41_ch2_sig': {
                        'extractor': 'last'
                    },
                    'wh41_ch3_sig': {
                        'extractor': 'last'
                    },
                    'wh41_ch4_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch1_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch2_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch3_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch4_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch5_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch6_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch7_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch8_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch9_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch10_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch11_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch12_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch13_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch14_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch15_sig': {
                        'extractor': 'last'
                    },
                    'wh51_ch16_sig': {
                        'extractor': 'last'
                    },
                    'wh55_ch1_sig': {
                        'extractor': 'last'
                    },
                    'wh55_ch2_sig': {
                        'extractor': 'last'
                    },
                    'wh55_ch3_sig': {
                        'extractor': 'last'
                    },
                    'wh55_ch4_sig': {
                        'extractor': 'last'
                    },
                    'wh57_sig': {
                        'extractor': 'last'
                    },
                    'wh68_sig': {
                        'extractor': 'last'
                    },
                    'ws80_sig': {
                        'extractor': 'last'
                    }
                }
            }
        )
