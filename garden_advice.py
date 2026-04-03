def get_gardening_advice(season, plant_type):
    """
    Returns specific gardening advice based on the season and plant type.
    Uses dictionary lookups instead of long if-elif chains.
    """
    
    # Data stored in dictionaries for easy updates
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Prepare the soil and plant early seeds.",
        "autumn": "Clear fallen leaves and prepare for the cold."
    }

    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Trim regularly to encourage new growth."
    }

    # Retrieve advice with a fallback default if the key isn't found
    s_info = season_advice.get(season.lower(), "No advice for this season.")
    p_info = plant_advice.get(plant_type.lower(), "No advice for this type of plant.")

    return f"{s_info}\n{p_info}"

def main():
    # TODO: Replace with input() to allow user interaction (addressed below)
    current_season = input("Enter the current season (e.g., summer, winter): ").strip()
    current_plant = input("Enter the plant type (e.g., flower, vegetable): ").strip()

    # Get and print the advice
    result = get_gardening_advice(current_season, current_plant)
    print("\n--- Your Gardening Advice ---")
    print(result)

if __name__ == "__main__":
    main()
