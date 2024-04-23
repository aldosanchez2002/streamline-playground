import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook

# Disable PyplotGlobalUseWarning
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

def main():
    st.title("Daily Calories Tracker")

    # Create an empty DataFrame to store the data
    df = pd.DataFrame(columns=['Date', 'Calories'])

    # Display input box for entering daily calories
    new_calories = st.number_input('Enter your daily calories:', value=0, step=1)

    # Submit button
    if st.button('Submit'):
        # Add new entry to DataFrame
        df = df.append({'Date': pd.to_datetime('today'), 'Calories': new_calories}, ignore_index=True)

        # Display the updated DataFrame
        st.write("Updated data:")
        st.write(df)

        # Calculate total calories
        total_calories = df['Calories'].sum()
        st.write(f"Total calories: {total_calories}")

        # Plot the data
        st.write("Calories over time:")
        plt.plot(df['Date'], df['Calories'])
        plt.xlabel('Date')
        plt.ylabel('Calories')
        st.pyplot()

if __name__ == "__main__":
    main()
