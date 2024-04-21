# Explore US Bikeshare Data
**"Explore US Bikeshare Data"** was a project from Udacity for the **["Programming for Data Science with Python"](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104)** Nanodegree Program.

#### From Udacity:

_"In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics."_

## Description
This project enables users to explore bikeshare data through predefined questions. It offers a user-friendly interface for seamless navigation and analysis of the dataset.

### These questions allow users to investigate the dataset, filtering by:
* City
* Month
* Day of the Week

### The information provided includes:

 * #### Popular times of travel (i.e., occurs most often in the start time)
    * most common month
    * most common day of week
    * most common hour of day

 * #### Popular stations and trip
    * most common start station
    * most common end station
    * most common trip from start to end (i.e., most frequent combination of start station and end station)

 * #### Trip duration
    * total travel time
    * average travel time

 * #### User info
    * counts of each user type
    * counts of each gender (only available for NYC and Chicago)
    * earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Files Used
### The files used for the project were:
* chicago.csv
    * Randomly selected data for the first six months of 2017 in Chicago
* new_york_city.csv
    * Randomly selected data for the first six months of 2017 in NYC
* washington.csv
    * Randomly selected data for the first six months of 2017 in Washington
* bikeshare.py
    * A template with helper code and comments to help guide the project

#### The city files contained the following information:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

#### The NYC and Chicago files also contained the following information about the riders:
* Gender
* Birth Year

## How to Use

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/h-rouse/pdsnd_github.git
   ```
2. Make sure you have Python installed on your machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the bikeshare.py file using Python:
    ```
    python bikeshare.py
    ```
5. Follow the prompts in the terminal to interactively explore the bikeshare data.

## Author
[h-rouse](https://github.com/h-rouse) is the sole author of this project. 

Reference material used credited below.

## Credits
### Built with:
* Python 3.12.2
    * program used to create the code
* time
    * library used in the code
* pandas
     * library used in the code
* numpy
    * library used in the code

### Reference material used during this project:
* [PEP 257](https://peps.python.org/pep-0257/)
* [Python time module](https://docs.python.org/3/library/time.html#time.sleep)
* [Python str.lower() method](https://docs.python.org/3/library/stdtypes.html#str.lower)
* [Python return statement](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-return_stmt)
* [Pandas to_datetime() function]( https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas-to-datetime)
* [Pandas Series.dt.day_name() method]( https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html#pandas.Series.dt.day_name)
* [Python datetime.datetime.hour](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour)
* [Python string module](https://docs.python.org/3/library/string.html#module-string)
* [Python KeyError exception](https://docs.python.org/3/library/exceptions.html#KeyError)
* [Pandas DataFrame.iloc[] method]( https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc)
* Udacity "Programming for Data Science with Python" course notes

## Last updated
April 21, 2024

README.md

