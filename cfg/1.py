import sys,os
import configparser

config = configparser.ConfigParser()
config.read("xxxooo",encoding='utf-8')
sections = config.sections()
print(sections)
#baseconf = print(config.items("baseconf"))
a = config.options("baseconf")
print(a)
v = config.get('baseconf','port')
print(v)
hs_sec = config.has_section('baseconf')
print(hs_sec)
#config.add_section("SEC_2")
#config.write(open('xxxooo', 'w'))

config.set('SEC_2', 'k10', "123")
config.write(open('xxxooo', 'w'))