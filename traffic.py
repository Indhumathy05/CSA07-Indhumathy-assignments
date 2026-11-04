
# Computer Networks Assignment 1
# Task 1 - Traffic Calculation

robots = 40 * 200 * 8 / 0.002 / 1_000_000
sensors = 600 * 50 * 8 / 1_000_000
cctv = 24 * 4
office = 150 * 0.10 * 2

total = robots + sensors + cctv + office
plant = total * 8

print("Robot traffic:", robots, "Mbps")
print("Sensor traffic:", sensors, "Mbps")
print("CCTV traffic:", cctv, "Mbps")
print("Office traffic:", office, "Mbps")
print("One line total:", total, "Mbps")
print("8-line plant:", plant, "Mbps")

new_total = robots + sensors + cctv * 0.05 + office

print("One line with local CCTV:", new_total, "Mbps")
print("8-line plant with local CCTV:", new_total * 8, "Mbps")
