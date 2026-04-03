"""
Garden Advice Tool
------------------
A modular script that provides seasonal and plant-specific gardening tips 
for enthusiasts worldwide. This version uses dictionary-based lookups 
for better maintainability and scalability.

Author: jprhs11
"""

def get_gardening_advice(season, plant_type):
    """
    Retrieves gardening tips by matching user inputs against advice dictionaries.
    
    Args:
        season (str): The current time of year (e.g., 'summer').
        plant_type (str): The category of plant (e.g., 'vegetable').
        
    Returns:
        str: A combined string of seasonal and plant-specific advice.
    """
    
    # Season-specific tips stored in a dictionary to avoid long if-elif chains
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Prepare the soil and plant early seeds.",
        "autumn": "Clear fallen leaves and prepare for the cold."
    }

    # Plant-specific tips for better modularity
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Trim regularly to encourage new growth."
    }

    # Retrieve advice with .get() to handle unknown inputs gracefully
    s_info = season_advice.get(season.lower(), "No advice for this season.")
    p_info = plant_advice.get(plant_type.lower(), "No advice for this type of plant.")

    return f"{s_info}\n{p_info}"

def main():
    """
    Handles user interaction and coordinates the advice generation process.
    """
    # Capture user input and remove extra whitespace
    current_season = input("Enter the current season (e.g., summer, winter): ").strip()
    current_plant = input("Enter the plant type (e.g., flower, vegetable): ").strip()

    # Generate and display the results
    result = get_gardening_advice(current_season, current_plant)
    print("\n--- Your Gardening Advice ---")
    print(result)

# Entry point for the script
if __name__ == "__main__":
    main()
