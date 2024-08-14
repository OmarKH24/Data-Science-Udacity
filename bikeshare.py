import time
import pandas as pd
import numpy as np

# updated line by refactoring

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cites = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "tuesday", "sunday", "all"]
              

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    city = ''
    month = ''
    day = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_valid = False 
    while not input_valid:
        city = input("Please Enter The City Name (chicago, new york city, washington): ").strip().lower()
        if(city in cites):
            input_valid = True
        else:
            print("Invalid city name. Please try again.")
        

    # TO DO: get user input for month (all, january, february, ... , june)
    input_valid = False
    while not input_valid:
        month = input("Please Enter The Month (all, january, february, ... , june): ").strip().lower()
        if(month in months):
            input_valid = True
        else:
            print("Invalid Month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    input_valid = False
    while not input_valid:
        day = input("Please Enter The Day Of Week (all, monday, tuesday, ... sunday): ").strip().lower()
        if(day in days):
            input_valid = True
        else:
            print("Invalid Day. Please try again.")

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
    """
    df = pd.read_csv(CITY_DATA[city])    
    # Convert the 'Start Time' column to 'Date' datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Convert the 'End Time' column to 'Date' datatype
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extract month and day from 'Start Time'
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all':
        df = df[df['day'] == day]

    print("Filtered Data Frame:")
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0] # get the most common month
    print(f"The Most Common Month in the DataFrame is: {common_month}") 
    
    
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0] # get the most common day
    print(f"The Most Common Day in the DataFrame is: {common_day}") # print the day

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.strftime('%H') # get the start hours
    common_start_hour = df['start_hour'].mode()[0] # get the most common start hour
    print(f"The Most Common Start Hour in the DataFrame is: {common_start_hour}") # print the start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0] # get the most common start station
    print(f"The Most Common Start Station in the DataFrame is: {common_start_station}") # print the most common start station

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0] # get the most common end station
    print(f"The Most Common End Station in the DataFrame is: {common_end_station}") # print the most common end station


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Destination'] = df['Start Station'] + ', to ' + df['End Station']
    common_combination = df['Trip Destination'].mode()[0]
    print(f"The Most Frequent Combination of start station and end station trip in the DataFrame is: {common_combination}") # print the most common combination


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Total Travel Time'] = df['End Time'] - df['Start Time']
    print(df['Total Travel Time'])

    # TO DO: display mean travel time
    mean_travel_time = df['Total Travel Time'].mean()
    print(f"The Mean Travel Time in the DataFrame is: {mean_travel_time}") # print the mean_travel_time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts() # get counts of each value in the 'User Type' column in the DataFrame
    print(user_types_counts) # print the counts for each value in the 'User Type' column in the DataFrame

    # only available for NYC and Chicago 
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]

        print(f"The Earliest Year of Birth in the DataFrame is: {earliest_birth_year}") # print the earliest_birth_year
        print(f"The Most Recent Year of Birth in the DataFrame is: {recent_birth_year}") # print the recent_birth_year
        print(f"The Most Common Year of Birth in the DataFrame is: {common_birth_year}") # print the common_birth_year



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
