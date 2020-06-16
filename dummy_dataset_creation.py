# To create dummy dataset for machine learning to train the model.

import pandas as pd
import random

# Panda module to create data frame
# Randint function from random module

column_names = ['column1_charwithnull', 'column2_char', 'column3_cat1', 'column4_cat2', 'column5_int', 'column6_formula']
data_frame = pd.DataFrame(columns=column_names)

randomListWithNull = ['', 'Y', 'N']
randomList = ['Y', 'N']
randomCat1 = ['SS', 'COMP']
randomCat2 = ['A', 'A+', 'B', 'G']

# Creating distinct list for character set & different categorical list.
# Above lists will be used to create dataset with randomly selected values.

number_of_row = 5000

for i in range(0, number_of_row):
    data_frame.loc[i] = (random.choice(randomListWithNull), random.choice(randomList), random.choice(randomCat1), random.choice(randomCat2), random.randint(0, 2800), random.randint(0, 300000) / random.randint(1, 15))

data_frame.to_csv("./Training_Set.csv", index=False)
