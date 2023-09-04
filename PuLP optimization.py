# PuLP problem solving
# car dealership problem

"""
There are five vehicle factories (A, B, C, D, E) that provide vehicles to 3 dealerships (1, 2, 3).
Transport costs are miles between the factory and dealerships.
Goal is to provide enough vehicles to the dealerships at the cheapest transportation cost.
"""

from pulp import *

# creates a list of all the supply nodes (factories)
factories = ["A","B","C","D","E"]

# number of vehicles for each supply node
supply = {"A": 100, "B": 50, "C": 50, "D": 75, "E":500}

#list of all demand nodes (car dealerships)
dealerships = ["1", "2", "3"]

# number of vehicles demanded by each dealership
demand = {
    "1": 250,
    "2": 250,
    "3": 250,
}

# costs of each possible transportation path
costs = [  # dealerships
    # 1 2 3
    [23, 64, 15],  # A  factories
    [53, 25, 35],  # B
    [66, 69, 100],  # C
    [8, 27, 124],  # D
    [77, 82, 13]   # E
]

costs = makeDict([factories, dealerships], costs, 0)

prob = LpProblem("Car Dealership Problem", LpMinimize)

routes = [(f, d) for f in factories for d in dealerships]

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route", (factories, dealerships), 0, None, LpInteger)

# Objective function
prob += (
    lpSum([vars[f][d] * costs[f][d] for (f, d) in routes]),
    "Sum_of_Transport_Costs",
)

# supply constraints
for f in factories:
    prob += (
        lpSum([vars[f][d] for d in dealerships]) <= supply[f],
        f"Sum_of_Products_out_of_factory_{f}",
    )

# demand constraints
for d in dealerships:
    prob += (
        lpSum([vars[f][d] for f in factories]) >= demand[d],
        f"Sum_of_Products_into_dealership{d}",
    )

prob.writeLP("CarDealershipProblem.lp")
prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Transport = ", value(prob.objective))