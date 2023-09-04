\* Car_Dealership_Problem *\
Minimize
Sum_of_Transport_Costs: 23 Route_A_1 + 64 Route_A_2 + 15 Route_A_3
 + 53 Route_B_1 + 25 Route_B_2 + 35 Route_B_3 + 66 Route_C_1 + 69 Route_C_2
 + 100 Route_C_3 + 8 Route_D_1 + 27 Route_D_2 + 124 Route_D_3 + 77 Route_E_1
 + 82 Route_E_2 + 13 Route_E_3
Subject To
Sum_of_Products_into_dealership1: Route_A_1 + Route_B_1 + Route_C_1
 + Route_D_1 + Route_E_1 >= 250
Sum_of_Products_into_dealership2: Route_A_2 + Route_B_2 + Route_C_2
 + Route_D_2 + Route_E_2 >= 250
Sum_of_Products_into_dealership3: Route_A_3 + Route_B_3 + Route_C_3
 + Route_D_3 + Route_E_3 >= 250
Sum_of_Products_out_of_factory_A: Route_A_1 + Route_A_2 + Route_A_3 <= 100
Sum_of_Products_out_of_factory_B: Route_B_1 + Route_B_2 + Route_B_3 <= 50
Sum_of_Products_out_of_factory_C: Route_C_1 + Route_C_2 + Route_C_3 <= 50
Sum_of_Products_out_of_factory_D: Route_D_1 + Route_D_2 + Route_D_3 <= 75
Sum_of_Products_out_of_factory_E: Route_E_1 + Route_E_2 + Route_E_3 <= 500
Bounds
 0 <= Route_A_1
 0 <= Route_A_2
 0 <= Route_A_3
 0 <= Route_B_1
 0 <= Route_B_2
 0 <= Route_B_3
 0 <= Route_C_1
 0 <= Route_C_2
 0 <= Route_C_3
 0 <= Route_D_1
 0 <= Route_D_2
 0 <= Route_D_3
 0 <= Route_E_1
 0 <= Route_E_2
 0 <= Route_E_3
Generals
Route_A_1
Route_A_2
Route_A_3
Route_B_1
Route_B_2
Route_B_3
Route_C_1
Route_C_2
Route_C_3
Route_D_1
Route_D_2
Route_D_3
Route_E_1
Route_E_2
Route_E_3
End
