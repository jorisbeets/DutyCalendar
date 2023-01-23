from configparser import ConfigParser

parser = ConfigParser()

parser["SCHEDULE 1"] = {
  "name":"Joris",
  "counter_length":"11",
  "startdate":"17-01-2023",
  "dayson":"15",
  "daysoff":"20"}
parser["SCHEDULE 2"] = {
  "name":"CarolineKort",
  "counter_length":"10",
  "startdate": "26-12-2022",
  "dayson":"8",
  "daysoff":"22"}
parser["SCHEDULE 3"] = {
  "name":"CarolineLang",
  "counter_length":"10",
  "startdate": "10-12-2022",
  "dayson":"9",
  "daysoff":"21"}

with open("config.ini", "w") as configfile:
  parser.write(configfile)