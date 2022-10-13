from statistics import mean
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
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    #  HINT: Use a while loop to handle invalid inputs
    city = (input("Enter the city you want to explore the data (Valid Options are Chicago, New York City, Washington)").lower()).strip()
    errorentry = 0

    while city not in  CITY_DATA.keys():
        errorentry += 1
        city = (input("Please Enter a valid input for the city from the list:Chicago, New York City, Washington").lower()).strip()


    # get user input for month (all, january, february, ... , june)
    month = (input("Enter the month to explore the data(Valid options are All, January, February, March, April, May and June)").lower()).strip()

    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month =  (input("Please Enter a valid input for the month from the list:All, January, February', March, April, May, June").lower()).strip()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day to explore the data(Valid Options are All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday").lower().strip()

    while day not in  ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = (input("Please Enter a valid input for the month from the list:All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday").lower()).strip()

    city = city.title()
    month = month.title()
    day = day.title()

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
    """
    print ('Data Filtering based on ', city, month, day )
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city.lower()))

    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    if month != 'All':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_month)


    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of week:', popular_day)

    # display the most common start hour
    popular_hour = (df['Start Time'].dt.strftime('%-H')).mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular Start Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Comb Station'] = df['Start Station'] + df['End Station']
    popular_comb_station = df['Comb Station'].mode()[0]
    print('Most Popular Start Station:', popular_comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600.0
    print('Total Travel Time in hours:', int(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60.0
    print('Mean Travel Time', int(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type Counts:', user_types)


    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender count', gender_count)
    except:
        print('No Gender column exists for the selected file')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('Earliest Birth Year', earliest_birth_year)
        print('Recent Birth Year', recent_birth_year)
        print('Common Birth Year',common_birth_year)
    except:
        print('No Details of Birth Year Exisits')

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
