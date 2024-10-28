import pandas as pd
import random
import matplotlib.pyplot as plt


def speed_dynamic():
    # Load dataset
    file_path = 'data\\2023-12-29 15-16-43.csv'  # Replace with your actual file path
    data = pd.read_csv(file_path)

    # Define constants for liability and premium calculations
    L_base = 100000  # Base liability (max liability)
    P_base = 200     # Base monthly premium
    k = 1000         # Liability reduction factor
    m = 10           # Premium increase factor

    # Ensure dataset has at least 10 rows
    if len(data) < 10:
        raise ValueError("Dataset has fewer than 10 rows. Please provide a larger dataset.")

    # Select 10 consecutive random rows for speed samples
    start_index = random.randint(0, len(data) - 1000)
    sample_data = data.iloc[start_index:start_index + 1000]
    speeds = sample_data["Vehicle speed (km/h)"]

    # Define scoring functions for each policy
    def calculate_scores(speed):
        return {
            'Total Coverage': 0.1 * speed + 0.2 * (L_base - k * speed) + 0.3 * (L_base - k * speed),
            'Economic': 0.7 * speed + 0.7 * (L_base - k * speed) + 0.7 * (L_base - k * speed),
            'Balanced': 0.3 * speed + 0.3 * (L_base - k * speed) + 0.4 * (L_base - k * speed)
        }

    # Calculate liabilities and premiums for each policy based on speed
    liabilities = {'Total Coverage': [], 'Economic': [], 'Balanced': []}
    premiums = {'Total Coverage': [], 'Economic': [], 'Balanced': []}

    for speed in speeds:
        scores = calculate_scores(speed)
        for policy, score in scores.items():
            liabilities[policy].append(L_base - k * score * score)
            premiums[policy].append(P_base + m * (L_base - score))
    return liabilities,premiums,speeds

if __name__ == "__main__":
    liabilities,premiums,speeds = speed_dynamic()
    # Plot speed on the x-axis and liability/premium on the y-axes
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot liability for each policy in the desired order
    liability_order = ['Economic', 'Balanced', 'Total Coverage']
    for policy in liability_order:
        ax1.plot(speeds, liabilities[policy], label=f"{policy} Liability", linestyle='-', marker='o')
    ax1.set_xlabel("Speed (km/h)")
    ax1.set_ylabel("Liability ($)", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a secondary y-axis for premiums
    ax2 = ax1.twinx()
    premium_order = ['Economic', 'Balanced', 'Total Coverage']
    for policy in premium_order:
        ax2.plot(speeds, premiums[policy], label=f"{policy} Premium", linestyle='--', marker='x')
    ax2.set_ylabel("Monthly Premium ($)", color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Add legends for clarity
    #fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

    # Show the plot
    plt.title("Insurance Policy Liability and Premium vs. Speed")
    plt.show()