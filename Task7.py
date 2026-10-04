print("====================================")
print("=        Travel Planner            =")
print("====================================")
Destination = input("Destination: ")
Distance_in_kilometers = float(input("Distance in kilometers: "))
Average_speed_in_km_h = float(input("Average speed in km/h: "))
Time_in_hours = Distance_in_kilometers / Average_speed_in_km_h 
print("Time in hours:", Time_in_hours)