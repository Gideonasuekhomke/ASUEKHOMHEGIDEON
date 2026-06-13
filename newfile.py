# python_test.py

# === Problem 1: Variables and Data Types ===
print("=== Problem 1 ===")

# 1. Create variables
market_name = "Balogun Market"
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False

# 2. Print variables and their types
print(f"Market: {market_name}, Type: {type(market_name)}")
print(f"Traders: {num_traders}, Type: {type(num_traders)}")
print(f"Coordinates: {location_coords}, Type: {type(location_coords)}")
print(f"Open Sundays: {is_open_sundays}, Type: {type(is_open_sundays)}")

# 3. Calculate and print average daily revenue
total_revenue = 25000000
average_revenue = total_revenue / num_traders
print(f"Average Daily Revenue per Trader: {average_revenue} Naira")
print()


# === Problem 2: Lists and Basic Operations ===
print("=== Problem 2 ===")
host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]

# 4. Add "Ivory Coast" to the end
host_countries.append("Ivory Coast")

# 5. Insert "Morocco" at position 1
host_countries.insert(1, "Morocco")

# 6. Remove "Senegal"
host_countries.remove("Senegal")

# 7. Print total number of countries
print("Total number of countries:", len(host_countries))

# 8. Print in alphabetical order without modifying original
print("Alphabetical order:", sorted(host_countries))

# 9. Print every second country using slicing
print("Every second country:", host_countries[::2])
print()


# === Problem 3: Dictionaries ===
print("=== Problem 3 ===")
river_data = {
    "Nile": {"length_km": 6650, "countries": 11},
    "Congo": {"length_km": 4700, "countries": 9},
    "Niger": {"length_km": 4180, "countries": 5}
}

# 10. Add Zambezi river
river_data["Zambezi"] = {"length_km": 2574, "countries": 6}

# 11. Update Niger river countries
river_data["Niger"]["countries"] = 6

# 12. Print all river names
print("River names:")
for river in river_data:
    print(river)

# 13. Print number of countries for Congo
print("Countries Congo flows through:", river_data["Congo"]["countries"])

# 14. Calculate total length of all rivers
total_length = 0
for river in river_data:
    total_length += river_data[river]["length_km"]
print("Total combined length of all rivers:", total_length)
print()


# === Problem 4: Loops ===
print("=== Problem 4 ===")

print("--- Part A: For Loops ---")
# 15. Multiplication table of 7
print("Multiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# 16. Print each letter in AFRICA
print("Letters in AFRICA:")
for letter in "AFRICA":
    print(letter)

# 17. Sum of even numbers from 1 to 50
sum_evens = 0
for num in range(1, 51):
    if num % 2 == 0:
        sum_evens += num
print("Sum of even numbers from 1 to 50:", sum_evens)

print("--- Part B: While Loop ---")
# 18. Count down from 20 to 1
print("Countdown:")
count = 20
while count > 0:
    print(count)
    count -= 1

# 19. First number > 500 divisible by 3 and 7
search_num = 501
while True:
    if search_num % 3 == 0 and search_num % 7 == 0:
        print("First number > 500 divisible by 3 and 7 is:", search_num)
        break # Exit the loop once we find it
    search_num += 1
print()


# === Problem 5: Conditional Statements ===
print("=== Problem 5 ===")

def classify_rainfall(mm):
    # Check highest condition first and work down
    if mm > 300:
        return "Flood Risk"
    elif mm >= 200:
        return "Heavy Rain"
    elif mm >= 100:
        return "Moderate Rain"
    elif mm >= 1:
        return "Light Rain"
    else:
        return "Dry"

# Test the function with the given values
test_values = [350, 250, 150, 50, 0]
for value in test_values:
    print(f"{value}mm: {classify_rainfall(value)}")
print()


# === Problem 6: Functions ===
print("=== Problem 6 ===")

print("--- Part A ---")
# Function to calculate exchange rate
def calculate_exchange(amount, rate):
    return amount * rate

# Test Part A
print(calculate_exchange(100, 1580))


print("--- Part B ---")
# Function with a default parameter for currency
def format_price(amount, currency="NGN"):
    # Using :, formats the number with commas (e.g. 5000 -> 5,000)
    return f"{currency} {amount:,}"

# Test Part B
print(format_price(5000))           
print(format_price(200, "GHS"))     


print("--- Part C ---")
# Function returning multiple values
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    # Average is sum of all scores divided by the number of scores
    average = sum(scores) / len(scores)
    
    return lowest, highest, average

# Test Part C
test_scores = [55, 72, 88, 61, 94, 47, 79]
low, high, avg = analyze_scores(test_scores)
print(f"Lowest score: {low}")
print(f"Highest score: {high}")
print(f"Class average: {avg}")