import pandas as pd

# Load the dataset
file_path = "/app/all_pref_DID_TFP.csv"
data = pd.read_csv(file_path)

# The percentage of increasing TFP
percentage = float(input('The percentage of increasing TFP \
per year(0.01, 0.02, 0.03 and so on---> '))

# Function to calculate the average rank change for each prefecture
def calculate_rank_change(data, increase=percentage):
    rank_changes = (
        {}
    )  # Dictionary to store the average rank changes for each prefecture

    # Loop through each prefecture
    for prefecture in data["prefecture"].unique():
        pref_data = data[data["prefecture"] == prefecture]  # 特定の都道府県のデータを選択
        changes = []  # 順位変動を格納するリスト

        # Loop through each year
        for year in data["year"].unique():
            year_data = data[data["year"] == year].copy()  # 特定の年度のデータを選択（コピーを作成）

            # Rank based on TFP
            year_data["rank"] = year_data["TFP"].rank(ascending=False, method="min")
            original_rank = year_data.loc[
                year_data["prefecture"] == prefecture, "rank"
            ].iloc[0]

            # Increase TFP by increased percentage points
            increased_tfp = (
                pref_data.loc[pref_data["year"] == year, "TFP"].iloc[0] + increase
            )
            year_data.loc[year_data["prefecture"] == prefecture, "TFP"] = increased_tfp

            # Recalculate ranks with the increased TFP
            year_data["rank_increased"] = year_data["TFP"].rank(
                ascending=False, method="min"
            )
            new_rank = year_data.loc[
                year_data["prefecture"] == prefecture, "rank_increased"
            ].iloc[0]

            # Calculate the rank change and add it to the list
            rank_change = original_rank - new_rank
            changes.append(rank_change)

        # Calculate the average rank change
        average_change = sum(changes) / len(changes)
        rank_changes[prefecture] = average_change

    return rank_changes


# Calculate the average rank change for each prefecture
average_rank_changes = calculate_rank_change(data)

# Calculate the national average from the dictionary of average rank changes for each prefecture
all_prefectures_average = sum(average_rank_changes.values()) / len(average_rank_changes)

average_rank_changes["national average"] = all_prefectures_average
# Display the results
print(average_rank_changes)
