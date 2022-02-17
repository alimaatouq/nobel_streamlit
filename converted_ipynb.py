from asyncore import write
import statsmodels
import streamlit as st
st.title('Converted ipynb file into py')
st.header("Exercise 1. Let's take a look at Nobel prize Laureats")
st.markdown("""
<p><img style="float: right;margin:5px 20px 5px 1px; max-width:250px" src="https://www.nicepng.com/png/detail/11-111010_laurel-wreath-psd37402-laurel-wreath.png"></p>
In this exercise we will dive into the Nobel prize Laureats dataset by the Nobel Prize Foundation. This dataset lists all prize winners from the start of the prize in 1901 till 2016.  \n
The Nobel prize is one of the most famous and prestigious intellectual awards. It is awarded annually for 6 different categories. From Stockholm, the Royal Swedish Academy of Sciences confers the prizes for physics, chemistry, and economics, the Karolinska Institute confers the prize for physiology or medicine, and the Swedish Academy confers the prize for literature. The Norwegian Nobel Committee based in Oslo confers the prize for peace.  \n
A person or organization awarded the Nobel Prize is called a Nobel Laureate. The word "laureate" refers to the laurel wreath (إكليل الغار) that was considered as "a trophy" in ancient greek, given to victors of competitions (image to the right).  \n
The aim of this exercise is to train you on handling dataframes with Pandas. Main visualization library used will be Seaborn (don't stick to it, focus later on Plotly please).
""" , unsafe_allow_html=True)

text1 = """
### Part 1 - Setting up the environment and loading required libraries
 
  1.1- Import Pandas, Seaborn and Numpy (as pd, sns and np)
  1.2- Read in the dataset
  1.3- Take a look at the first 10 laureats

  1.1- Import Pandas, Seaborn and Numpy (as pd, sns and np)
"""
st.write(text1)

import pandas as pd
import seaborn as sns
import numpy as np

st.write("""1.2- Read in the dataset 
Hint: Use pd.read_csv to read in datasets/nobel.csv and save it into a dataframe "nobel" """)
url = "https://drive.google.com/file/d/1GRdngFI5Do-TrvWtCnOBOl0e3vgc2tU0/view?usp=sharing"
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
nobel = pd.read_csv(path)

st.write("""1.3- Take a look at the first 10 laureats
Hint: use the method head()""")

st.code("""
1.1- Import Pandas, Seaborn and Numpy (as pd, sns and np
import pandas as pd
import seaborn as sns
import numpy as np

#  1.2- Read in the dataset
# Hint: Use pd.read_csv to read in datasets/nobel.csv and save it into a dataframe "nobel"
url = "https://drive.google.com/file/d/1GRdngFI5Do-TrvWtCnOBOl0e3vgc2tU0/view?usp=sharing"
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
nobel = pd.read_csv(path)

# 1.3- Take a look at the first 10 laureats
# Hint: use the method head()
display(nobel.head(10))
"""
)

st.write((nobel.head(10)))

text2 = """
### Part 2 - Which country had most laureats?

Just looking at the first couple of prize winners, or Nobel laureates as they are also called,
we already see a celebrity: Wilhelm Conrad Röntgen, the guy who discovered X-rays. And actually, 
we see that all of the winners in 1901 were guys that came from Europe. But that was back in 1901, 
looking at all winners in the dataset, from 1901 to 2016, 
which country is the most commonly represented? Also, when did it start to dominate the prize?
(For country, we will use the column birth_country of the winner)


Display the number of (possibly shared) Nobel Prizes handed between 1901 and 2016.
Hint: Count the number of rows/prizes using the len() function. Use the display() function to display the result.
I had to import a library to be able to use display() function source: https://stackoverflow.com/questions/49328447/display-in-python
"""
st.write(text2)
from IPython.display import display
display(len(nobel['prize']))
st.write(len(nobel['prize']))

st.write("Count the number of prizes for each birth_country using value_counts() and show the top 10. Do not use display().")
prize_per_country = nobel['birth_country'].value_counts()

st.code("""
from IPython.display import display
display(len(nobel['prize']))
st.write(len(nobel['prize']))
prize_per_country = nobel['birth_country'].value_counts()
print(prize_per_country.head(10))
""")

print(prize_per_country.head(10))
st.write(prize_per_country.head(10))

text3 = """ ### Part 3 - USA-born laureats by decade

3.1 - Calculate the proportion of USA born winners per decade
3.2 - Display the proportions of USA born winners per decade


3.1 - Add a usa_born_winner column to nobel, where the value is True when birth_country is "United States of America".
Refer to https://cmdlinetips.com/2019/05/how-to-create-a-column-using-condition-on-another-column-in-pandas/ """

st.write(text3)
nobel['usa_born_winner'] = np.where(nobel["birth_country"] == "United States of America", True, False)

text4 = """ Add a decade column to nobel for the decade each prize was awarded. Here, np.floor() will come in handy. Ensure the decade column is of type int64.
Hint: astype(int)
check this example: 
year = pd.Series([1843, 1877, 1923])
decade = (np.floor(year / 10) * 10).astype(int)
decade is now 1840, 1870, 1920"""
st.write(text4)
year_series = pd.Series(nobel['year'])
nobel['decade'] = (np.floor(year_series/10)*10).astype(int)

st.write("""3.2- Display the proportions of USA born winners per decade
Hint: Use groupby to group by decade, setting as_index=False. Then isolate the usa_born_winner column and take the mean(). Assign the resulting DataFrame to prop_usa_winners.""") 
winners_decade = nobel.groupby('decade', as_index=False)['usa_born_winner'].count()

prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

print(prop_usa_winners)

winners_decade.sort_values('usa_born_winner', ascending=False).reset_index(drop=True)
st.code("""
year_series = pd.Series(nobel['year'])
nobel['decade'] = (np.floor(year_series/10)*10).astype(int)
winners_decade = nobel.groupby('decade', as_index=False)['usa_born_winner'].count()

prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

print(prop_usa_winners)

winners_decade.sort_values('usa_born_winner', ascending=False).reset_index(drop=True)
""")
st.write(prop_usa_winners)
st.write("""
### Part 4 - USA laureats, visualized
A table is OK, but to see when the USA started to dominate the Nobel charts we need a plot!

Plot the proportion of USA born winners per decade.

4.1 - Use seaborn to plot prop_usa_winners with decade on the x-axis and usa_born_winner on the y-axis as an sns.lineplot. Assign the plot to ax.<br>
4.2 - Fix the y-scale so that it shows percentages using PercentFormatter.
""")
import matplotlib.pyplot as plt
fig = plt.figure()
# Setting the plotting theme (done for you)
sns.set()
# and setting the size of all plots. (done for you)
plt.rcParams['figure.figsize'] = [15, 12]  # try different numbers once you have the plot

# Plotting USA born winners 
ax = sns.lineplot(x= 'decade', y='usa_born_winner', data = nobel)

# Adding %-formatting to the y-axis (done for you)
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

# Use Percent formatter method here
#Hint: Check this: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent/36319915#36319915
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

st.code("""
import matplotlib.pyplot as plt
fig = plt.figure()
# Setting the plotting theme (done for you)
sns.set()
# and setting the size of all plots. (done for you)
plt.rcParams['figure.figsize'] = [15, 12]  # try different numbers once you have the plot

# Plotting USA born winners 
ax = sns.lineplot(x= 'decade', y='usa_born_winner', data = nobel)

# Adding %-formatting to the y-axis (done for you)
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

# Use Percent formatter method here
#Hint: Check this: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent/36319915#36319915
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
""")
st.pyplot(fig)

st.write("""### Part 5 - What is the gender of a typical Nobel Prize winner?

 So the USA became the dominating winner of the Nobel Prize first in the 1930s and had remained since. If we look at the gender of laureats, we see a clear imbalande. How significant is this imbalance? And is it better or worse within specific prize categories like physics, medicine, literature, etc.? Let's find out.
 We have to plot the proportions of female laureats by decade split by prize category.
 
 5.1 - Add the female_winner column to nobel, where the value is True when sex is "Female".
 
 5.2 - Use groupby to group by both decade and category, setting as_index=False. Then isolate the female_winner column and take the mean(). Assign the resulting DataFrame to prop_female_winners.

 5.3 - Copy and paste your seaborn plot from part 4 (including axis formatting code), but plot prop_female_winners and map the category variable to the "hue" parameter.
 """)

 # 5.1 - Calculating the proportion of female laureates per decade
nobel['female_winner'] = np.where(nobel["sex"] == "Female", True, False)

# 5.2 - Grouping by both decade and category
#Hint_link: https://stackoverflow.com/questions/17679089/pandas-dataframe-groupby-two-columns-and-get-counts
prop_female_winners = nobel.groupby(['decade', 'category'], as_index = False)['female_winner'].mean()

# 5.3 - Plotting USA born winners with % winners on the y-axis (refer to what you did in part 4)
fig1 =plt.figure()
sns.set()
# and setting the size of all plots. (done for you)
plt.rcParams['figure.figsize'] = [15, 12]  # try different numbers once you have the plot

# Plotting USA born winners 
ax = sns.lineplot(x= 'decade', y='female_winner', data = prop_female_winners, hue= 'category')

# Adding %-formatting to the y-axis (done for you)
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

# Use Percent formatter method here
#Hint: Check this: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent/36319915#36319915
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

st.code("""
# 5.1 - Calculating the proportion of female laureates per decade
nobel['female_winner'] = np.where(nobel["sex"] == "Female", True, False)

# 5.2 - Grouping by both decade and category
#Hint_link: https://stackoverflow.com/questions/17679089/pandas-dataframe-groupby-two-columns-and-get-counts
prop_female_winners = nobel.groupby(['decade', 'category'], as_index = False)['female_winner'].mean()

# 5.3 - Plotting USA born winners with % winners on the y-axis (refer to what you did in part 4)
fig1 =plt.figure()
sns.set()
# and setting the size of all plots. (done for you)
plt.rcParams['figure.figsize'] = [15, 12]  # try different numbers once you have the plot

# Plotting USA born winners 
ax = sns.lineplot(x= 'decade', y='female_winner', data = prop_female_winners, hue= 'category')

# Adding %-formatting to the y-axis (done for you)
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

# Use Percent formatter method here
#Hint: Check this: https://stackoverflow.com/questions/31357611/format-y-axis-as-percent/36319915#36319915
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
""")
st.pyplot(fig1)

st.write("""### Part 6 - The first woman to win the Nobel Prize
 
Who was the first woman to receive a Nobel Prize? And in which category?

6.1 - Select only the rows of 'Female' winners in nobel.

6.2 -Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.
""")
# 6.1 - Select only the rows of 'Female' winners in nobel.
female_winners = nobel[nobel['female_winner'] == True]

#6.2 - Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.
# Hint: DataFrame.nsmallest(self, n, columns, keep='first')
# Hint_link: https://www.w3resource.com/pandas/dataframe/dataframe-nsmallest.php
#Another Hint_link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nsmallest.html
first_female_winner = female_winners.nsmallest(1, 'female_winner')
# OR I can use: first_female_winner = female_winners.nsmallest(1, 'female_winner', keep='first') but I only need 1 row. 

print(first_female_winner)

st.code("""
# 6.1 - Select only the rows of 'Female' winners in nobel.
female_winners = nobel[nobel['female_winner'] == True]

#6.2 - Using the nsmallest() method with its n and columns parameters, pick out the first woman to get a Nobel Prize.
# Hint: DataFrame.nsmallest(self, n, columns, keep='first')
# Hint_link: https://www.w3resource.com/pandas/dataframe/dataframe-nsmallest.php
#Another Hint_link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nsmallest.html
first_female_winner = female_winners.nsmallest(1, 'female_winner')
# OR I can use: first_female_winner = female_winners.nsmallest(1, 'female_winner', keep='first') but I only need 1 row. 

print(first_female_winner)
""")

st.write(first_female_winner)

st.write("""### Part 7 - Some won more than 1 ! 

Who are these few? 

Extract and display the rows of repeat Nobel Prize winners. Use 'groupby' to group nobel by 'full_name'. Use the 'filter' method to keep only those rows in nobel with winners with 2 or more prizes.

Selecting the laureates that have received 2 or more prizes.
Hint: Here is an example of how to use groupby together with filter. This would keep only those rows with birth countries that have had 50 or more winners:
nobel.groupby('birth_country').filter(lambda group: len(group) >= 50)""")
multiple_nobel_winners =  nobel.groupby('full_name').filter(lambda group: len(group) >= 2)
# OR Method 2
multiple_nobel_winners_2 = nobel[nobel.duplicated(['full_name'], keep = False)]
#method 1 result
print(multiple_nobel_winners)

st.code("""
multiple_nobel_winners =  nobel.groupby('full_name').filter(lambda group: len(group) >= 2)
# OR Method 2
multiple_nobel_winners_2 = nobel[nobel.duplicated(['full_name'], keep = False)]
#method 1 result
print(multiple_nobel_winners)
""")

st.write(multiple_nobel_winners)

st.write("""### Part 8 - How old are you when you get the prize?
Several laureats have received the Nobel prize twice. Marie Curie got the prize in physics for discovering radiation and in chemistry for isolating radium and polonium. John Bardeen got it twice in physics for transistors and superconductivity, Frederick Sanger got it twice in chemistry, and Linus Carl Pauling got it first in chemistry and later in peace for his work in promoting nuclear disarmament. Two organizations also got the prize twice : the Red Cross and the UNHCR.

But how old are Laureats generally when they get the prize?

Calculate and plot the age of each winner when they won their Nobel Prize.

8.1 - Convert the nobel['birth_date'] column to datetime using pd.to_datetime.

8.2 - Add a new column nobel['age'] that contains the age of each winner when they got the prize. That is, year of prize win minus birth year.

8.3 - Use sns.lmplot (not sns.lineplot) to make a plot with year on the x-axis and age on the y-axis.""")
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
nobel['birth_year'] = pd. DatetimeIndex(nobel['birth_date']).year
nobel['age'] = nobel['year'] - nobel['birth_year']
sns.lmplot(x= 'year', y= 'age', data= nobel, lowess=True, aspect=2, line_kws={'color':'black'})

st.code("""
# 8.1 - Converting birth_date from String to datetime
nobel["birth_date"] = pd.to_datetime(nobel["birth_date"])
nobel.info()
# Hint: https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime

# 8.2 - Calculating the age of Nobel Prize winners
nobel['birth_year'] = pd. DatetimeIndex(nobel['birth_date']).year
nobel["age"] = nobel["year"] - nobel["birth_date"]

# 8.3 - Plotting the age of Nobel Prize winners: Use sns.lmplot (not sns.lineplot) to make a plot with year on the x-axis and age on the y-axis.
# To make the plot prettier, add the arguments lowess=True, aspect=2, and line_kws={'color' : 'black'}.
sns.lmplot(x= 'year', y= 'age', data= nobel, lowess=True, aspect=2, line_kws={'color':'black'})
# Hint_link: https://seaborn.pydata.org/generated/seaborn.lmplot.html
"""
)

st.pyplot(fig = plt)

import io 
buffer = io.StringIO() 
nobel.info(buf=buffer)
s = buffer.getvalue() 
with open("df_info.txt", "w", encoding="utf-8") as f:
  st.text(s)

st.write("""### Part 9 - Age differences between prize categories
From the plot above, we can see that people used to be around 55 when they received the prize, but nowadays the average is closer to 65.
We can also see that the density of points is much high nowadays than befor, and since the number of prizes is still the same (+1), then this means that nowadays many more of the prizes are shared between several people. We can also see the small gap in prizes around the Second World War (1939 - 1945).
Let's look at age trends within different prize categories (use sns.lmplot).
You have to Plot how old tha laureats are, within the different price categories.
As before, use sns.lmplot to make a plot with year on the x-axis and age on the y-axis. But this time, make one plot per prize category by setting the row argument to 'category'
Hint: Copy and paste your solution from task 8 and then add the argument row='category' to the function call""")
st.code("""
sns.lmplot(x= 'year', y= 'age', data= nobel, lowess=True, aspect=2, line_kws={'color':'black'}, row = 'category')
""")
st.write("""Scroll down to see the several plots. One by category. Beautiful!""")
sns.lmplot(x= 'year', y= 'age', data= nobel, lowess=True, aspect=2, line_kws={'color':'black'}, row = 'category')
st.pyplot(fig = plt)

st.write("""### Part 10 - Oldest and youngest winners
Who are the oldest and youngest people ever to have won a Nobel Prize? Pick out the rows of the oldest and the youngest winner of a Nobel Prize.
The oldest winner of a Nobel Prize as of 2016
Hint: Use nlargest() to pick out and display the row of the oldest winner.""")
oldest_winner = nobel.nlargest(1, 'age')
print(oldest_winner)
st.code("""
oldest_winner = nobel.nlargest(1, 'age')
print(oldest_winner)
""")
st.write("The oldest Nobel prize winner is: ",nobel["full_name"].iloc[793])
st.write(oldest_winner)

st.write("""The youngest winner of a Nobel Prize as of 2016
Hint: Use nsmallest() to pick out and display the row of the youngest winner.""")
youngest_winner = nobel.nsmallest(1, 'age')
print(youngest_winner)
st.code("""
youngest_winner = nobel.nsmallest(1, 'age')
print(youngest_winner)
""")
st.write("The youngest Nobel prize winner is: ",nobel["full_name"].iloc[885])
st.write(youngest_winner)
st.markdown("""## Done. Nobel Prize in Analytics !
<p><img style="float: center;margin:5px 20px 5px 1px; max-width:250px" src="https://www.nicepng.com/png/detail/11-111010_laurel-wreath-psd37402-laurel-wreath.png"></p>
""", unsafe_allow_html=True)
