# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) 
#     # print(data)
#     for row in data:
#         # print(row)
#         temperatures = []
#         for row in data:
#             if row[1] != "temp":
#                 temperatures.append(int(row[1]))
#         print(temperatures)
   
import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temperatures = data["temp"].to_list()  
# avg_temp = sum(temperatures) / len(temperatures)
# print(int(avg_temp))

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data["temp"].median())

# # Get data in columns
# print(data["condition"])
# print(data.condition)
# print(data.day)


# #get data in rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"] 
# print(monday.condition)
# print(monday.temp * 9/5 + 32)

#create a dataframe from scratch
data_dict = {
    "students": ["Pratham", "Anish", "Shreyansh","Divyanshu"],
    "scores": [76, 56, 65,60],
}
pandas_data = pandas.DataFrame(data_dict)
pandas_data.to_csv("new_data.csv")
print(pandas_data)