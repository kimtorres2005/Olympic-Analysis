import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
def load_data():
    """
    Loads the datasets into Pandas DataFrames.
    """
    dictionary_df = pd.read_csv("dictionary.csv")
    summer_df = pd.read_csv("summer.csv")
    winter_df = pd.read_csv("winter.csv")
    return dictionary_df, summer_df, winter_df

# Step 2: Analyze Questions
def most_gold_medals(summer_df, winter_df):
    """
    Finds the countries with the most gold medals overall.
    """
    gold_medals_summer = summer_df[summer_df["Medal"] == "Gold"].groupby("Country").size()
    gold_medals_winter = winter_df[winter_df["Medal"] == "Gold"].groupby("Country").size()
    total_gold_medals = gold_medals_summer.add(gold_medals_winter, fill_value=0).sort_values(ascending=False)
    
    # Ensure the result is in int64
    total_gold_medals = total_gold_medals.astype('int64')
    
    print("\nTop 10 countries with the most gold medals overall:")
    print(total_gold_medals.head(10))
    # Save plot to file
    total_gold_medals.head(10).plot(kind="bar", title="Top 10 Countries with Most Gold Medals")
    plt.ylabel("Number of Gold Medals")
    plt.savefig("gold_medals.png")
    plt.show()

def medals_over_time(summer_df, winter_df, country="USA"):
    """
    Analyzes how the number of medals won by a specific country has changed over time.
    """
    summer_medals = summer_df[summer_df["Country"] == country].groupby("Year").size()
    winter_medals = winter_df[winter_df["Country"] == country].groupby("Year").size()
    total_medals = summer_medals.add(winter_medals, fill_value=0).sort_index()
    
    # Ensure the result is in int64
    total_medals = total_medals.astype('int64')
    
    print(f"\nMedals won by {country} over time:")
    print(total_medals)
    # Plot the total medals over time
    total_medals.plot(kind="line", title=f"Medals won by {country} Over Time", xlabel="Year", ylabel="Number of Medals")
    plt.savefig(f"medals_over_time_{country}.png")
    plt.show()

def most_medals_by_athlete(summer_df, winter_df):
    """
    Finds the athletes who have won the most medals in a single Olympics.
    """
    summer_medals = summer_df.groupby(["Year", "Athlete"]).size()
    winter_medals = winter_df.groupby(["Year", "Athlete"]).size()
    total_medals = pd.concat([summer_medals, winter_medals]).sort_values(ascending=False)
    
    # Ensure the result is in int64
    total_medals = total_medals.astype('int64')
    
    print("\nTop 10 athletes with the most medals in a single Olympics:")
    print(total_medals.head(10))
    # Plotting the top athletes with the most medals
    total_medals.head(10).plot(kind="bar", title="Top 10 Athletes with Most Medals in a Single Olympics")
    plt.ylabel("Number of Medals")
    plt.savefig("top_athletes.png")
    plt.show()

# Additional function: Medals by Gender
def medals_by_gender(summer_df, winter_df):
    """
    Analyzes how many medals were won by male vs female athletes.
    """
    gender_medals_summer = summer_df.groupby("Gender").size()
    gender_medals_winter = winter_df.groupby("Gender").size()
    total_gender_medals = gender_medals_summer.add(gender_medals_winter, fill_value=0)
    
    # Ensure the result is in int64
    total_gender_medals = total_gender_medals.astype('int64')
    
    print("\nMedals won by gender:")
    print(total_gender_medals)
    # Plot the medals by gender
    total_gender_medals.plot(kind="pie", title="Medals won by Gender", autopct='%1.1f%%')
    plt.ylabel("")
    plt.savefig("medals_by_gender.png")
    plt.show()

# Main Program
def main():
    try:
        # Load data
        dictionary_df, summer_df, winter_df = load_data()
        
        # Question 1: Most gold medals overall
        most_gold_medals(summer_df, winter_df)
        
        # Question 2: Medals won by a specific country over time
        medals_over_time(summer_df, winter_df, country="USA")
        
        # Question 3: Most medals by an athlete in a single Olympics
        most_medals_by_athlete(summer_df, winter_df)
        
        # Additional Analysis: Medals by Gender
        medals_by_gender(summer_df, winter_df)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
