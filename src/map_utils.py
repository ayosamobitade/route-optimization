# src/map_utils.py

from typing import List, Optional
import folium
from folium import Map, Marker, Icon, PolyLine
from folium.plugins import MarkerCluster
import pandas as pd


def create_map(
    center: Optional[List[float]] = None, 
    zoom_start: int = 12
) -> Map:
    """
    Initialize a Folium map centered at given coordinates.

    Args:
        center (Optional[List[float]]): [latitude, longitude]. If None, defaults to (0, 0).
        zoom_start (int): Initial zoom level of the map.

    Returns:
        folium.Map: Initialized map object.
    """
    if center is None:
        center = [0.0, 0.0]
    return folium.Map(location=center, zoom_start=zoom_start)


def add_clustered_markers(
    map_obj: Map, 
    locations: pd.DataFrame,
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    popup_cols: Optional[List[str]] = None,
    icon_color: str = "blue",
    icon_prefix: str = "fa",
    icon_name: str = "truck"
) -> None:
    """
    Add clustered markers to the map for given locations.

    Args:
        map_obj (folium.Map): Folium map object to add markers on.
        locations (pd.DataFrame): DataFrame with location data.
        lat_col (str): Column name for latitude.
        lon_col (str): Column name for longitude.
        popup_cols (Optional[List[str]]): List of columns to include in popup text.
        icon_color (str): Color of the marker icon.
        icon_prefix (str): Icon prefix for FontAwesome icons.
        icon_name (str): Icon name for the marker.

    Returns:
        None
    """
    marker_cluster = MarkerCluster().add_to(map_obj)

    for _, row in locations.iterrows():
        location = [row[lat_col], row[lon_col]]
        popup_text = ""
        if popup_cols:
            popup_text = "<br>".join(f"{col}: {row[col]}" for col in popup_cols)

        marker = Marker(
            location=location,
            popup=popup_text,
            tooltip=popup_text if popup_text else None,
            icon=Icon(color=icon_color, icon=icon_name, prefix=icon_prefix)
        )
        marker.add_to(marker_cluster)


def draw_route(
    map_obj: Map, 
    route_coords: List[List[float]], 
    color: str = "red", 
    weight: int = 5, 
    opacity: float = 0.8
) -> None:
    """
    Draw a polyline route on the map connecting the given coordinates.

    Args:
        map_obj (folium.Map): Folium map object.
        route_coords (List[List[float]]): List of [latitude, longitude] points in order.
        color (str): Line color.
        weight (int): Line thickness.
        opacity (float): Line opacity.

    Returns:
        None
    """
    PolyLine(route_coords, color=color, weight=weight, opacity=opacity).add_to(map_obj)


def save_map(map_obj: Map, filepath: str) -> None:
    """
    Save the Folium map to an HTML file.

    Args:
        map_obj (folium.Map): Map object to save.
        filepath (str): Path to save the HTML file.

    Returns:
        None
    """
    map_obj.save(filepath)
