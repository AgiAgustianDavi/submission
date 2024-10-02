import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

# function to prepare dataset
def create_year_rentals_df(df):
    year_rentals_df = df.groupby(by='yr').cnt.sum().sort_values().reset_index()
    return year_rentals_df

def create_total_rentals_2011_df(df):
    year2011_df = df[df['yr'] == 2011]
    total_rental_2011_df = year2011_df.groupby(by='mnth').cnt.sum().reset_index().sort_values(by='mnth', ascending=True)
    return total_rental_2011_df


def create_total_rentals_2012_df(df):
    year2012_df = df[df['yr'] == 2012]
    total_rental_2012_df = year2012_df.groupby(by='mnth').cnt.sum().reset_index().sort_values(by='mnth', ascending=True)
    return total_rental_2012_df

def create_total_rentals_season_df(df):
    total_rental_season_df = df.groupby(by='season').cnt.sum().sort_values(ascending=False).reset_index()
    return total_rental_season_df
    

def create_total_rentals_weathersit_df(df):
    total_rental_weathersit_df = df.groupby(by='weathersit').cnt.sum().sort_values(ascending=False).reset_index()
    return total_rental_weathersit_df

def create_total_rentals_day_df(df):
    total_rental_day_df = df.groupby(by='weekday').cnt.sum().reset_index().sort_values(by='cnt', ascending=False)
    return total_rental_day_df

def create_proportion_users(df):
    total_casual = df['casual'].sum()
    total_registered = df['registered'].sum()
    return total_casual, total_registered

def create_rentals_hours(df):
    rentals_hours_df = df.groupby(by='hr').cnt.sum().reset_index()
    return rentals_hours_df

def create_rentals_holiday_df(df):
    rental_holiday_df = df.groupby(by='holiday').cnt.sum().sort_values(ascending=False).reset_index()
    return rental_holiday_df

def create_rentals_weekend_df(df):
    rental_weekend_df = df.groupby(by='weekend').cnt.sum().sort_values(ascending=False).reset_index()
    return rental_weekend_df

def create_rentals_workingday_df(df):
    rental_workingday_df = df.groupby(by='workingday').cnt.sum().sort_values(ascending=False).reset_index()
    return rental_workingday_df

def assign_high_color(df):
    max_rentals= df['cnt'].max()
    colors = ['#FF0000' if x == max_rentals else '#1f77b4' for x in df['cnt']]
    return colors

# load cleaned dataset
df = pd.read_csv("dashboard/main_data.csv")

# Streamlit layout
st.title("🚴‍♂️ Bike Sharing Data Dashboard")
st.markdown("""
Welcome to the Bike Sharing Data Dashboard! This dashboard provides a comprehensive analysis of bike rental data, allowing you to explore key metrics like rentals by year, month, season, weather, and more. 
Use the **sidebar** to filter data by date range and discover insights into user behaviors.
""")

# Sidebar for date filtering
st.sidebar.header("Filter by Date Range")
min_date = pd.to_datetime(df['dteday']).min()
max_date = pd.to_datetime(df['dteday']).max()

# Streamlit sidebar input for date range
start_date, end_date = st.sidebar.date_input(
    label='Select Date Range',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Filter dataset by selected date range
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

main_df = df[(pd.to_datetime(df['dteday']) >= start_date) & (pd.to_datetime(df['dteday']) <= end_date)]

#prepare the datasets will we used
year_rentals_df = create_year_rentals_df(main_df)
total_rental_2011_df = create_total_rentals_2011_df(main_df)
total_rental_2012_df = create_total_rentals_2012_df(main_df)
total_rental_season_df = create_total_rentals_season_df(main_df)
total_rental_weathersit_df = create_total_rentals_weathersit_df(main_df)
total_rental_day_df = create_total_rentals_day_df(main_df)
rentals_hours_df = create_rentals_hours(main_df)
rental_holiday_df = create_rentals_holiday_df(main_df)
rental_weekend_df = create_rentals_weekend_df(main_df)
rental_workingday_df = create_rentals_workingday_df(main_df)

# visualization: Total Bike Rentals by Year
st.subheader("📅 Total Bike Rentals by Year")

fig, ax = plt.subplots(figsize=(12, 6))

# Assign color
max_rentals= year_rentals_df['cnt'].max()
colors = ['#FF0000' if x == max_rentals else '#1f77b4' for x in year_rentals_df['cnt']]

sns.barplot(
    y= 'cnt',
    x= 'yr',
    data= year_rentals_df,
    palette= colors,
    ax=ax
)

ax.set_title("Total Bike Rentals by Year", fontsize=18)
ax.set_ylabel("Total Rentals (in Millions)", fontsize=12)
ax.set_xlabel("Year", fontsize=12)

st.pyplot(fig)

# Visualization: Total Bike Rentals by Month (2011 & 2012)
st.subheader("📊 Total Bike Rentals by Month (2011 vs 2012)")

fig, ax = plt.subplots(figsize=(12,6))

# Plot for 2011
ax.plot(
    total_rental_2011_df['mnth'],
    total_rental_2011_df['cnt'],
    marker='o',
    linewidth=2,
    color='#1f77b4',
    label='2011'
)

# Plot for 2012
ax.plot(
    total_rental_2012_df['mnth'],
    total_rental_2012_df['cnt'],
    marker='o',
    linewidth=2,
    color='#FF0000',
    label='2012'
)

ax.set_title("Total Bike Rentals by Month", fontsize=18)
ax.set_ylabel("Total Rentals", fontsize=12)
ax.set_xlabel("Month", fontsize=12)
ax.legend(fontsize=12)

st.pyplot(fig)

# visualization: Total Bike Rentals by Season & Weathersit
st.subheader("🌦 Total Bike Rentals by Weather and Season")

col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots()
    sns.barplot(
        x="cnt", 
        y="weathersit", 
        data=total_rental_weathersit_df, 
        palette=assign_high_color(total_rental_weathersit_df), 
        ax=ax
    )
    ax.set_title("By Weather Condition")
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.barplot(
        x="cnt", 
        y="season", 
        data=total_rental_season_df, 
        palette=assign_high_color(total_rental_season_df), 
        ax=ax
    )
    ax.set_title("By Season")
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    st.pyplot(fig)

# visualization: Total Bike Rentals by Days
st.subheader("📅 Total Bike Rentals by Days")

fig, ax = plt.subplots(figsize=(12,6))

# Bar for Days
sns.barplot(
    x="cnt", 
    y="weekday",
    data= total_rental_day_df,
    palette= assign_high_color(total_rental_day_df)
)
ax.set_title("Rentals by Days", loc="center", fontsize=18)
ax.set_ylabel(None)
ax.set_xlabel(None)

st.pyplot(fig)

# Visualization: Proportion of users
st.subheader("👥 Proportion of Casual vs Registered Users")

fig, ax = plt.subplots(figsize=(6, 6))
total_casual, total_registered = create_proportion_users(main_df)
sizes = [total_casual, total_registered]
labels = ['Casual Users', 'Registered Users']
colors = ['#1f77b4', '#FF0000']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Users", fontsize=16)

st.pyplot(fig)

# Visulaization: Hours with Highest Bike Rentals
st.subheader("⏰ Hours with Highest Bike Rentals ")

fig, ax = plt.subplots(figsize=(12, 6))

# Bar plot for Hours
sns.barplot(
    x = 'hr',
    y = 'cnt',
    data = rentals_hours_df,
    palette = assign_high_color(rentals_hours_df),
    ax = ax
)

ax.set_title('Top 5 Hours with Highest Bike Rentals', fontsize=18)
ax.set_xlabel('Hour of the Day', fontsize=12)

st.pyplot(fig)



# Visualization: Rentals on Holidays, Weekends, and Working Days
st.subheader("🏖 Rentals on Holidays, Weekends, and Working Days")

# Plot 1: Rentals on Holidays
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    y = 'cnt',
    x = 'holiday',
    data = rental_holiday_df,
    palette = assign_high_color(rental_holiday_df),
    ax = ax
)
ax.set_title("Rentals on Holidays", fontsize=15)

st.pyplot(fig)

# Plot 2: Rentals on Weekends
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    y = 'cnt',
    x = 'weekend',
    data = rental_weekend_df,
    palette = assign_high_color(rental_weekend_df),
    ax=ax
)
ax.set_title("Rentals on Weekends", fontsize=15)

st.pyplot(fig)

# Plot 3: Rentals on Working Days
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    y = 'cnt',
    x = 'workingday',
    data = rental_workingday_df,
    palette = assign_high_color(rental_workingday_df),
    ax=ax
)
ax.set_title("Rentals on Working Days", fontsize=15)

st.pyplot(fig)

