#### Assignment 11
# IMDb Movie Analysis

This assignment is a chance to practice the basics of using a Pandas DataFrame, including importing data to Python, accessing specific values and columns, updating values, filtering data, sorting data, and using math functions. The hardest part of this is just remembering the syntax of all the pandas DataFrame methods.

The dataset you'll be using is the top rated 1000 movies from imdb.com. It contains these columns:
- `title`: movie title
- `overview`: short description of the movie
- `released_year`: year the movie first came out
- `primary_genre`: the first genre listed for the movie on IMDb
- `runtime_minutes`: how long the movie is in minutes
- `imdb_rating`: The average rating (1-10) from all IMDb users that have rated it
- `votes`: the number of IMDb users that have rated the movie.
- `metacritic_rating`: the movie's rating on metacritic (0-100) (a different site that aggregates professional ratings)
- `gross_earnings_dollars`: How much money the movie grossed in dollars
- `director`: who directed the movie

## Libraries Required
- `pandas`
- `openpyxl`
    - you don't need to include `import openpyxl`, but it needs to be installed so that `pandas` can read and create excel files.

## Note so you don't get frustrated
If you have the Excel Viewer extension installed and you click on an Excel file in VS Code you'll be able to see it. Just PLEASE remember, that if you open up an Excel file, then change that Excel file with your code, and then go back to look at the Excel file, you WON'T see the change UNTIL you close the window with the excel file and then open it back up again. If it seems like your code isn't exporting Excel files correctly, just try closing out of the excel file window and see if that fixes it.

## Logical Flow:
### 1. Import data from an Excel file:
- Using the provided `imdb_top_1000.xlsx` file in your repository, create a DataFrame using the `.read_excel()` function from `pandas`. Name your DataFrame whatever you want, but these instructions will just use `df` to refer to your DataFrame.
- Then print out your DataFrame, but use `df.head()` so that it only prints out the first 5 rows
    - There are 1000 rows in your DataFrame, so `.head()` makes it easier to see what the structure looks like without taking up all the space in your terminal.

> Hint: For readability, I recommend putting an extra blank line between each print statement you print out below

### 2. Access specific columns:
- Print out only the `title` column with `.head()`
- Print out just the `title` and `released_year` columns in one print statement with `.head()`
    - remember to use `[[column_name, column_name2]]`

### 3. Update values:
- Change the `overview` column of row index `16` to be `"No, I am your father"`
    - You could use .loc or .iloc to do this
- Then, print out the entire row with index `16`.
    - It will probably print out vertically, that's totally fine.

### 4. Inserting a new column:
- Add a column called `runtime_hours` to the DataFrame. It should be 6th column (right after `runtime_minutes`. Just remember that column indices are 0 based). Use the `.insert()` method to do this. This column should be calculated based on the `runtime_minutes` column.
    - You can use this to convert minutes to hours: `(df["runtime_minutes"] / 60).round(2)`
- Print out the `title`, `runtime_minutes`, and `runtime_hours` columns with `.head()` to see if you did it right. It should look like this:
```
                      title  runtime_minutes  runtime_hours
0  The Shawshank Redemption              142           2.37
1             The Godfather              175           2.92
2           The Dark Knight              152           2.53
3    The Godfather: Part II              202           3.37
4              12 Angry Men               96           1.60 
```
- Export the whole DataFrame (that has the new column and the updated value in index 16) to an excel file using the `.to_excel()` method. Use the `index=False` parameter in the `to_excel()` function to leave out the index values in the exported file. Call the file `everything_plus_new_column.xlsx`. It needs to be called that exactly for the automated tests to pass.


### 5. Filtering the dataframe:
- Use the `.query()` method (or another method if you want) to find all movies with `Comedy` as their `primary_genre`, that were released in 2015 or newer, and have an `imdb_rating` of 8.0 or higher.
- Print out the filtered results
- Export the results to an excel file using the `.to_excel()` method. Use the `index=False` parameter in the `to_excel()` function to leave out the index values in the exported file. Call the file `newer_comedies.xlsx`. It needs to be called that exactly for the automated tests to pass.

### 6. Using math functions:
- Use the `.max()` function on the `gross_earnings_dollars` to find out what the highest grossing amount is in the dataset.

### 7. Group by and math functions:
- Use the `.groupby()` function to view the `mean`  `imdb_rating` (rounded to the 2nd decimal place) grouped by `primary_genre`. In otherwords, you're finding out what the mean rating is for each genre of movie. When using `.groupby()` remember that the structure looks like this:
    - `df.groupby('column_you_are_grouping_on')['column_you_are_calculating_on].mean().round(2)`
- Print out the results
- Export the results to an excel file using `.to_excel()`, but keep the indices this time. Call the excel file `mean_rating_by_genre.xlsx`.

## Rubric
- See `RUBRIC.md` for details on each of the tests you're scored on.
- To see what score you'll receive, run the tests using the testing tab (it looks like a beaker).
    - In the testing tab, press `Configure Python Tests`, then choose `pytest`, then `tests`, and then press the `Run Tests` button.
        - If you accidentally choose the wrong options for `Configure Python Tests`, to choose again, go to `View` > `Command Palette` and then type `Python: Configure Tests` and hit enter. Then choose the options above again.
- To see your results and any error messages, right click the `TEST_RESULTS_SUMMARY.md` file and choose `Open Preview`.

## Example Output
Note: Depending on your screen size and how zoomed out or zoomed in your screen is in VS Code, your terminal might not print out every column, and might put `...` between some columns. Thats totally fine.

```
                      title                                           overview  released_year primary_genre  runtime_minutes  imdb_rating    votes  metacritic_rating  gross_earnings_dollars              director
0  The Shawshank Redemption  Two imprisoned men bond over a number of years...           1994         Drama              142          9.3  2343110               80.0              28341469.0        Frank Darabont
1             The Godfather  An organized crime dynasty's aging patriarch t...           1972         Crime              175          9.2  1620367              100.0             134966411.0  Francis Ford Coppola
2           The Dark Knight  When the menace known as the Joker wreaks havo...           2008        Action              152          9.0  2303232               84.0             534858444.0     Christopher Nolan
3    The Godfather: Part II  The early life and career of Vito Corleone in ...           1974         Crime              202          9.0  1129952               90.0              57300000.0  Francis Ford Coppola
4              12 Angry Men  A jury holdout attempts to prevent a miscarria...           1957         Crime               96          9.0   689845               96.0               4360000.0          Sidney Lumet 

0    The Shawshank Redemption
1               The Godfather
2             The Dark Knight
3      The Godfather: Part II
4                12 Angry Men
Name: title, dtype: object 

                      title  released_year
0  The Shawshank Redemption           1994
1             The Godfather           1972
2           The Dark Knight           2008
3    The Godfather: Part II           1974
4              12 Angry Men           1957 

title                     Star Wars: Episode V - The Empire Strikes Back
overview                                            No, I am your father
released_year                                                       1980
primary_genre                                                     Action
runtime_minutes                                                      124
imdb_rating                                                          8.7
votes                                                            1159315
metacritic_rating                                                   82.0
gross_earnings_dollars                                       290475067.0
director                                                  Irvin Kershner
Name: 16, dtype: object 

                      title  runtime_minutes  runtime_hours
0  The Shawshank Redemption              142           2.37
1             The Godfather              175           2.92
2           The Dark Knight              152           2.53
3    The Godfather: Part II              202           3.37
4              12 Angry Men               96           1.60 

                                         title                                           overview  released_year primary_genre  runtime_minutes  runtime_hours  imdb_rating   votes  metacritic_rating  gross_earnings_dollars                  director
19                                Gisaengchung  Greed and class discrimination threaten the ne...           2019        Comedy              132           2.20          8.6  552778               96.0              53367844.0              Bong Joon Ho
128                                 Chhichhore  A tragic incident forces Anirudh, a middle-age...           2019        Comedy              143           2.38          8.2   33893                NaN                898575.0             Nitesh Tiwari
132  Three Billboards Outside Ebbing, Missouri  A mother personally challenges the local autho...           2017        Comedy              115           1.92          8.2  432610               88.0              54513740.0           Martin McDonagh
322                                 Badhaai ho  A man is embarrassed when he finds out his mot...           2018        Comedy              124           2.07          8.0   27978                NaN                     NaN  Amit Ravindernath Sharma
327                                 La La Land  While navigating their careers in Los Angeles,...           2016        Comedy              128           2.13          8.0  505918               94.0             151101803.0           Damien Chazelle 

936662225.0 

primary_genre
Action       7.95
Adventure    7.94
Animation    7.93
Biography    7.94
Comedy       7.90
Crime        8.02
Drama        7.96
Family       7.80
Fantasy      8.00
Film-Noir    7.97
Horror       7.91
Mystery      7.98
Thriller     7.80
Western      8.35
Name: imdb_rating, dtype: float64 
```