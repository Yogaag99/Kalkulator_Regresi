from math import sqrt
import pandas as pd

df = pd.read_csv('data_regresi.csv')

n = df.shape[0]
df['xy'] = [df['x'][i]*df['y'][i] for i in range(n)]
df['x^2'] = [df['x'][i]**2 for i in range(n)]
df['y^2'] = [df['y'][i]**2 for i in range(n)]

sum_x = sum(df['x'])
sum_y = sum(df['y'])
sum_xy = sum(df['xy'])
sum_xx = sum(df['x^2'])
sum_yy = sum(df['y^2'])

delta = n*sum_xx - sum_x**2

slope = (n*sum_xy - sum_x*sum_y)/delta
intercept = (sum_xx*sum_y - sum_x*sum_xy)/delta

S_y = sqrt(1/(n-2) * (sum_yy - (sum_xx*sum_y**2 - 2*sum_x*sum_xy*sum_y + n*sum_xy**2)/delta))
d_slope = sqrt(n/delta) * S_y
d_intercept = sqrt(sum_xx/delta) * S_y

print(df)

print('slope:', slope)
print('S_x:', d_slope)
print('intercept:', intercept)
print('S_y:', d_intercept)