import pandas
import csv  # built-in library for working with csv files
WEATHER_FILE = "weather_data.csv"
# default way of working with file

with open(WEATHER_FILE) as data_file:
    data = data_file.readlines()
print(data)

# using csv library


with open(WEATHER_FILE) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# using Pandas library (third-party)


data = pandas.read_csv(WEATHER_FILE)
print("---------")
print(type(data))
print(data)
print(data["temp"])

print("---------")
data_dict = data.to_dict()
print(data_dict)

print("---------")
temp_list = data["temp"].to_list()
print(temp_list)

# custom function


def get_average_from_list(list):
    sum = 0
    for item in list:
        sum += item
    return round(sum / len(list))


print(get_average_from_list(temp_list))

# python built-in sum method

print(round(sum(temp_list) / len(temp_list)))

# using pandas Series.mean method

print(round(data["temp"].mean()))

# get max in list

print(data["temp"].max())


# data can be selected with bracket or dot notation, case sensitive

print(data["condition"])
print(data.condition)


# get data from rows
print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])


# accessing data from store variable

monday = data[data.day == "Monday"]
print(monday.condition)

# convert temp C to F
print(int(monday.temp) * 9 / 5 + 32)


# create DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

scratch_data = pandas.DataFrame(data_dict)
print(scratch_data)

# export to csv

scratch_data.to_csv("my_export.csv")
