"""
This program do:
1. Load winequality-red.csv and winequality-white.csv as separate Dataframes,
add wine_type column and merge into a single Dataframe.
2. Filter by `quality`:
    - High-quality wines (`quality >= 7`)
    - Low-quality wines (`quality <= 4`)
3. Compute the average alcohol content for:
    - High-quality wines
    - Low-quality wines
4. Print result in console.
"""
import transform
import pandas as pd


def main():
    # Extract data

    # Read data from csv files
    white_wine = pd.read_csv("winequality-white.csv", sep=";")
    red_wine = pd.read_csv("winequality-red.csv", sep=";")



    # Transform the data

    # Add a column to each dataframe to indicate the wine type
    transform.add_column(white_wine, "wine_type", "white")
    transform.add_column(red_wine, "wine_type", "red")

    # Merge the dataframes
    wines = pd.concat([white_wine, red_wine])

    # Filter the data to get high-quality and low-quality wines
    high_quality_wines = transform.filter_by_quality(wines, 7)
    low_quality_wines = transform.filter_by_quality(wines, 4, True)

    # Compute the average alcohol content for high-quality and low-quality wines
    high_quality_alcohol = transform.count_avarage_alcohol(high_quality_wines)
    low_quality_alcohol = transform.count_avarage_alcohol(low_quality_wines)



    # Display the data

    # To set display options to show all columns and rows:

    # 1) Set display options by uncommenting the following lines:
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # 2) Remove head from the print statements below
    print("Wine data:")
    print(wines.head(10))

    print("\nHigh-quality wines:")
    print(high_quality_wines.head(10))
    print("\nAverage alcohol content for high-quality wines: {:.2f}".format(high_quality_alcohol))

    print("\nLow-quality wines:")
    print(low_quality_wines.head(10))
    print("Average alcohol content for low-quality wines: {:.2f}".format(low_quality_alcohol))

if __name__=="__main__":
    main()