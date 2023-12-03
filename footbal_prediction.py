# Predicting multiple matches

prediction_count = 2  # Number of future matches to predict

for _ in range(prediction_count):
    print("\n--- Predicting Future Match ---")
    home_team = input("Enter the name of the home team: ")
    away_team = input("Enter the name of the away team: ")

    home_goals = int(input(f"Enter the number of goals scored by {home_team}: "))
    away_goals = int(input(f"Enter the number of goals scored by {away_team}: "))

    print("\nPrediction:")



def predict_match(home_team, away_team, home_goals, away_goals):
    if home_goals > away_goals:
        result = f"{home_team} wins!"
    elif home_goals < away_goals:
        result = f"{away_team} wins!"
    else:
        result = "It's a draw!"

    print(f"{home_team} vs {away_team}")
    print(f"Result: {result}")

# Predicting multiple matches

prediction_count = 2  # Number of future matches to predict

for i in range(prediction_count):
    print("\n--- Predicting Future Match ---")
    home_team = input("Enter the name of the home team: ")
    away_team = input("Enter the name of the away team: ")

    home_goals = int(input(f"Enter the number of goals scored by {home_team}: "))
    away_goals = int(input(f"Enter the number of goals scored by {away_team}: "))

    print("\nPrediction:")
    predict_match(home_team, away_team, home_goals, away_goals)

