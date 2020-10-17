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
    cityi = input('please choose a city, "chicago, new york city, washington",: ')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while cityi.lower() not in ('chicago', 'new york city', 'washington'):
          print('please choose a valid city')
          cityi = input('please choose a city, "chicago, new york city, washington",: ')
          if cityi.lower() in ('chicago', 'new york city', 'washington'):
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    monthi = input('now lets pick a month,: ')
    while monthi.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
          print('please choose a valid month between january to june')
          monthi = input('please pick a month,: ')
          if monthi.lower() in ('january', 'february', 'march', 'april', 'may', 'june'):
                break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayi = input('now lets pick a day,: ')
    while dayi.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
          print('please choose a valid day such as: monday, tuesday, etc..')
          dayi = input('please pick a day,: ')
          if dayi.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                break
    city = cityi.lower()
    month = monthi.lower()
    day = dayi.lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #load_data()
    # TO DO: display the most common month
    montho = df['month'].mode()[0]

    # TO DO: display the most common day of week
    dayo = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('the most comon month is {}, the most comon day is {}, and the most popular hour {}'.format(montho, dayo, popular_hour))
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    start_and_end = (df['Start Station'] + df['End Station']).mode()[0]


    print('the most comon start station {}, and the most comon end station {}, and the most frequent combination of start station and end station trip {}'.format(start_time, end_station, start_and_end))
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration'])

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()

    print('total travel time {}, and average travel time {}'.format(total_travel, average_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    mini = min(df['Birth Year'])
    maxi = max(df['Birth Year'])
    comon = df['Birth Year'].mode()[0]

    print('the user counts {}, the gender counts {}, the earliest year {}, the most recent year {}, and the most comon year {},'.format(user_counts, gender_counts, mini, maxi, comon))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    more = input('would you like to see the raw data? Enter yes or no.\n')
    st = 0
    en = 5
    if more.lower() == 'yes':
        while True:
            print(df.iloc[st:en])
            st += 5
            en += 5
            more_da = input('would you like to see more data? Enter yes or no.\n')
            if more_da != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city in ('washington'):
            print('there is no user info for this city')
        else:
            user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
