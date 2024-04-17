# 1 - nyc_weather.csv contains new york city weather for the first
# few days in the month of January. Answer the following questions:

# a) Average temp in the 1st week of January?
# b) Max temp in 1st 10 days of January?
# c) Determine data structure to use

list = []

with open('nyc_weather.csv', 'r') as f:
    for line in f:
        elements = line.split(',')
        try:
            temperature = int(elements[1])
            list.append(temperature)
        except:
            print("Temp not valid, skipping")

# check to make sure list is populated
print(list)

# a) get temp during first week of january
first_week = list[0:7]
avg_first_week = sum(first_week) / len(first_week)
print("Average temperature during first week of January:", avg_first_week)

# b) get max temp in first 10 days of january
first_ten_days = list[0:10]
max_temp = max(first_ten_days)
print("Max temperature in first 10 days of January:", max_temp)

# 2 - nyc_weather.csv contains new york city weather for the first
# few days in the month of January. Answer the following questions:

# i) Temp on January 9th?
# ii) Temp on January 4th?
hashMap = {}

with open('nyc_weather.csv', 'r') as f:
    for line in f:
        elements = line.split(',')
        date = elements[0]
        try:
            temperature = int(elements[1])
            hashMap[date] = temperature
        except:
            print("Temp not valid, skipping")

# check to make sure hashMap is populated
print(hashMap.keys())
print(hashMap.values())

# i) get temp on January 9th
print("Temperature on January 9th:", hashMap['Jan 9'])

# ii) get temp on January 4th
print("Temperature on January 4th:", hashMap['Jan 4'])