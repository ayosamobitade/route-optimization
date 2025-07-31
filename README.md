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

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/route-optimization.git
cd route-optimization
```
    Create a virtual environment and activate it (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

    Install dependencies:

pip install -r app/requirements.txt

## Usage
### Jupyter Notebooks
- `01_data_visualization.ipynb`: Explore and visualize delivery locations on maps.
- `02_optimize_routes.ipynb`: Run route optimization on delivery points.
- `03_real_world_maps.ipynb`: Visualize optimized routes on real-world maps.

### Run Streamlit App
```bash
streamlit run app/streamlit_app.py
```
Open the URL shown in your browser to interact with the route optimization app.

## Data Format
- `locations.csv` should contain at least these columns:

|id	| address | latitude | longitude |
|----|----|-----|-----|
| 0 | Depot Address | 6.5244 | 3.3792 |
| 1 | Customer 1 | 6.465422 | 3.406448 |
| ... | ... | ... | ... |

- `route_result.json` is a JSON array of location IDs in the optimized visiting order, e.g.:

```json
[0, 3, 5, 2, 7, 4, 1, 6, 0]
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Google OR-Tools for optimization algorithms.
- Folium for map visualizations.
- Streamlit for easy web app creation.