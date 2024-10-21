import pandas as pd

df_date_region1 = pd.DataFrame(
    [
        ('2022-02-04','East', 97.0),
        ('2022-02-04','West',243.0),
        ('2022-02-05','East',160.0),
        ('2022-02-05','West',35.0),
        ('2022-02-06','East',110.0),
        ('2022-02-06','West',86.0)
    ],
columns =['Date', 'Region', 'Total']).set_index(['Date', 'Region'])


df_date_region2 = pd.DataFrame(
    [
        ('2022-02-04','South', 114.0),
        ('2022-02-05','South', 325.0),
        ('2022-02-06','South', 212.0)
    ],
columns =['Date', 'Region', 'Total']).set_index(['Date', 'Region'])
df_date_region = pd.concat([df_date_region1,
                df_date_region2]).sort_index(level=['Date', 'Region'])
print(df_date_region)
