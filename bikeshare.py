import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    
    Expected Input: User input for city, month, and day.
        Example Input: "chicago", "1" (for January), "3" (for Wednesday)
    Expected Output: Tuple containing city, month, and day strings.
        Example Output: ("chicago", "january", "wednesday")
    """
    # Added time.sleep() thoughout to improve readability.
    # Added ASCII art to add visual interest.
    time.sleep(1)
    print(f'\n{bicycle_ascii_1}')
    time.sleep(0.5)
    print(f'\n{bicycle_ascii_2}')
    time.sleep(0.5)
    print(f'\n{bicycle_ascii_3}')
    time.sleep(0.5)
    print(f'\n{bicycle_ascii_4}')
    time.sleep(0.5)
    print(f'\n{bicycle_ascii_5}')
    
    print('\nHello! Let\'s explore some US bikeshare data!')
    time.sleep(2)
    
    # Exiting option to improve functionality.
    print('-'*40)
    print('\n\nNOTE: Input "x" to exit the program at any time\n')
    print('-'*40)
    time.sleep(2)
    # Get user input for city (chicago, new york city, washington). Use a while loop to handle invalid inputs.
    while True:
        city = input('\n\nThe following cities are available to research: '
                     '\n\nChicago \nNew York City \nWashington'
                     # Added .lower() to correct for casing errors
                     '\n\nPlease enter a city name: ').lower()
    # Returning None for city, month, and day to exit program when 'x' is input.
        if city == 'x':
           return None, None, None
        elif city not in CITY_DATA:
            time.sleep(0.5)
            print('\n\nThat is an invalid entry. \n')
            time.sleep(2)
        else:
            time.sleep(0.5)
            print(f'\nGreat! You\'ve selected {city.title()}.')
            time.sleep(1)
            print('-'*40)
            break

    # Defined a dictionary to map the assigned numbers to month options.
    month_dict = {
        '1': 'january',
        '2': 'february',
        '3': 'march',
        '4': 'april',
        '5': 'may',
        '6': 'june',
        '7': 'all'
    }
    # Get user input for month (all, january, february, ... , june).
    while True:
        month_input = input('\nPlease enter one of the assigned numbers to select a month: '
                            '\n\n1) January \n2) February \n3) March \n4) April \n5) May \n6) June \n7) All months \n\n- ')
        if month_input == 'x':
           return None, None, None
        elif month_input not in month_dict:
            time.sleep(0.5)
            print('\nThat is an invalid entry. \n')
            time.sleep(2)
        else:
            month = month_dict[month_input]
            time.sleep(0.5)
            print(f'\nGreat! You\'ve selected {month.title()}.')
            time.sleep(1)
            print('-'*40)
            break   
                
    # Defined a dictionary to map the assigned numbers to day options.              
    day_dict = {
        '1': 'sunday',
        '2': 'monday',
        '3': 'tuesday',
        '4': 'wednesday',
        '5': 'thursday',
        '6': 'friday',
        '7': 'saturday',
        '8': 'all'
    }
    # Get user input for day of week (all, monday, tuesday, ... sunday).
    while True:
        day_input = input('\nPlease enter one of the assigned numbers to select a day of the week: '
                      '\n\n1) Sunday \n2) Monday \n3) Tuesday \n4) Wednesday \n5) Thursday \n6) Friday \n7) Saturday \n8) All Days \n\n- ')
        if day_input == 'x':
           return None, None, None
        elif day_input not in day_dict:
            time.sleep(0.5)
            print('\nThat is an invalid entry. \n')
            time.sleep(2)
        else:
            day = day_dict[day_input]
            time.sleep(0.5)
            print(f'\nGreat! You\'ve selected {day.title()}.')
            time.sleep(1)
            break
        
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

    Expected Input: City, month, and day strings.
        Example Input: "chicago", "january", "wednesday"
    Expected Output: Pandas DataFrame containing filtered bikeshare data.
        Example Output: DataFrame with rows corresponding to bike rides in Chicago in January on Wednesdays.
    """
    # Load data from file for specified city.
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert 'Start Time' column to datetime format.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month from 'Start Time' column.
    df['Month'] = df['Start Time'].dt.month
    
    # Extract day of week from 'Start Time' column.
    df['Day of Week'] = df['Start Time'].dt.day_name()
    
    # Apply filters for month if applicable, create new df if filtered by month.
    # Added +1 after .index() to account for inclusivity.
    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month_num]
    
    # Apply filters for day if applicable, create new df if filtered by day.
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Expected Input: Pandas DataFrame containing bikeshare data.
        Example Input: DataFrame with filtered bikeshare data.
    Expected Output: Print statements displaying statistics on the most frequent times of travel.
        Example Output:
            The most common month to travel is: January
            The most common day to travel is: Wednesday
            The most common start hour is: 8    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    time.sleep(2)
    start_time = time.time()
    
    # Defined a dictionary to map month numbers to month names.
    month_names = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July'
    }

    # Display the most common month.
    most_common_month = df['Month'].mode()[0]
    month_name = month_names[most_common_month]
    print('\nThe most common month to travel is: ', month_name)
    
    # Display the most common day of week.
    most_common_day = df['Day of Week'].mode()[0]
    print('\nThe most common day to travel is: ', most_common_day)

    # Display the most common start hour.
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nThe most common start hour is: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(3)
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Expected Input: Pandas DataFrame containing bikeshare data.
        Example Input: DataFrame with filtered bikeshare data.
    Expected Output: Print statements displaying statistics on the most popular stations and trip.
        Example Output:
            The most commonly used start station is: Union Station
            The most commonly used end station is: Millennium Park
            The most frequent combination of start and end station trips is: Union Station to Millennium Park
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    time.sleep(2)
    start_time = time.time()

    # Display most commonly used start station.
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is: ', most_common_start_station)
          
    # Display most commonly used end station.
    most_common_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: ', most_common_end_station)

    # Display most frequent combination of start station and end station trip.
    df['Start-End Combo'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_startendcombo = df['Start-End Combo'].mode()[0]
    print('\nThe most frequest combination of start and end station trips is: ', most_common_startendcombo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(3)
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Expected Input: Pandas DataFrame containing bikeshare data.
        Example Input: DataFrame with filtered bikeshare data.
    Expected Output: Print statements displaying statistics on the total and average trip duration.
        Example Output:
            The total travel time for all trips was: 15 days, 10 hours, 25 minutes, and 30 seconds.
            The mean travel time for all trips was: 750 seconds
    """

    print('\nCalculating Trip Duration...\n')
    time.sleep(2)
    start_time = time.time()

    # Display total travel time.
    total_travel = df['Trip Duration'].sum()
    
    # Convert total_travel to day, hours, minutes, and seconds to improve readability.
    total_days = int(total_travel // (24 * 3600))
    total_remainder_hours = (total_travel % (24 * 3600))
    total_hours = int(total_remainder_hours // 3600)
    total_remainder_minutes = (total_remainder_hours % 3600)
    total_minutes = int(total_remainder_minutes // 60)
    total_seconds = int(total_remainder_minutes % 60)
    
    print('\nThe total travel time for all trips was:\n'
          f'\n{total_days} days, {total_hours} hours, {total_minutes} minutes, and {total_seconds} seconds.\n'
          f'\n(or {int(total_travel)} seconds)')

    # Display mean travel time.
    # Convert mean_travel_time to int to remove milliseconds.
    mean_travel_time = int(df['Trip Duration'].mean())
    print('\nThe mean travel time for all trips was: ', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(3)
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    
    Expected Input: Pandas DataFrame containing bikeshare data.
        Example Input: DataFrame with filtered bikeshare data.
    Expected Output: Print statements displaying statistics on bikeshare users.
        Example Output:
            Counts of user types:
            Subscriber: 500
            Customer: 100
            
            There were 300 males and 200 females.
            
            The earliest birth year was 1970.
            The most recent birth year was 1990.
            The most common birth year was 1985.    
    """

    print('\nCalculating User Stats...\n')
    time.sleep(2)
    start_time = time.time()

    # Display counts of user types.
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types: ')
    for user_type, count in user_types.items():
        print(f"{user_type}: {count}")

    # Display counts of gender.
    try:
        gender_count = df['Gender'].value_counts()
        male_count = gender_count['Male']
        female_count = gender_count['Female']
        print(f"\nThere were {male_count} males and {female_count} females.")
    # Handle the case where 'Male' or 'Female' keys are not present in gender_count.
    except KeyError:
        print("\nGender data not available.")

    # Display earliest, most recent, and most common year of birth.
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year was {earliest_birth_year}.")
        print(f"\nThe most recent birth year was {most_recent_birth_year}.")
        print(f"\nThe most common birth year was {most_common_birth_year}.")
    # Handle the case where 'Birth Year' column is not present in the df.
    except KeyError:
        print("\nBirth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(3)
    print('-'*40)

# Added ASCII art independent of definitions.  
bicycle_ascii_1 = """
-

-
 -
 -
-
"""

bicycle_ascii_2 = """
----
 |
  ---
 -   -
 -   -
  ---
"""

bicycle_ascii_3 = """
      ----
 ______|
  ---   ---
 -   - -   -
 -   - -   -
  ---   ---
"""
bicycle_ascii_4 = """
            -
       ______
        ---  
       -   - 
       -   - 
        ---  
"""

bicycle_ascii_5 = """
                 
             
              
            
            
              
"""

def main():
    while True:
        city, month, day = get_filters()
        if city is None:
            print('Exiting program...')
            break
            
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # Index df to allow user to view groups of raw data.
        start_index = 0
        
        print('\nWould you like to see 5 lines of raw data?')
        # While loop to allow for raw data viewing.
        while True:
            show_raw_data = input('\nEnter yes or no.\n'
                                  '\n- ').lower()
            if show_raw_data == 'x':
                print('Exiting program...')
                # Return to exit program.
                return
            elif show_raw_data == 'yes':
                time.sleep(1)
                print('\n')
                # Display the next 5 rows.
                print(df.iloc[start_index:start_index + 5])
                # Add 5 to start_index.
                start_index += 5
                time.sleep(3)
                print('\nWould you like to see 5 more lines of data?')
            elif show_raw_data == 'no':
                print('\n')
                time.sleep(1)
                break
            else:
                time.sleep(0.5)
                print('\n\nThat is an invalid entry. \n')
                time.sleep(2)

        restart = input('\nWould you like to restart?'
                        '\n\nEnter "yes" to restart or anything else to exit.\n\n -')
        if restart.lower() != 'yes':
            time.sleep(1)
            print('\nThank you for exploring US bikeshare data! Have a great day!\n')
            time.sleep(2)
            print(f'\n{bicycle_ascii_1}')
            time.sleep(0.5)
            print(f'\n{bicycle_ascii_2}')
            time.sleep(0.5)
            print(f'\n{bicycle_ascii_3}')
            time.sleep(0.5)
            print(f'\n{bicycle_ascii_4}')
            time.sleep(0.5)
            print(f'\n{bicycle_ascii_5}')
            break


if __name__ == "__main__":
	main()
