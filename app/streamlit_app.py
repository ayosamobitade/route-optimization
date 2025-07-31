
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json
from typing import List


def load_locations(filepath: str) -> pd.DataFrame:
    """
    Load delivery locations from a CSV file.

    Args:
        filepath (str): Path to CSV file.

    Returns:
        pd.DataFrame: DataFrame containing locations with latitude, longitude, and address.
    """
    df = pd.read_csv(filepath)
    required_cols = {"id", "latitude", "longitude", "address"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_cols}")
    return df


def load_route(filepath: str) -> List[int]:
    """
    Load optimized route as a list of location IDs from JSON.

    Args:
        filepath (str): Path to JSON route file.

    Returns:
        List[int]: Ordered list of location IDs.
    """
    with open(filepath, "r") as f:
        route = json.load(f)
    if not isinstance(route, list):
        raise ValueError("Route JSON must be a list of location IDs")
    return route


def create_route_map(locations: pd.DataFrame, route: List[int]) -> folium.Map:
    """
    Create a Folium map with delivery locations and route lines.

    Args:
        locations (pd.DataFrame): DataFrame with location data.
        route (List[int]): Ordered list of location IDs for the route.

    Returns:
        folium.Map: Folium map object.
    """
    # Center map on average coordinates
    center_lat = locations['latitude'].mean()
    center_lon = locations['longitude'].mean()
    route_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Get locations in route order
    route_locs = locations.set_index("id").loc[route]

    # Add markers
    for idx, row in route_locs.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"ID: {row['id']}<br>Address: {row['address']}",
            tooltip=f"Stop {route.index(row['id']) + 1}",
            icon=folium.Icon(color='blue', icon='truck', prefix='fa')
        ).add_to(route_map)

    # Draw route polyline
    points = route_locs[['latitude', 'longitude']].values.tolist()
    folium.PolyLine(points, color="red", weight=5, opacity=0.8).add_to(route_map)

    return route_map


def main() -> None:
    st.title("Delivery Route Optimization")

    st.sidebar.header("Settings")
    locations_path = st.sidebar.text_input("Locations CSV Path", "data/locations.csv")
    route_path = st.sidebar.text_input("Route JSON Path", "app/route_result.json")

    # Load data
    try:
        locations = load_locations(locations_path)
        route = load_route(route_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    st.subheader("Delivery Locations")
    st.dataframe(locations)

    st.subheader("Optimized Route Order")
    st.write(route)

    st.subheader("Route Map")
    route_map = create_route_map(locations, route)

    # Display map using streamlit-folium
    st_folium(route_map, width=700, height=500)


if __name__ == "__main__":
    main()
