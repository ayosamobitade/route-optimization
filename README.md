# Delivery Route Optimization

A Python project to optimize delivery routes for logistics companies using real-world map data. The system finds the most efficient routes to minimize travel distance/time, simulating what services like Amazon, DHL, or Uber Eats use behind the scenes.

---

## Features

- Load delivery locations with latitude and longitude.
- Calculate distance matrices using Haversine formula or external APIs.
- Optimize routes using Google OR-Tools solving Traveling Salesman Problem (TSP).
- Visualize delivery points and optimized routes on interactive maps with Folium.
- Simulate driver progress along the optimized route.
- Interactive web app built with Streamlit for route visualization.

---

## Project Structure
```
route-optimization/
│
├── data/
│ ├── locations.csv # Delivery addresses with latitude/longitude
│ └── distance_matrix.csv # Optional precomputed distances
│
├── notebooks/
│ ├── 01_data_visualization.ipynb
│ ├── 02_optimize_routes.ipynb
│ └── 03_real_world_maps.ipynb
│
├── src/
│ ├── init.py
│ ├── map_utils.py # Map creation and visualization helpers
│ ├── distance_calculator.py # Distance calculation utilities
│ ├── route_optimizer.py # Route optimization using OR-Tools
│ └── simulate_driver.py # Driver route simulation script
│
├── app/
│ ├── streamlit_app.py # Streamlit app for route visualization
│ ├── requirements.txt
│ └── route_result.json # JSON file with optimized route order
│
├── tests/
│ └── test_optimizer.py # Unit tests for route optimizer
│
├── README.md
├── LICENSE
├── .gitignore
└── setup.py
```
