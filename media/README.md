
# Media Dataset Analysis

## Dataset Overview
Analysis of the media dataset with detailed insights, statistical summaries, and key findings.

### Sample Data
```
        date language   type        title                             by  overall  quality  repeatability
0  15-Nov-24    Tamil  movie  Meiyazhagan           Arvind Swamy, Karthi        4        5              1
1  10-Nov-24    Tamil  movie    Vettaiyan        Rajnikanth, Fahad Fazil        2        2              1
2  09-Nov-24    Tamil  movie       Amaran  Siva Karthikeyan, Sai Pallavi        4        4              1
3  11-Oct-24   Telugu  movie        Kushi    Vijay Devarakonda, Samantha        3        3              1
4  05-Oct-24    Tamil  movie         GOAT                          Vijay        3        3              1
```

### Summary Statistics
```
                count unique                top  freq      mean       std  min  25%  50%  75%  max
date             2553   2055          21-May-06     8       NaN       NaN  NaN  NaN  NaN  NaN  NaN
language         2652     11            English  1306       NaN       NaN  NaN  NaN  NaN  NaN  NaN
type             2652      8              movie  2211       NaN       NaN  NaN  NaN  NaN  NaN  NaN
title            2652   2312  Kanda Naal Mudhal     9       NaN       NaN  NaN  NaN  NaN  NaN  NaN
by               2390   1528  Kiefer Sutherland    48       NaN       NaN  NaN  NaN  NaN  NaN  NaN
overall        2652.0    NaN                NaN   NaN  3.047511   0.76218  1.0  3.0  3.0  3.0  5.0
quality        2652.0    NaN                NaN   NaN  3.209276  0.796743  1.0  3.0  3.0  4.0  5.0
repeatability  2652.0    NaN                NaN   NaN  1.494721  0.598289  1.0  1.0  1.0  2.0  3.0
```

### Missing Values
```
date              99
language           0
type               0
title              0
by               262
overall            0
quality            0
repeatability      0
```

### Key Insights
- Overall quality scores average around 3.21.
- Repeatability is generally low, with an average score of 1.49.
- Missing values in `date` and `by` fields are significant.
