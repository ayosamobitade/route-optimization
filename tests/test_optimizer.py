
import unittest
from src.route_optimizer import optimize_route
from typing import List


class TestRouteOptimizer(unittest.TestCase):
    def setUp(self) -> None:
        # A simple symmetric distance matrix for 4 nodes
        # Distances in meters
        self.distance_matrix: List[List[int]] = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0],
        ]

    def test_optimize_route_single_vehicle(self):
        route = optimize_route(self.distance_matrix, num_vehicles=1, depot=0)
        self.assertIsNotNone(route, "No solution found by optimizer")
        self.assertIsInstance(route, list, "Route should be a list")
        self.assertTrue(all(isinstance(i, int) for i in route), "Route elements should be integers")
        self.assertEqual(route[0], 0, "Route should start at depot index 0")
        self.assertEqual(route[-1], 0, "Route should end at depot index 0")
        # Check route length (should include all nodes + return to depot)
        self.assertEqual(len(route), len(self.distance_matrix) + 1)


if __name__ == "__main__":
    unittest.main()
