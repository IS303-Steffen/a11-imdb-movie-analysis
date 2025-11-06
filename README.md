#### Assignment 10
# Pandas Basics

This assignment is a chance to practice the basics of using a Pandas dataframe, including importing data to Python, accessing specific values and columns, updating values, filtering data, sorting data, and using math functions.

Note that the output of this program is kind of ugly. At this point, you are just practicing the main functions of pandas. Its use will become more elegant when you combine it with databases.

## Libraries Required
-	pandas

## Logical Flow:
### 1. Import data from an Excel file:
-	Using the provided `practice_names.csv` file in your repository, create a DataFrame using the `read_csv` function from `pandas`.

> Hint: For readability, I recommend putting an extra blank line between each print statement you print out below

2. Access specific columns:
-	Print out the city column
-	Print out the name and age columns in one print statement 
    - remember to use `[[column_name, column_name2]]`

3. Update values:
-	Update the salary of "Joey Tribbiani" to 56000 and the age of "Jane Smith" to 29. Then, in one print statement print out the rows for Joey Tribbiani and Jane Smith (so just those 2 rows, but it includes all columns).

4. Inserting columns:
-	Add a column called “seniority” to the DataFrame. It should be 4th column. Make the column filled with an empty string ( `""` or `''` ) as the data.

5. Updating based on a condition:
-	Update the “seniority” column to say “Experienced” for anyone that is 35 years old or older.

6. Filter:
-	Use the `.query()` method to find all individuals who are 30 years old or older and live in either "Seattle", "Boston", or "San Francisco". The result of this query should be stored as a new DataFrame (or do the query in place).

7. Sort:
-	Sort the DataFrame based on the salary column in descending order, and make sure the original DataFrame is changed, or that you store the result in a new DataFrame. Print out this DataFrame
    - At this point the DataFrame should contain a "seniority" column, and only individuals 30 years old or old that live in "Seattle", "Boston", or "San Francisco").

8. Math functions:
-	Print out the mean of the salary column, rounded to the 2nd decimal.
    - Note that at this point, you’ve filtered out a lot of data, which is how it should be. This is the mean salary of the filtered data to this point.

9. Group by:
-	Create a new DataFrame that is grouped by “city” and make it so that you show the mean salary of each city. Print out the new DataFrame

10. Exporting to a new format
-	Export the new DataFrame you made to an Excel file called “mean_salary_by_city.xlsx”

## Example Output
```
0          New York
1       Los Angeles
2           Chicago
3           Seattle
4           Houston
5      Philadelphia
6            Boston
7     San Francisco
8            Newark
9         San Diego
10         New York
11      Los Angeles
12          Chicago
13          Seattle
14          Houston
15     Philadelphia
16           Boston
17    San Francisco
18           Newark
19        San Diego
20         New York
21      Los Angeles
22          Chicago
23          Seattle
24          Houston
25     Philadelphia
26           Boston
27    San Francisco
28           Newark
29        San Diego
Name: city, dtype: object

                 name  age
0           John Doe   35
1         Jane Smith   28
2       Frank Wright   40
3          Amy Adams   30
4       Rachel Green   32
5      Chandler Bing   36
6        Ross Geller   37
7      Monica Geller   34
8     Joey Tribbiani   38
9      Phoebe Buffay   36
10         Bob Dylan   41
11      Sarah Connor   29
12        James Dean   50
13   Natalie Portman   31
14       Jack Dawson   42
15      Tracy Jordan   39
16         Liz Lemon   37
17     Jenna Maroney   40
18   Kenneth Parcell   27
19   Frank Rossitano   35
20          Lucy Liu   50
21      Marc Anthony   29
22       Bruce Wayne   33
23        Clark Kent   36
24      Diana Prince   32
25      Peter Parker   21
26      Harry Potter   29
27  Hermione Granger   28
28       Ron Weasley   30
29      Draco Malfoy   31

             name  age         city  salary
8  Joey Tribbiani   38       Newark   56000
1      Jane Smith   29  Los Angeles   65000

                name  age           city    seniority  salary
23       Clark Kent   36        Seattle  Experienced   94000
16        Liz Lemon   37         Boston  Experienced   91000
7     Monica Geller   34  San Francisco                80000
6       Ross Geller   37         Boston  Experienced   72000
3         Amy Adams   30        Seattle                71000
13  Natalie Portman   31        Seattle                62000
17    Jenna Maroney   40  San Francisco  Experienced   58000

 75428.57

 city
Boston           81500.000000
San Francisco    69000.000000
Seattle          75666.666667
Name: salary, dtype: float64
```

## Rubric
See `Rubric.md`