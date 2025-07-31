# src/route_optimizer.py

from typing import List, Optional
from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def optimize_route(
    distance_matrix: List[List[int]], 
    num_vehicles: int = 1, 
    depot: int = 0
) -> Optional[List[int]]:
    """
    Optimize the delivery route using OR-Tools.

    Args:
        distance_matrix (List[List[int]]): Square matrix of distances between points (int, e.g., meters).
        num_vehicles (int): Number of vehicles for routing problem (default is 1 for TSP).
        depot (int): Index of the depot/start location.

    Returns:
        Optional[List[int]]: Ordered list of location indices representing the optimal route,
                             or None if no solution found.
    """
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index: int, to_index: int) -> int:
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Set the cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.seconds = 30  # Optional time limit for solver

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        route_indices: List[int] = []
        for vehicle_id in range(num_vehicles):
            index = routing.Start(vehicle_id)
            while not routing.IsEnd(index):
                node_index = manager.IndexToNode(index)
                route_indices.append(node_index)
                index = solution.Value(routing.NextVar(index))
            # Add the depot at end (optional, to complete route)
            route_indices.append(manager.IndexToNode(index))
        return route_indices
    else:
        return None
