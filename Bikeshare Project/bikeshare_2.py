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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please enter your desired city name, one of the following: [chicago, new york city, washington]\n").lower()
            file_name = CITY_DATA[city]
            break
        except KeyError:
            print("\n----- You entered an invalid city name! -----\n")

    # get user input for month (all, january, february, ... , june)
    month = input("Please enter the month you want to filter with, one of the following: [all, january, february, march, april, may, june]\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day you want to filter with, one of the following: [all, monday, tuesday, wednsday, thursday, friday, saturday, sunday]\n").lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print("The most common Month is: {}".format(months[common_month-1]))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common Day is: {}".format(common_day))

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common Start Hour is: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common End Station is: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ":" + df['End Station']
    frequent_station_combination = df['Station Combination'].mode()[0]
    freq_start, freq_end = frequent_station_combination.split(':')
    print("The most frequent combination of start station and end station trip is FROM {} TO {}".format(freq_start, freq_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: {}s".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("The mean travel time is: {}s".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of each user type is:\n{}".format(user_types))

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("The count of each gender is:\n{}".format(gender_count))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        sorted_df = df.sort_values(by=['Birth Year'], ascending=True)
        yob_list = list(sorted_df['Birth Year'].dropna())
        print("The earliest year of birth is: {}".format(yob_list[0]))
        print("The most recent year of birth is: {}".format(yob_list[-1]))
        print("The most common year of birth is: {}".format(sorted_df['Birth Year'].mode()[0]))
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

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

        display = input('\nWant to display first 5 lines of raw data? Enter yes or no.\n')
        if display.lower() == 'yes':
            count_start, count_end = 0, 5
            while count_end <= df.shape[0]:
                print(df[count_start:count_end])
                next_display = input('\nWant to display next 5 lines of raw data? Enter yes or no.\n')
                if next_display.lower() == 'yes':
                    count_start += 5
                    count_end += 5
                else:
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
