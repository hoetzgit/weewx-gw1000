"""
Test suite for the GW1000 driver.

Copyright (C) 2020 Gary Roderick                   gjroderick<at>gmail.com

A python unittest based test suite for aspects of the GW1000 driver. The test
suite tests correct operation of:

-

Version: 0.3.0                                   Date: 20 March 2021

Revision History
    20 March 2021      v0.3.0
        - incomplete but works with release v0.3.0 under python3
        - initial release

To run the test suite:

-   copy this file to the target machine, nominally to the $BIN/user/tests
    directory

-   run the test suite using:

    $ PYTHONPATH=/home/weewx/bin python3 -m user.tests.test_gw1000

    or

    $ PYTHONPATH=/usr/share/weewx python3 -m user.tests.test_gw1000
"""
# python imports
import struct
import unittest

# Python 2/3 compatibility shims
import six

# WeeWX imports
import user.gw1000

# TODO. Check speed_data data and result are correct
# TODO. Check rain_data data and result are correct
# TODO. Check rainrate_data data and result are correct
# TODO. Check big_rain_data data and result are correct
# TODO. Check light_data data and result are correct
# TODO. Check uv_data data and result are correct
# TODO. Check uvi_data data and result are correct
# TODO. Check datetime_data data and result are correct
# TODO. Check leak_data data and result are correct
# TODO. Check batt_data data and result are correct
# TODO. Check distance_data data and result are correct
# TODO. Check utc_data data and result are correct
# TODO. Check count_data data and result are correct
# TODO. Add decode firmware check refer issue #31


class ParserTestCase(unittest.TestCase):
    """Test the Parser class."""

    response1 = {'raw': 1,
                 'payload': 2
                }
    response2 = {'raw': 1,
                 'payload': 2
                }
    cmd_broadcast = {'raw': 1,
                     'parsed': 2
                     }
    cmd_read_ecowitt = {'raw': 1,
                        'parsed': 2
                        }
    parse_cmd_read_wunderground = {'raw': 1,
                                   'parsed': 2
                                   }
    parse_cmd_read_wow = {'raw': 1,
                          'parsed': 2
                          }
    parse_cmd_read_weathercloud = {'raw': 1,
                                   'parsed': 2
                                   }
    parse_cmd_read_customized = {'raw': 1,
                                 'parsed': 2
                                 }
    parse_cmd_read_usrpath = {'raw': 1,
                              'parsed': 2
                              }
    parse_cmd_get_soilhumiad = {'raw': 1,
                                'parsed': 2
                                }
    parse_cmd_get_mulch_offset = {'raw': 1,
                                  'parsed': 2
                                  }
    parse_cmd_get_pm25_offset = {'raw': 1,
                                 'parsed': 2
                                 }
    parse_cmd_get_co2_offset = {'raw': 1,
                                'parsed': 2
                                }
    parse_cmd_read_station_mac = {'raw': 1,
                                  'parsed': 2
                                  }
    parse_cmd_gw1000_livedata = {'raw': 1,
                                 'parsed': 2
                                 }
    parse_cmd_read_ssss = {'raw': 1,
                           'parsed': 2
                           }
    parse_cmd_read_raindata = {'raw': 1,
                               'parsed': 2
                               }
    parse_cmd_read_gain = {'raw': 1,
                           'parsed': 2
                           }
    parse_cmd_read_calibration = {'raw': 1,
                                  'parsed': 2
                                  }
    parse_cmd_read_sensor_id = {'raw': 1,
                                'parsed': 2
                                }
    parse_cmd_read_sensor_id_new = {'raw': 1,
                                    'parsed': 2
                                    }
    parse_cmd_read_firmware_version = {'raw': 1,
                                       'parsed': 2
                                       }
    cmd_read_ecowitt = {'raw': 1,
                        'parsed': 2
                        }

    def setUp(self):
        # get a Parser object
        self.parser = user.gw1000.Parser()
        self.maxDiff = None

    def tearDown(self):
        pass

    def test_get_payload(self):
        """Test Parser.get_payload method."""

        # test a response where the size is stored in a single byte
        self.assertEqual(self.parser.get_payload(self.response1['raw'], size_bytes=1), self.response1['payload'])
        # test a response where the size is stored in two bytes
        self.assertEqual(self.parser.get_payload(self.response2['raw'], size_bytes=2), self.response2['payload'])

    def test_parse_cmds(self):
        """Test the Parser.parse_cmd_xxxxx() methods."""

        # test parse_cmd_broadcast()
        self.assertEqual(self.parser.parse_cmd_broadcast(self.cmd_broadcast['raw']),
                         self.cmd_broadcast['parsed'])
        # test cmd_read_ecowitt()
        self.assertEqual(self.parser.cmd_read_ecowitt(self.cmd_read_ecowitt['raw']),
                         self.cmd_read_ecowitt['parsed'])
        # test parse_cmd_read_wunderground()
        self.assertEqual(self.parser.parse_cmd_read_wunderground(self.parse_cmd_read_wunderground['raw']),
                         self.parse_cmd_read_wunderground['parsed'])
        # test parse_cmd_read_wow()
        self.assertEqual(self.parser.parse_cmd_read_wow(self.parse_cmd_read_wow['raw']),
                         self.parse_cmd_read_wow['parsed'])
        # test parse_cmd_read_weathercloud()
        self.assertEqual(self.parser.parse_cmd_read_weathercloud(self.parse_cmd_read_weathercloud['raw']),
                         self.parse_cmd_read_weathercloud['parsed'])
        # test parse_cmd_read_customized()
        self.assertEqual(self.parser.parse_cmd_read_customized(self.parse_cmd_read_customized['raw']),
                         self.parse_cmd_read_customized['parsed'])
        # test parse_cmd_read_usrpath()
        self.assertEqual(self.parser.parse_cmd_read_usrpath(self.parse_cmd_read_usrpath['raw']),
                         self.parse_cmd_read_usrpath['parsed'])
        # test parse_cmd_get_soilhumiad()
        self.assertEqual(self.parser.parse_cmd_get_soilhumiad(self.parse_cmd_get_soilhumiad['raw']),
                         self.parse_cmd_get_soilhumiad['parsed'])
        # test parse_cmd_get_mulch_offset()
        self.assertEqual(self.parser.parse_cmd_get_mulch_offset(self.parse_cmd_get_mulch_offset['raw']),
                         self.parse_cmd_get_mulch_offset['parsed'])
        # test parse_cmd_get_pm25_offset()
        self.assertEqual(self.parser.parse_cmd_get_pm25_offset(self.parse_cmd_get_pm25_offset['raw']),
                         self.parse_cmd_get_pm25_offset['parsed'])
        # test parse_cmd_get_co2_offset()
        self.assertEqual(self.parser.parse_cmd_get_co2_offset(self.parse_cmd_get_co2_offset['raw']),
                         self.parse_cmd_get_co2_offset['parsed'])
        # test parse_cmd_read_station_mac()
        self.assertEqual(self.parser.parse_cmd_read_station_mac(self.parse_cmd_read_station_mac['raw']),
                         self.parse_cmd_read_station_mac['parsed'])
        # test parse_cmd_gw1000_livedata()
        self.assertEqual(self.parser.parse_cmd_gw1000_livedata(self.parse_cmd_gw1000_livedata['raw']),
                         self.parse_cmd_gw1000_livedata['parsed'])
        # test parse_cmd_read_ssss()
        self.assertEqual(self.parser.parse_cmd_read_ssss(self.parse_cmd_read_ssss['raw']),
                         self.parse_cmd_read_ssss['parsed'])
        # test parse_cmd_read_raindata()
        self.assertEqual(self.parser.parse_cmd_read_raindata(self.parse_cmd_read_raindata['raw']),
                         self.parse_cmd_read_raindata['parsed'])
        # test parse_cmd_read_gain()
        self.assertEqual(self.parser.parse_cmd_read_gain(self.parse_cmd_read_gain['raw']),
                         self.parse_cmd_read_gain['parsed'])
        # test parse_cmd_read_calibration()
        self.assertEqual(self.parser.parse_cmd_read_calibration(self.parse_cmd_read_calibration['raw']),
                         self.parse_cmd_read_calibration['parsed'])
        # test parse_cmd_read_sensor_id()
        self.assertEqual(self.parser.parse_cmd_read_sensor_id(self.parse_cmd_read_sensor_id['raw']),
                         self.parse_cmd_read_sensor_id['parsed'])
        # test parse_cmd_read_sensor_id_new()
        self.assertEqual(self.parser.parse_cmd_read_sensor_id_new(self.parse_cmd_read_sensor_id_new['raw']),
                         self.parse_cmd_read_sensor_id_new['parsed'])
        # test parse_cmd_read_firmware_version()
        self.assertEqual(self.parser.parse_cmd_read_firmware_version(self.parse_cmd_read_firmware_version['raw']),
                         self.parse_cmd_read_firmware_version['parsed'])


class SensorsStateTestCase(unittest.TestCase):
    """Test the Parser.SensorsState class."""

    sensor_ids = {
        b'\x00': {'name': 'wh65', 'long_name': 'WH65', 'batt_fn': 'batt_binary'},
        b'\x01': {'name': 'wh68', 'long_name': 'WH68', 'batt_fn': 'batt_volt'},
        b'\x02': {'name': 'ws80', 'long_name': 'WS80', 'batt_fn': 'batt_volt'},
        b'\x03': {'name': 'wh40', 'long_name': 'WH40', 'batt_fn': 'batt_binary'},
        b'\x04': {'name': 'wh25', 'long_name': 'WH25', 'batt_fn': 'batt_binary'},
        b'\x05': {'name': 'wh26', 'long_name': 'WH26', 'batt_fn': 'batt_binary'},
        b'\x06': {'name': 'wh31_ch1', 'long_name': 'WH31 ch1', 'batt_fn': 'batt_binary'},
        b'\x07': {'name': 'wh31_ch2', 'long_name': 'WH31 ch2', 'batt_fn': 'batt_binary'},
        b'\x08': {'name': 'wh31_ch3', 'long_name': 'WH31 ch3', 'batt_fn': 'batt_binary'},
        b'\x09': {'name': 'wh31_ch4', 'long_name': 'WH31 ch4', 'batt_fn': 'batt_binary'},
        b'\x0a': {'name': 'wh31_ch5', 'long_name': 'WH31 ch5', 'batt_fn': 'batt_binary'},
        b'\x0b': {'name': 'wh31_ch6', 'long_name': 'WH31 ch6', 'batt_fn': 'batt_binary'},
        b'\x0c': {'name': 'wh31_ch7', 'long_name': 'WH31 ch7', 'batt_fn': 'batt_binary'},
        b'\x0d': {'name': 'wh31_ch8', 'long_name': 'WH31 ch8', 'batt_fn': 'batt_binary'},
        b'\x0e': {'name': 'wh51_ch1', 'long_name': 'WH51 ch1', 'batt_fn': 'batt_binary'},
        b'\x0f': {'name': 'wh51_ch2', 'long_name': 'WH51 ch2', 'batt_fn': 'batt_binary'},
        b'\x10': {'name': 'wh51_ch3', 'long_name': 'WH51 ch3', 'batt_fn': 'batt_binary'},
        b'\x11': {'name': 'wh51_ch4', 'long_name': 'WH51 ch4', 'batt_fn': 'batt_binary'},
        b'\x12': {'name': 'wh51_ch5', 'long_name': 'WH51 ch5', 'batt_fn': 'batt_binary'},
        b'\x13': {'name': 'wh51_ch6', 'long_name': 'WH51 ch6', 'batt_fn': 'batt_binary'},
        b'\x14': {'name': 'wh51_ch7', 'long_name': 'WH51 ch7', 'batt_fn': 'batt_binary'},
        b'\x15': {'name': 'wh51_ch8', 'long_name': 'WH51 ch8', 'batt_fn': 'batt_binary'},
        b'\x16': {'name': 'wh41_ch1', 'long_name': 'WH41 ch1', 'batt_fn': 'batt_int'},
        b'\x17': {'name': 'wh41_ch2', 'long_name': 'WH41 ch2', 'batt_fn': 'batt_int'},
        b'\x18': {'name': 'wh41_ch3', 'long_name': 'WH41 ch3', 'batt_fn': 'batt_int'},
        b'\x19': {'name': 'wh41_ch4', 'long_name': 'WH41 ch4', 'batt_fn': 'batt_int'},
        b'\x1a': {'name': 'wh57', 'long_name': 'WH57', 'batt_fn': 'batt_int'},
        b'\x1b': {'name': 'wh55_ch1', 'long_name': 'WH55 ch1', 'batt_fn': 'batt_int'},
        b'\x1c': {'name': 'wh55_ch2', 'long_name': 'WH55 ch2', 'batt_fn': 'batt_int'},
        b'\x1d': {'name': 'wh55_ch3', 'long_name': 'WH55 ch3', 'batt_fn': 'batt_int'},
        b'\x1e': {'name': 'wh55_ch4', 'long_name': 'WH55 ch4', 'batt_fn': 'batt_int'},
        b'\x1f': {'name': 'wh34_ch1', 'long_name': 'WH34 ch1', 'batt_fn': 'batt_volt'},
        b'\x20': {'name': 'wh34_ch2', 'long_name': 'WH34 ch2', 'batt_fn': 'batt_volt'},
        b'\x21': {'name': 'wh34_ch3', 'long_name': 'WH34 ch3', 'batt_fn': 'batt_volt'},
        b'\x22': {'name': 'wh34_ch4', 'long_name': 'WH34 ch4', 'batt_fn': 'batt_volt'},
        b'\x23': {'name': 'wh34_ch5', 'long_name': 'WH34 ch5', 'batt_fn': 'batt_volt'},
        b'\x24': {'name': 'wh34_ch6', 'long_name': 'WH34 ch6', 'batt_fn': 'batt_volt'},
        b'\x25': {'name': 'wh34_ch7', 'long_name': 'WH34 ch7', 'batt_fn': 'batt_volt'},
        b'\x26': {'name': 'wh34_ch8', 'long_name': 'WH34 ch8', 'batt_fn': 'batt_volt'},
        b'\x27': {'name': 'wh45', 'long_name': 'WH45', 'batt_fn': 'batt_int'},
        b'\x28': {'name': 'wh35_ch1', 'long_name': 'WH35 ch1', 'batt_fn': 'batt_volt'},
        b'\x29': {'name': 'wh35_ch2', 'long_name': 'WH35 ch2', 'batt_fn': 'batt_volt'},
        b'\x2a': {'name': 'wh35_ch3', 'long_name': 'WH35 ch3', 'batt_fn': 'batt_volt'},
        b'\x2b': {'name': 'wh35_ch4', 'long_name': 'WH35 ch4', 'batt_fn': 'batt_volt'},
        b'\x2c': {'name': 'wh35_ch5', 'long_name': 'WH35 ch5', 'batt_fn': 'batt_volt'},
        b'\x2d': {'name': 'wh35_ch6', 'long_name': 'WH35 ch6', 'batt_fn': 'batt_volt'},
        b'\x2e': {'name': 'wh35_ch7', 'long_name': 'WH35 ch7', 'batt_fn': 'batt_volt'},
        b'\x2f': {'name': 'wh35_ch8', 'long_name': 'WH35 ch8', 'batt_fn': 'batt_volt'}
    }
    not_registered = ('fffffffe', 'ffffffff')
    parse_sensor_id_data = {'raw': 1,
                            'parsed': 2
                            }
    get_sensor_state_packet = {'raw': 1,
                               'parsed': 2
                               }

    def setUp(self):

        # get a Parser object
        self.parser = user.gw1000.Parser()
        self.maxDiff = None

    def tearDown(self):

        pass

    def test_constants(self):
        """Test SensorsState class constants."""

        # sensor_ids
        self.assertEqual(self.parser.sen_state_obj.sensor_ids, self.sensor_ids)
        # not_registered
        self.assertEqual(self.parser.sen_state_obj.not_registered, self.not_registered)

    def test_parse_sensor_id_data(self):
        """Test parse_sensor_id_data() method."""

        self.assertEqual(self.parser.sen_state_obj.parse_sensor_id_data['raw'],
                         self.parse_sensor_id_data['parsed'])

    def test_get_sensor_state_packet(self):
        """Test get_sensor_state_packet() method."""

        self.assertEqual(self.parser.sen_state_obj.get_sensor_state_packet['raw'],
                         self.get_sensor_state_packet['parsed'])

    def test_battery_desc(self):
        """Test battery_desc() method."""

        # binary description
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x00', 0), 'OK')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x00', 1), 'low')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x00', 2), 'Unknown')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x00', None), 'Unknown')

        # int description
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x16', 0), 'low')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x16', 1), 'low')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x16', 4), 'OK')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x16', 6), 'DC')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x16', 7), 'Unknown')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x16', None), 'Unknown')

        # voltage description
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x20', 0), 'low')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x20', 1.2), 'low')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x20', 1.5), 'OK')
        self.assertEqual(self.parser.sen_state_obj.battery_desc(b'\x20', None), 'Unknown')

    def test_battery_decode(self):
        """Test battery decode methods."""

        # binary battery states (method batt_binary())
        self.assertEqual(self.parser.sen_state_obj.batt_binary(255), 1)
        self.assertEqual(self.parser.sen_state_obj.batt_binary(4), 0)

        # integer battery states (method batt_int())
        for int_batt in range(7):
            self.assertEqual(self.parser.sen_state_obj.batt_int(int_batt), int_batt)

        # voltage battery states (method batt_volt())
        self.assertEqual(self.parser.sen_state_obj.batt_volt(0), 0.00)
        self.assertEqual(self.parser.sen_state_obj.batt_volt(100), 2.00)
        self.assertEqual(self.parser.sen_state_obj.batt_volt(101), 2.02)
        self.assertEqual(self.parser.sen_state_obj.batt_volt(255), 5.1)

class SensorsDataTestCase(unittest.TestCase):
    """Test the Parser.SensorsData class."""

    response_struct = {
        b'\x01': ('decode_temp', 2, 'intemp'),
        b'\x02': ('decode_temp', 2, 'outtemp'),
        b'\x03': ('decode_temp', 2, 'dewpoint'),
        b'\x04': ('decode_temp', 2, 'windchill'),
        b'\x05': ('decode_temp', 2, 'heatindex'),
        b'\x06': ('decode_humid', 1, 'inhumid'),
        b'\x07': ('decode_humid', 1, 'outhumid'),
        b'\x08': ('decode_press', 2, 'absbarometer'),
        b'\x09': ('decode_press', 2, 'relbarometer'),
        b'\x0A': ('decode_dir', 2, 'winddir'),
        b'\x0B': ('decode_speed', 2, 'windspeed'),
        b'\x0C': ('decode_speed', 2, 'gustspeed'),
        b'\x0D': ('decode_rain', 2, 'rainevent'),
        b'\x0E': ('decode_rainrate', 2, 'rainrate'),
        b'\x0F': ('decode_rain', 2, 'rainhour'),
        b'\x10': ('decode_rain', 2, 'rainday'),
        b'\x11': ('decode_rain', 2, 'rainweek'),
        b'\x12': ('decode_big_rain', 4, 'rainmonth'),
        b'\x13': ('decode_big_rain', 4, 'rainyear'),
        b'\x14': ('decode_big_rain', 4, 'raintotals'),
        b'\x15': ('decode_light', 4, 'light'),
        b'\x16': ('decode_uv', 2, 'uv'),
        b'\x17': ('decode_uvi', 1, 'uvi'),
        b'\x18': ('decode_datetime', 6, 'datetime'),
        b'\x19': ('decode_speed', 2, 'daymaxwind'),
        b'\x1A': ('decode_temp', 2, 'temp1'),
        b'\x1B': ('decode_temp', 2, 'temp2'),
        b'\x1C': ('decode_temp', 2, 'temp3'),
        b'\x1D': ('decode_temp', 2, 'temp4'),
        b'\x1E': ('decode_temp', 2, 'temp5'),
        b'\x1F': ('decode_temp', 2, 'temp6'),
        b'\x20': ('decode_temp', 2, 'temp7'),
        b'\x21': ('decode_temp', 2, 'temp8'),
        b'\x22': ('decode_humid', 1, 'humid1'),
        b'\x23': ('decode_humid', 1, 'humid2'),
        b'\x24': ('decode_humid', 1, 'humid3'),
        b'\x25': ('decode_humid', 1, 'humid4'),
        b'\x26': ('decode_humid', 1, 'humid5'),
        b'\x27': ('decode_humid', 1, 'humid6'),
        b'\x28': ('decode_humid', 1, 'humid7'),
        b'\x29': ('decode_humid', 1, 'humid8'),
        b'\x2A': ('decode_pm25', 2, 'pm251'),
        b'\x2B': ('decode_temp', 2, 'soiltemp1'),
        b'\x2C': ('decode_moist', 1, 'soilmoist1'),
        b'\x2D': ('decode_temp', 2, 'soiltemp2'),
        b'\x2E': ('decode_moist', 1, 'soilmoist2'),
        b'\x2F': ('decode_temp', 2, 'soiltemp3'),
        b'\x30': ('decode_moist', 1, 'soilmoist3'),
        b'\x31': ('decode_temp', 2, 'soiltemp4'),
        b'\x32': ('decode_moist', 1, 'soilmoist4'),
        b'\x33': ('decode_temp', 2, 'soiltemp5'),
        b'\x34': ('decode_moist', 1, 'soilmoist5'),
        b'\x35': ('decode_temp', 2, 'soiltemp6'),
        b'\x36': ('decode_moist', 1, 'soilmoist6'),
        b'\x37': ('decode_temp', 2, 'soiltemp7'),
        b'\x38': ('decode_moist', 1, 'soilmoist7'),
        b'\x39': ('decode_temp', 2, 'soiltemp8'),
        b'\x3A': ('decode_moist', 1, 'soilmoist8'),
        b'\x3B': ('decode_temp', 2, 'soiltemp9'),
        b'\x3C': ('decode_moist', 1, 'soilmoist9'),
        b'\x3D': ('decode_temp', 2, 'soiltemp10'),
        b'\x3E': ('decode_moist', 1, 'soilmoist10'),
        b'\x3F': ('decode_temp', 2, 'soiltemp11'),
        b'\x40': ('decode_moist', 1, 'soilmoist11'),
        b'\x41': ('decode_temp', 2, 'soiltemp12'),
        b'\x42': ('decode_moist', 1, 'soilmoist12'),
        b'\x43': ('decode_temp', 2, 'soiltemp13'),
        b'\x44': ('decode_moist', 1, 'soilmoist13'),
        b'\x45': ('decode_temp', 2, 'soiltemp14'),
        b'\x46': ('decode_moist', 1, 'soilmoist14'),
        b'\x47': ('decode_temp', 2, 'soiltemp15'),
        b'\x48': ('decode_moist', 1, 'soilmoist15'),
        b'\x49': ('decode_temp', 2, 'soiltemp16'),
        b'\x4A': ('decode_moist', 1, 'soilmoist16'),
        b'\x4C': ('decode_batt', 16, 'lowbatt'),
        b'\x4D': ('decode_pm25', 2, 'pm251_24h_avg'),
        b'\x4E': ('decode_pm25', 2, 'pm252_24h_avg'),
        b'\x4F': ('decode_pm25', 2, 'pm253_24h_avg'),
        b'\x50': ('decode_pm25', 2, 'pm254_24h_avg'),
        b'\x51': ('decode_pm25', 2, 'pm252'),
        b'\x52': ('decode_pm25', 2, 'pm253'),
        b'\x53': ('decode_pm25', 2, 'pm254'),
        b'\x58': ('decode_leak', 1, 'leak1'),
        b'\x59': ('decode_leak', 1, 'leak2'),
        b'\x5A': ('decode_leak', 1, 'leak3'),
        b'\x5B': ('decode_leak', 1, 'leak4'),
        b'\x60': ('decode_distance', 1, 'lightningdist'),
        b'\x61': ('decode_utc', 4, 'lightningdettime'),
        b'\x62': ('decode_count', 4, 'lightningcount'),
        # WH34 battery data is not obtained from live data rather it is
        # obtained from sensor ID data
        b'\x63': ('decode_wh34', 3, 'temp9'),
        b'\x64': ('decode_wh34', 3, 'temp10'),
        b'\x65': ('decode_wh34', 3, 'temp11'),
        b'\x66': ('decode_wh34', 3, 'temp12'),
        b'\x67': ('decode_wh34', 3, 'temp13'),
        b'\x68': ('decode_wh34', 3, 'temp14'),
        b'\x69': ('decode_wh34', 3, 'temp15'),
        b'\x6A': ('decode_wh34', 3, 'temp16'),
        b'\x70': ('decode_wh45', 16, ('temp17', 'humid17', 'pm10',
                                      'pm10_24h_avg', 'pm255', 'pm255_24h_avg',
                                      'co2', 'co2_24h_avg')),
        b'\x71': (None, None, None),
        b'\x72': ('decode_wet', 1, 'leafwet1'),
        b'\x73': ('decode_wet', 1, 'leafwet2'),
        b'\x74': ('decode_wet', 1, 'leafwet3'),
        b'\x75': ('decode_wet', 1, 'leafwet4'),
        b'\x76': ('decode_wet', 1, 'leafwet5'),
        b'\x77': ('decode_wet', 1, 'leafwet6'),
        b'\x78': ('decode_wet', 1, 'leafwet7'),
        b'\x79': ('decode_wet', 1, 'leafwet8')
    }
    rain_field_codes = (b'\x0D', b'\x0E', b'\x0F', b'\x10',
                        b'\x11', b'\x12', b'\x13', b'\x14')
    wind_field_codes = (b'\x0A', b'\x0B', b'\x0C', b'\x19')

    response_data = 'FF FF 27 00 40 01 01 40 06 26 08 27 D2 09 27 D2 2A 00 5A ' \
                    '4D 00 65 2C 27 2E 14 1A 00 ED 22 3A 1B 01 0B 23 3A 4C 06 ' \
                    '00 00 00 05 FF FF 00 F6 FF FF FF FF FF FF FF 62 00 00 00 ' \
                    '00 61 FF FF FF FF 60 FF EC'
    parsed_response = {'intemp': 32.0,
                       'inhumid': 38,
                       'absbarometer': 1019.4,
                       'relbarometer': 1019.4,
                       'pm251': 9.0,
                       'pm251_24h_avg': 10.1,
                       'soilmoist1': 39,
                       'soilmoist2': 20,
                       'temp1': 23.7,
                       'humid1': 58,
                       'temp2': 26.7,
                       'humid2': 58,
                       'lightningcount': 0,
                       'lightningdettime': None,
                       'lightningdist': None,
                       'datetime': 1599021263}
    temp_data = {'hex': '00 EA', 'value': 23.4}
    humid_data = {'hex': '48', 'value': 72}
    press_data = {'hex': '27 4C', 'value': 1006.0}
    dir_data = {'hex': '00 70', 'value': 112}
    speed_data = {'hex': '00 70', 'value': 11.2}
    rain_data = {'hex': '01 70', 'value': 36.8}
    rainrate_data = {'hex': '00 34', 'value': 5.2}
    big_rain_data = {'hex': '01 70 37 21', 'value': 2413136.1}
    light_data = {'hex': '02 40 72 51', 'value': 3777800.1}
    uv_data = {'hex': '32 70', 'value': 1291.2}
    uvi_data = {'hex': '0C', 'value': 12}
    datetime_data = {'hex': '0C AB 23 41 56 37', 'value': (12, 171, 35, 65, 86, 55)}
    pm25_data = {'hex': '00 39', 'value': 5.7}
    moist_data = {'hex': '3A', 'value': 58}
    leak_data = {'hex': '3A', 'value': 58}
    distance_data = {'hex': '1A', 'value': 26}
    utc_data = {'hex': '5F 40 72 51', 'value': 1598059089}
    count_data = {'hex': '00 40 72 51', 'value': 4223569}
    wh34_data = {'hex': '00 EA 4D',
                 'field': 't',
                 'value': {'t': 23.4}
                 }
    wh45_data = {'hex': '00 EA 4D 35 6D 28 78 34 3D 62 7E 8D 2A 39 9F 04',
                 'field': ('t', 'h', 'p10', 'p10_24', 'p25', 'p25_24', 'c', 'c_24'),
                 'value': {'t': 23.4, 'h': 77, 'p10': 1367.7, 'p10_24': 1036.0,
                           'p25': 1337.3, 'p25_24': 2521.4, 'c': 36138, 'c_24': 14751}
                 }

    def setUp(self):

        # get a Parser object
        self.parser = user.gw1000.Parser()
        self.maxDiff = None

    def tearDown(self):

        pass

    def test_constants(self):
        """Test constants used by class Parser.SensorsData()."""

        # response_struct
        self.assertEqual(self.parser.sen_data_obj.response_struct, self.response_struct)
        # rain_field_codes
        self.assertEqual(self.parser.sen_data_obj.rain_field_codes, self.rain_field_codes)
        # wind_field_codes
        self.assertEqual(self.parser.sen_data_obj.wind_field_codes, self.wind_field_codes)

    def test_decode(self):
        """Test class Parser() methods used to decode obs bytes."""

        # test temperature decode (method decode_temp())
        self.assertEqual(self.parser.sen_data_obj.decode_temp(hex_to_bytes(self.temp_data['hex'])),
                         self.temp_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_temp(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_temp(hex_to_bytes(xbytes(3))), None)

        # test humidity decode (method decode_humid())
        self.assertEqual(self.parser.sen_data_obj.decode_humid(hex_to_bytes(self.humid_data['hex'])),
                         self.humid_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_humid(hex_to_bytes(xbytes(0))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_humid(hex_to_bytes(xbytes(2))), None)

        # test pressure decode (method decode_press())
        self.assertEqual(self.parser.sen_data_obj.decode_press(hex_to_bytes(self.press_data['hex'])),
                         self.press_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_press(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_press(hex_to_bytes(xbytes(3))), None)

        # test direction decode (method decode_dir())
        self.assertEqual(self.parser.sen_data_obj.decode_dir(hex_to_bytes(self.dir_data['hex'])),
                         self.dir_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_dir(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_dir(hex_to_bytes(xbytes(3))), None)

        # test big rain decode (method decode_big_rain())
        self.assertEqual(self.parser.sen_data_obj.decode_big_rain(hex_to_bytes(self.big_rain_data['hex'])),
                         self.big_rain_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_big_rain(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_big_rain(hex_to_bytes(xbytes(5))), None)

        # test datetime decode (method decode_datetime())
        self.assertEqual(self.parser.sen_data_obj.decode_datetime(hex_to_bytes(self.datetime_data['hex'])),
                         self.datetime_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_datetime(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_datetime(hex_to_bytes(xbytes(7))), None)

        # test distance decode (method decode_distance())
        self.assertEqual(self.parser.sen_data_obj.decode_distance(hex_to_bytes(self.distance_data['hex'])),
                         self.distance_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_distance(hex_to_bytes(xbytes(0))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_distance(hex_to_bytes(xbytes(2))), None)

        # test utc decode (method decode_utc())
        self.assertEqual(self.parser.sen_data_obj.decode_utc(hex_to_bytes(self.utc_data['hex'])),
                         self.utc_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_utc(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_utc(hex_to_bytes(xbytes(5))), None)

        # test count decode (method decode_count())
        self.assertEqual(self.parser.sen_data_obj.decode_count(hex_to_bytes(self.count_data['hex'])),
                         self.count_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_count(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_count(hex_to_bytes(xbytes(5))), None)

        # test speed decode (method decode_speed())
        self.assertEqual(self.parser.sen_data_obj.decode_speed(hex_to_bytes(self.speed_data['hex'])),
                         self.speed_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_speed(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_speed(hex_to_bytes(xbytes(3))), None)

        # test rain decode (method decode_rain())
        self.assertEqual(self.parser.sen_data_obj.decode_rain(hex_to_bytes(self.rain_data['hex'])),
                         self.rain_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_rain(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_rain(hex_to_bytes(xbytes(3))), None)

        # test rain rate decode (method decode_rainrate())
        self.assertEqual(self.parser.sen_data_obj.decode_rainrate(hex_to_bytes(self.rainrate_data['hex'])),
                         self.rainrate_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_rainrate(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_rainrate(hex_to_bytes(xbytes(3))), None)

        # test light decode (method decode_light())
        self.assertEqual(self.parser.sen_data_obj.decode_light(hex_to_bytes(self.light_data['hex'])),
                         self.light_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_light(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_light(hex_to_bytes(xbytes(5))), None)

        # test uv decode (method decode_uv())
        self.assertEqual(self.parser.sen_data_obj.decode_uv(hex_to_bytes(self.uv_data['hex'])),
                         self.uv_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_uv(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_uv(hex_to_bytes(xbytes(3))), None)

        # test uvi decode (method decode_uvi())
        self.assertEqual(self.parser.sen_data_obj.decode_uvi(hex_to_bytes(self.uvi_data['hex'])),
                         self.uvi_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_uvi(hex_to_bytes(xbytes(0))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_uvi(hex_to_bytes(xbytes(2))), None)

        # test moisture decode (method decode_moist())
        self.assertEqual(self.parser.sen_data_obj.decode_moist(hex_to_bytes(self.moist_data['hex'])),
                         self.moist_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_moist(hex_to_bytes(xbytes(0))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_moist(hex_to_bytes(xbytes(2))), None)

        # test pm25 decode (method decode_pm25())
        self.assertEqual(self.parser.sen_data_obj.decode_pm25(hex_to_bytes(self.pm25_data['hex'])),
                         self.pm25_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_pm25(hex_to_bytes(xbytes(1))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_pm25(hex_to_bytes(xbytes(3))), None)

        # test leak decode (method decode_leak())
        self.assertEqual(self.parser.sen_data_obj.decode_leak(hex_to_bytes(self.leak_data['hex'])),
                         self.leak_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_leak(hex_to_bytes(xbytes(0))), None)
        self.assertEqual(self.parser.sen_data_obj.decode_leak(hex_to_bytes(xbytes(2))), None)

        # test wh34 decode (method decode_pm10())
        pass

        # test wh34 decode (method decode_co2())
        pass

        # test wh34 decode (method decode_wh34())
        self.assertEqual(self.parser.sen_data_obj.decode_wh34(hex_to_bytes(self.wh34_data['hex']), field=self.wh34_data['field']), self.wh34_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_wh34(hex_to_bytes(xbytes(1)), field=self.wh34_data['field']), {})
        self.assertEqual(self.parser.sen_data_obj.decode_wh34(hex_to_bytes(xbytes(4)), field=self.wh34_data['field']), {})

        # test wh45 decode (method decode_wh45())
        self.assertEqual(self.parser.sen_data_obj.decode_wh45(hex_to_bytes(self.wh45_data['hex']), fields=self.wh45_data['field']),
                         self.wh45_data['value'])
        # test correct handling of too few and too many bytes
        self.assertEqual(self.parser.sen_data_obj.decode_wh45(hex_to_bytes(xbytes(1)), fields=self.wh45_data['field']), {})
        self.assertEqual(self.parser.sen_data_obj.decode_wh45(hex_to_bytes(xbytes(17)), fields=self.wh45_data['field']), {})

        # test legacy decode battery (method decode_batt())
        # should return None no matter what we pass
        self.assertEqual(self.parser.sen_data_obj.decode_batt(hex_to_bytes(xbytes(0))), None)

        # test parsing of all possible sensors
        self.assertDictEqual(self.parser.parse(cmd='CMD_GW1000_LIVEDATA', raw_data=hex_to_bytes(self.response_data)),
                             self.parsed_response)


class UtilitiesTestCase(unittest.TestCase):
    """Unit tests for utility functions."""

    unsorted_dict = {'leak2': 'leak2',
                     'inHumidity': 'inhumid',
                     'wh31_ch3_batt': 'wh31_ch3_batt',
                     'leak1': 'leak1',
                     'wh31_ch2_batt': 'wh31_ch2_batt',
                     'windDir': 'winddir',
                     'inTemp': 'intemp'}
    sorted_dict_str = "{'inHumidity': 'inhumid', 'inTemp': 'intemp', " \
                      "'leak1': 'leak1', 'leak2': 'leak2', " \
                      "'wh31_ch2_batt': 'wh31_ch2_batt', " \
                      "'wh31_ch3_batt': 'wh31_ch3_batt', " \
                      "'windDir': 'winddir'}"
    sorted_keys = ['inHumidity', 'inTemp', 'leak1', 'leak2',
                   'wh31_ch2_batt', 'wh31_ch3_batt', 'windDir']
    bytes_to_hex_fail_str = "cannot represent '%s' as hexadecimal bytes"

    def test_utilities(self):

        # test natural_sort_keys()
        self.assertEqual(user.gw1000.natural_sort_keys(self.unsorted_dict),
                         self.sorted_keys)

        # test natural_sort_dict()
        self.assertEqual(user.gw1000.natural_sort_dict(self.unsorted_dict),
                         self.sorted_dict_str)

        # test bytes_to_hex()
        self.assertEqual(user.gw1000.bytes_to_hex(hex_to_bytes('ff 00 66 b2')),
                         'FF 00 66 B2')
        self.assertEqual(user.gw1000.bytes_to_hex(hex_to_bytes('ff 00 66 b2'), separator=':'),
                         'FF:00:66:B2')
        self.assertEqual(user.gw1000.bytes_to_hex(hex_to_bytes('ff 00 66 b2'), caps=False),
                         'ff 00 66 b2')
        self.assertEqual(user.gw1000.bytes_to_hex(hex_to_bytes('ff 00 66 b2'), separator=':', caps=False),
                         'ff:00:66:b2')
        # and check exceptions raised
        # TypeError
        self.assertEqual(user.gw1000.bytes_to_hex(22), self.bytes_to_hex_fail_str % 22)
        # AttributeError
        self.assertEqual(user.gw1000.bytes_to_hex(hex_to_bytes('ff 00 66 b2'), separator=None),
                         self.bytes_to_hex_fail_str % hex_to_bytes('ff 00 66 b2'))

        # test obfuscate()
        # > 8 character string, should see trailing 4 characters
        self.assertEqual(user.gw1000.obfuscate('1234567890'), '******7890')
        # 7 character string, should see trailing 3 characters
        self.assertEqual(user.gw1000.obfuscate('1234567'), '****567')
        # 5 character string, should see trailing 2 characters
        self.assertEqual(user.gw1000.obfuscate('12345'), '***45')
        # 3 character string, should see last character
        self.assertEqual(user.gw1000.obfuscate('123'), '**3')
        # 2 character string, should see no characters
        self.assertEqual(user.gw1000.obfuscate('12'), '**')
        # check obfuscation character
        self.assertEqual(user.gw1000.obfuscate('1234567890', obf_char='#'),
                         '######7890')


class ListsAndDictsTestCase(unittest.TestCase):
    """Test case to test list and dict consistency."""

    def setUp(self):

        # construct the default field map
        default_field_map = dict(user.gw1000.Gw1000.default_field_map)
        # now add in the rain field map
        default_field_map.update(user.gw1000.Gw1000.rain_field_map)
        # now add in the wind field map
        default_field_map.update(user.gw1000.Gw1000.wind_field_map)
        # now add in the battery state field map
        default_field_map.update(user.gw1000.Gw1000.battery_field_map)
        # now add in the sensor signal field map
        default_field_map.update(user.gw1000.Gw1000.sensor_signal_field_map)
        # and save it for later
        self.default_field_map = default_field_map

    def test_dicts(self):
        """Test dicts for consistency."""

        # test that each entry in the GW1000 default field map appears in the observation group dictionary
        for w_field, g_field in six.iteritems(self.default_field_map):
            self.assertIn(g_field,
                          user.gw1000.DirectGw1000.gw1000_obs_group_dict.keys(),
                          msg="A field from the GW1000 default field map is missing from the observation group dictionary")

        # test that each entry in the observation group dictionary is included in the GW1000 default field map
        for g_field, group in six.iteritems(user.gw1000.DirectGw1000.gw1000_obs_group_dict):
            self.assertIn(g_field,
                          self.default_field_map.values(),
                          msg="A key from the observation group dictionary is missing from the GW1000 default field map")


class StationTestCase(unittest.TestCase):

    cmd_read_fware_ver = b'\x50'
    read_fware_cmd_bytes = b'\xff\xffP\x03S'
    read_fware_resp_bytes = b'\xff\xffP\x11\rGW1000_V1.6.1v'
    read_fware_resp_bad_checksum_bytes = b'\xff\xffP\x11\rGW1000_V1.6.1w'
    read_fware_resp_bad_cmd_bytes = b'\xff\xffQ\x11\rGW1000_V1.6.1v'

    def setUp(self):

        # get a Gw1000Collector Station object, specify phony ip, port and mac
        # to prevent the GW1000 driver from actually looking for a GW1000
        self.station = user.gw1000.Gw1000Collector.Station(ip_address='1.1.1.1',
                                                           port=1234,
                                                           mac='1:2:3:4:5:6')

    def test_response(self):

        # test checksum calculation
        self.assertEqual(self.station.calc_checksum(b'00112233bbccddee'), 168)
        # test check_response() with good data, should be no exception
        try:
            self.station.check_response(self.read_fware_resp_bytes,
                                        self.cmd_read_fware_ver)
        except user.gw1000.InvalidChecksum:
            self.fail("check_reponse() raised an InvalidChecksum exception")
        except user.gw1000.InvalidApiResponse:
            self.fail("check_reponse() raised an InvalidApiResponse exception")
        # test check_response() with a bad checksum data, should be an InvalidChecksum exception
        self.assertRaises(user.gw1000.InvalidChecksum,
                          self.station.check_response,
                          response=self.read_fware_resp_bad_checksum_bytes,
                          cmd_code=self.cmd_read_fware_ver)
        # test check_response() with a bad response, should be an InvalidApiResponse exception
        self.assertRaises(user.gw1000.InvalidApiResponse,
                          self.station.check_response,
                          response=self.read_fware_resp_bad_cmd_bytes,
                          cmd_code=self.cmd_read_fware_ver)


class Gw1000TestCase(unittest.TestCase):

    def setUp(self):

        pass

    def test_map(self):
        pass

    def test_rain(self):
        pass

    def test_lightning(self):
        pass


def hex_to_bytes(hex_string):
    """Takes a string of hex character pairs and returns a string of bytes.

    Allows us to specify a byte string in a little more human readable format.
    Takes a space delimited string of hex pairs and converts to a string of
    bytes. hex_string pairs must be spaced delimited, eg 'AB 2E 3B'.

    If we only ran under python3 we could use bytes.fromhex(), but we need to
    cater for python2 as well so use struct.pack.
    """

    # first get our hex string as a list of integers
    dec_list = [int(a, 16) for a in hex_string.split()]
    # now pack them in a sequence of bytes
    return struct.pack('B' * len(dec_list), *dec_list)


def xbytes(num, hex_string='00', separator=' '):
    """Construct a string of delimited repeated hex pairs.

    Resulting string contains num occurrences of hex_string separated by
    separator.
    """

    return separator.join([hex_string] * num)


if __name__ == '__main__':
    unittest.main(verbosity=2)
