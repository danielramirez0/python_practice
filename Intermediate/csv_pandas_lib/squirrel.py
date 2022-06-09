# Create a csv with small table containing Fur Color (Logged in 2018 data under Primary Fur Color column) and Count of grey, black, and cinnamon fur colors
import pandas

DATA = pandas.read_csv("squirrel_data.csv")
COLORS = ["Gray", "Black", "Cinnamon"]
counts = []

for color in COLORS:
    counts.append(len(DATA[DATA["Primary Fur Color"] == color]))

counts_dict = {
    "color": COLORS,
    "count": counts,
}

new_data = pandas.DataFrame(counts_dict)
new_data.to_csv("squirrel_count.csv")

