# Name project: Bikeshare United States
# Author: Camilo Jiménez

# Import libraries
import time
import pandas as pd
import numpy as np

# Import data
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Functions provide information according to user criteria


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to know your data? \n")
        city = city.lower()
        if city in ["chicago", "new york city", "washington"]:
            break
        else:
            print(
                "Please enter a city from the following options: Chicago, New York City or Washington \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "If you want to filter by month, please enter a month between January and June. Else, please write 'all' \n")
        month = month.lower()
        if month in ['january', 'febrary', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Please enter a month between January and June or write 'all' \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "If you want to filter by day, please enter a day. Else write 'all' \n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Please enter a day between Monday and Sunday \n")

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

    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    # Start Time is converted because its data type is object
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    # I create two columns: 'month' and 'day_of_week'
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'febrary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day of the week is: ",
          df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    print("The most common start hour is: ",
          df['Start Time'].dt.hour.mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ",
          df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ",
          df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df["Start Station"] + " - " + df["End Station"]
    print("The most frequent combination (Start Station - End station) is: ",
          df['combination'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: ", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The mean travel time is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")

    # TO DO: Display counts of gender
    if city != 'washington':
        gen = df.groupby(['Gender'])['Gender'].count()
        print("Count of gender is: ", gen)

        # TO DO: Display earliest, most recent, and most common year of birth
        eyb = sorted(df.groupby(['Birth Year'])[
                     'Birth Year'], reverse=True)[0][0]
        print("The earliest year of birth is: ", eyb, "\n")
        mryb = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        print("The most recent year of birth is: ", mryb, "\n")
        mcyb = df['Birth Year'].mode()[0]
        print("The most common year of birth is: ", mcyb, "\n")
    else:
        print("Washington doesn´t have data about 'Gender' and 'Birth Year'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Show row data (print 5 rows of the data until he/she says no)
    x = 0
    while True:
        raw_data = input("Would you like to see raw data? Enter yes or no. \n")
        if raw_data.lower() == "yes":
            print(df[x:x+5])
            x = x+5
        else:
            break


def restart():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__restart__":
    restart()
