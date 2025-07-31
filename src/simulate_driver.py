from typing import List, Tuple
import time
import math


def haversine_distance(
    coord1: Tuple[float, float], 
    coord2: Tuple[float, float]
) -> float:
    """
    Calculate Haversine distance between two geo points in kilometers.

    Args:
        coord1 (Tuple[float, float]): (latitude, longitude) of first point.
        coord2 (Tuple[float, float]): (latitude, longitude) of second point.

    Returns:
        float: Distance in kilometers.
    """
    R = 6371.0  # Earth radius in km

    lat1_rad = math.radians(coord1[0])
    lon1_rad = math.radians(coord1[1])
    lat2_rad = math.radians(coord2[0])
    lon2_rad = math.radians(coord2[1])

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def simulate_route(
    route_coords: List[Tuple[float, float]], 
    average_speed_kmh: float = 40.0, 
    pause_seconds: float = 1.0
) -> None:
    """
    Simulate driving the delivery route step-by-step, printing distance and estimated time.

    Args:
        route_coords (List[Tuple[float, float]]): Ordered list of (latitude, longitude) coordinates.
        average_speed_kmh (float): Average driving speed in km/h.
        pause_seconds (float): Seconds to pause between steps to simulate real-time.

    Returns:
        None
    """
    total_distance = 0.0
    total_time_hours = 0.0

    print("Starting delivery route simulation...\n")

    for i in range(len(route_coords) - 1):
        start = route_coords[i]
        end = route_coords[i + 1]

        distance_km = haversine_distance(start, end)
        time_hours = distance_km / average_speed_kmh

        total_distance += distance_km
        total_time_hours += time_hours

        print(f"Leg {i + 1}:")
        print(f"  From: {start}")
        print(f"  To:   {end}")
        print(f"  Distance: {distance_km:.2f} km")
        print(f"  Estimated travel time: {time_hours * 60:.1f} minutes\n")

        # Pause to simulate travel time passing (can adjust or remove)
        time.sleep(pause_seconds)

    print("Route simulation complete.")
    print(f"Total distance: {total_distance:.2f} km")
    print(f"Estimated total travel time: {total_time_hours * 60:.1f} minutes")


# Example usage:
if __name__ == "__main__":
    # Example route coordinates (lat, lon)
    example_route = [
        (6.5244, 3.3792),  # Depot/start
        (6.465422, 3.406448),
        (6.4310, 3.4231),
        (6.5244, 3.3792)   # Return to depot
    ]

    simulate_route(example_route)
