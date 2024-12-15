
# Goodreads Dataset Analysis

## Dataset Overview
Analysis of the goodreads dataset with detailed insights, statistical summaries, and key findings.

### Sample Data
```
   book_id  goodreads_book_id  best_book_id  work_id  books_count       isbn        isbn13                      authors  original_publication_year                            original_title                                                     title language_code  average_rating  ratings_count  work_ratings_count  work_text_reviews_count  ratings_1  ratings_2  ratings_3  ratings_4  ratings_5                                                   image_url                                             small_image_url
0        1            2767052       2767052  2792775          272  439023483  9.780439e+12              Suzanne Collins                     2008.0                          The Hunger Games                   The Hunger Games (The Hunger Games, #1)           eng            4.34        4780653             4942365                   155254      66715     127936     560092    1481305    2706317  https://images.gr-assets.com/books/1447303603m/2767052.jpg  https://images.gr-assets.com/books/1447303603s/2767052.jpg
1        2                  3             3  4640799          491  439554934  9.780440e+12  J.K. Rowling, Mary GrandPré                     1997.0  Harry Potter and the Philosopher's Stone  Harry Potter and the Sorcerer's Stone (Harry Potter, #1)           eng            4.44        4602479             4800065                    75867      75504     101676     455024    1156318    3011543        https://images.gr-assets.com/books/1474154022m/3.jpg        https://images.gr-assets.com/books/1474154022s/3.jpg
2        3              41865         41865  3212258          226  316015849  9.780316e+12              Stephenie Meyer                     2005.0                                  Twilight                                   Twilight (Twilight, #1)         en-US            3.57        3866839             3916824                    95009     456191     436802     793319     875073    1355439    https://images.gr-assets.com/books/1361039443m/41865.jpg    https://images.gr-assets.com/books/1361039443s/41865.jpg
3        4               2657          2657  3275794          487   61120081  9.780061e+12                   Harper Lee                     1960.0                     To Kill a Mockingbird                                     To Kill a Mockingbird           eng            4.25        3198671             3340896                    72586      60427     117415     446835    1001952    1714267     https://images.gr-assets.com/books/1361975680m/2657.jpg     https://images.gr-assets.com/books/1361975680s/2657.jpg
4        5               4671          4671   245494         1356  743273567  9.780743e+12          F. Scott Fitzgerald                     1925.0                          The Great Gatsby                                          The Great Gatsby           eng            3.89        2683664             2773745                    51992      86236     197621     606158     936012     947718     https://images.gr-assets.com/books/1490528560m/4671.jpg     https://images.gr-assets.com/books/1490528560s/4671.jpg
```

### Summary Statistics
```
                             count unique                                                                                       top  freq                  mean                  std          min              25%              50%              75%              max
book_id                    10000.0    NaN                                                                                       NaN   NaN                5000.5           2886.89568          1.0          2500.75           5000.5          7500.25          10000.0
goodreads_book_id          10000.0    NaN                                                                                       NaN   NaN          5264696.5132        7575461.86359          1.0         46275.75         394965.5       9382225.25       33288638.0
best_book_id               10000.0    NaN                                                                                       NaN   NaN          5471213.5801        7827329.89072          1.0         47911.75         425123.5        9636112.5       35534230.0
work_id                    10000.0    NaN                                                                                       NaN   NaN          8646183.4246       11751060.82408         87.0        1008841.0        2719524.5      14517748.25       56399597.0
books_count                10000.0    NaN                                                                                       NaN   NaN               75.7127           170.470728          1.0             23.0             40.0             67.0           3455.0
isbn                          9300   9300                                                                                 439023483     1                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
isbn13                      9415.0    NaN                                                                                       NaN   NaN  9755044298883.462891  442861920665.573364  195170342.0  9780316192995.0  9780451528640.0  9780830777175.0  9790007672390.0
authors                      10000   4664                                                                              Stephen King    60                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
original_publication_year   9979.0    NaN                                                                                       NaN   NaN           1981.987674           152.576665      -1750.0           1990.0           2004.0           2011.0           2017.0
original_title                9415   9274                                                                                               5                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
title                        10000   9964                                                                            Selected Poems     4                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
language_code                 8916     25                                                                                       eng  6341                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
average_rating             10000.0    NaN                                                                                       NaN   NaN              4.002191             0.254427         2.47             3.85             4.02             4.18             4.82
ratings_count              10000.0    NaN                                                                                       NaN   NaN            54001.2351        157369.956436       2716.0         13568.75          21155.5          41053.5        4780653.0
work_ratings_count         10000.0    NaN                                                                                       NaN   NaN            59687.3216        167803.785237       5510.0         15438.75          23832.5          45915.0        4942365.0
work_text_reviews_count    10000.0    NaN                                                                                       NaN   NaN             2919.9553          6124.378132          3.0            694.0           1402.0          2744.25         155254.0
ratings_1                  10000.0    NaN                                                                                       NaN   NaN             1345.0406          6635.626263         11.0            196.0            391.0            885.0         456191.0
ratings_2                  10000.0    NaN                                                                                       NaN   NaN              3110.885          9717.123578         30.0            656.0           1163.0          2353.25         436802.0
ratings_3                  10000.0    NaN                                                                                       NaN   NaN            11475.8938         28546.449183        323.0           3112.0           4894.0           9287.0         793319.0
ratings_4                  10000.0    NaN                                                                                       NaN   NaN            19965.6966         51447.358384        750.0          5405.75           8269.5          16023.5        1481305.0
ratings_5                  10000.0    NaN                                                                                       NaN   NaN            23789.8056         79768.885611        754.0           5334.0           8836.0          17304.5        3011543.0
image_url                    10000   6669  https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png  3332                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
small_image_url              10000   6669    https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png  3332                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
```

### Missing Values
```
book_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0
```

### Key Insights
- Books in this dataset have an average rating of around 4.0.
- Missing values are primarily in `isbn`, `isbn13`, and `language_code` columns.
- English (`eng`) is the dominant language in this dataset.
