from configparser import ConfigParser

parser = ConfigParser()

parser["SCHEDULE1"] = {
  "name":"Joris",
  "counter_length":"11",
  "startdate":"2023",
  "days_on":"15",
  "days_off":"20"}
parser["SCHEDULE2"] = {
  "name":"Caroline",
  "counter_length":"10",
  "startdate": "203",
  "days_on":"15",
  "days_off":"20"}

with open("config.ini", "w") as configfile:
  parser.write(configfile)