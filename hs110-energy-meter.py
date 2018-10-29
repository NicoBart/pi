from pyHS100 import SmartPlug
from pprint import pformat as pf

ENERGY_METER = "192.168.1.34"

plug = SmartPlug(ENERGY_METER)

## Querying basic information
print("Hardware: %s" % pf(plug.hw_info))
print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device

## State & switching
print("Current state: %s" % plug.state)

#plug.turn_off()
#plug.turn_on()

#plug.state = "ON"
#plug.state = "OFF"

## Time information
print("Current time: %s" % plug.time)
print("Timezone: %s" % plug.timezone)

## Getting and setting plug alias
print("Alias: %s" % plug.alias)
#plug.alias = "My New Smartplug"

## Getting energy meter status
print("Current consumtion: %s Watt" % plug.current_consumption())
print("Current consumption: %s" % plug.get_emeter_realtime())
print("Per day: %s" % plug.get_emeter_daily(year=2018, month=10))
print("Per month: %s" % plug.get_emeter_monthly(year=2018))
