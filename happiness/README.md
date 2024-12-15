
# Happiness Dataset Analysis

## Dataset Overview
Analysis of the happiness dataset with detailed insights, statistical summaries, and key findings.

### Sample Data
```
  Country name  year  Life Ladder  Log GDP per capita  Social support  Healthy life expectancy at birth  Freedom to make life choices  Generosity  Perceptions of corruption  Positive affect  Negative affect
0  Afghanistan  2008        3.724               7.350           0.451                              50.5                         0.718       0.164                      0.882            0.414            0.258
1  Afghanistan  2009        4.402               7.509           0.552                              50.8                         0.679       0.187                      0.850            0.481            0.237
2  Afghanistan  2010        4.758               7.614           0.539                              51.1                         0.600       0.118                      0.707            0.517            0.275
3  Afghanistan  2011        3.832               7.581           0.521                              51.4                         0.496       0.160                      0.731            0.480            0.267
4  Afghanistan  2012        3.783               7.661           0.521                              51.7                         0.531       0.234                      0.776            0.614            0.268
```

### Summary Statistics
```
                                   count unique      top freq        mean       std     min     25%     50%      75%     max
Country name                        2363    165  Lebanon   18         NaN       NaN     NaN     NaN     NaN      NaN     NaN
year                              2363.0    NaN      NaN  NaN  2014.76386  5.059436  2005.0  2011.0  2015.0   2019.0  2023.0
Life Ladder                       2363.0    NaN      NaN  NaN    5.483566  1.125522   1.281   4.647   5.449   6.3235   8.019
Log GDP per capita                2335.0    NaN      NaN  NaN    9.399671  1.152069   5.527  8.5065   9.503  10.3925  11.676
Social support                    2350.0    NaN      NaN  NaN    0.809369  0.121212   0.228   0.744  0.8345    0.904   0.987
Healthy life expectancy at birth  2300.0    NaN      NaN  NaN   63.401828  6.842644    6.72  59.195    65.1  68.5525    74.6
Freedom to make life choices      2327.0    NaN      NaN  NaN    0.750282  0.139357   0.228   0.661   0.771    0.862   0.985
Generosity                        2282.0    NaN      NaN  NaN    0.000098  0.161388   -0.34  -0.112  -0.022  0.09375     0.7
Perceptions of corruption         2238.0    NaN      NaN  NaN    0.743971  0.184865   0.035   0.687  0.7985  0.86775   0.983
Positive affect                   2339.0    NaN      NaN  NaN    0.651882   0.10624   0.179   0.572   0.663    0.737   0.884
Negative affect                   2347.0    NaN      NaN  NaN    0.273151  0.087131   0.083   0.209   0.262    0.326   0.705
```

### Missing Values
```
Country name                          0
year                                  0
Life Ladder                           0
Log GDP per capita                   28
Social support                       13
Healthy life expectancy at birth     63
Freedom to make life choices         36
Generosity                           81
Perceptions of corruption           125
Positive affect                      24
Negative affect                      16
```

### Key Insights
- Life Ladder scores have a mean of 5.48 and vary significantly.
- Missing values are found in GDP, social support, and health expectancy.
- Positive correlation between GDP and happiness levels is notable.
