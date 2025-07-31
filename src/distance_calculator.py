# src/distance_calculator.py

from typing import List, Tuple, Optional
import math
import requests
import pandas as pd


def haversine_distance(
    coord1: Tuple[float, float], 
    coord2: Tuple[float, float]
) -> float:
    """
    Calculate the Haversine distance between two latitude/longitude points.

    Args:
        coord1 (Tuple[float, float]): (latitude, longitude) of the first point.
        coord2 (Tuple[float, float]): (latitude, longitude) of the second point.

    Returns:
        float: Distance between points in meters.
    """
    R = 6371000  # Earth radius in meters

    lat1_rad = math.radians(coord1[0])
    lon1_rad = math.radians(coord1[1])
    lat2_rad = math.radians(coord2[0])
    lon2_rad = math.radians(coord2[1])

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance


def create_distance_matrix(
    locations: List[Tuple[float, float]]
) -> List[List[float]]:
    """
    Create a symmetric distance matrix (in meters) using Haversine distances.

    Args:
        locations (List[Tuple[float, float]]): List of (latitude, longitude) tuples.

    Returns:
        List[List[float]]: 2D distance matrix.
    """
    size = len(locations)
    matrix: List[List[float]] = []

    for i in range(size):
        row: List[float] = []
        for j in range(size):
            dist = haversine_distance(locations[i], locations[j]) if i != j else 0.0
            row.append(dist)
        matrix.append(row)

    return matrix


def get_google_distance_matrix(
    origins: List[Tuple[float, float]],
    destinations: List[Tuple[float, float]],
    api_key: str
) -> Optional[List[List[float]]]:
    """
    Query Google Distance Matrix API for travel distances (in meters).

    Args:
        origins (List[Tuple[float, float]]): List of origin coordinates.
        destinations (List[Tuple[float, float]]): List of destination coordinates.
        api_key (str): Your Google Maps API key.

    Returns:
        Optional[List[List[float]]]: Distance matrix in meters, or None if failed.
    """
    origin_str = "|".join([f"{lat},{lon}" for lat, lon in origins])
    destination_str = "|".join([f"{lat},{lon}" for lat, lon in destinations])

    url = (
        "https://maps.googleapis.com/maps/api/distancematrix/json"
        f"?origins={origin_str}&destinations={destination_str}&key={api_key}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Google API request failed with status code {response.status_code}")
        return None

    data = response.json()

    if data.get("status") != "OK":
        print(f"Google API returned error status: {data.get('status')}")
        return None

    distance_matrix: List[List[float]] = []

    for row in data["rows"]:
        distances_row = []
        for element in row["elements"]:
            if element.get("status") == "OK":
                distances_row.append(element["distance"]["value"])  # meters
            else:
                distances_row.append(float('inf'))  # unreachable
        distance_matrix.append(distances_row)

    return distance_matrix


def get_osrm_distance(
    coord1: Tuple[float, float],
    coord2: Tuple[float, float],
    osrm_server_url: str = "http://router.project-osrm.org"
) -> Optional[float]:
    """
    Query OSRM API for driving distance between two points (meters).

    Args:
        coord1 (Tuple[float, float]): (lat, lon) start point.
        coord2 (Tuple[float, float]): (lat, lon) end point.
        osrm_server_url (str): OSRM server URL.

    Returns:
        Optional[float]: Distance in meters or None if request failed.
    """
    url = (
        f"{osrm_server_url}/route/v1/driving/"
        f"{coord1[1]},{coord1[0]};{coord2[1]},{coord2[0]}"
        "?overview=false"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "routes" in data and len(data["routes"]) > 0:
            return data["routes"][0]["distance"]
    except Exception as e:
        print(f"OSRM request failed: {e}")

    return None
