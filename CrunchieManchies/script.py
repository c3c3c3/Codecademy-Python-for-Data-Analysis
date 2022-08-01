import numpy as np

calorie_stats=np.genfromtxt('cereal.csv', delimiter=',')
average_calories=np.mean(calorie_stats)
print average_calories

calorie_stats_sorted=np.sort(calorie_stats)
print calorie_stats_sorted

median_calories=np.median(calorie_stats)
print median_calories

nth_percentile=np.percentile(calorie_stats,5)
print nth_percentile
more_calories=np.mean(calorie_stats>60)
print more_calories
calorie_std=np.std(calorie_stats)
print calorie_std

# Current report conveys info about calorie  amount in cereals. The average value amongst the entire set is 106.88 which is not representative inasmuch as the vast majority of set is higher than this number. The median value is a whole lot more unbiased and equals 110. 
# The nth percentile ends up showing that only 5% of competitor cereals are lower than 60 calories. 
#The standard deviation is 19.36 which means high volatility of the data.
