# Weather Data Project - Milestone 3
# Functions for calculating meteorlogical data

def calculate_wind_chill(temp, ws):

    # Checks if Wind Chill Formula is Valid
    if temp > 50 or ws <= 3:
        return None

    # Calculates Wind Chill Factor
    wind_chill = (
        35.74
        + (0.6215 * temp)
        - (35.75 * (ws ** 0.16))
        + (0.4275 * temp * (ws ** 0.16))

        )

    return wind_chill

def calculate_cloud_base(temp, dew_point):

    # Calculates Temperature Spread
    temperature_spread = temp - dew_point

    # Calculates Cloud Base Altitude in Feet
    cloud_base = (temperature_spread / 4.4) * 1000

    return cloud_base

if __name__ == "__main__":
    print("Testing Weather Calculations")
    print("Wind Chill:", calculate_wind_chill(40,10))
    print("Cloud Base:", calculate_cloud_base(50,40))
    print("Invalid Wind Chill:", calculate_wind_chill(60,10))
