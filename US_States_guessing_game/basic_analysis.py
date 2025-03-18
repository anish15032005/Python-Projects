#count no. of gray,cinnamon and black squirrels in the central park
import pandas as pd
data = pd.read_csv("squirrel_data.csv")

#count no of gray squirrels

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
#create a dataset for the above data
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}
squirrel_data = pd.DataFrame(data_dict)
squirrel_data.to_csv("squirrel_count.csv")
print(squirrel_data)