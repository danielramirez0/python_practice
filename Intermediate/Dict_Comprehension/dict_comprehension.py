# comprehension 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)


# comprehension 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)


# Iterate over a Pandas DataFrame

import pandas 

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76,98]
}

# working with Pandas DataFrame is similar (if not exactly) like working with a dictionary

# Looping through a dict
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame (not ideal)
for (key, value) in student_data_frame.items():
    print(key, value)

# Looping using pandas built-in method
for (index, row) in student_data_frame.iterrows():
    print(index, row.student, row.score)
    if row.student == "Angela":
        print(row.score)