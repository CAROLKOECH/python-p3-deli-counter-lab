def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        line_status = "The line is currently:"
        for idx, name in enumerate(katz_deli, start=1):
            line_status += f" {idx}. {name}"
        return line_status

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    return f"Welcome, {name}. You are number {position} in line."

def now_serving(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"
    else:
        serving_name = katz_deli.pop(0)
        return f"Currently serving {serving_name}."

# Test cases
katz_deli = []
print(take_a_number(katz_deli, "Ada"))  # Output: Welcome, Ada. You are number 1 in line.
print(take_a_number(katz_deli, "Grace"))  # Output: Welcome, Grace. You are number 2 in line.
print(take_a_number(katz_deli, "Kent"))  # Output: Welcome, Kent. You are number 3 in line.

print(line(katz_deli))  # Output: "The line is currently: 1. Ada 2. Grace 3. Kent"

print(now_serving(katz_deli))  # Output: "Currently serving Ada."

print(line(katz_deli))  # Output: "The line is currently: 1. Grace 2. Kent"

print(take_a_number(katz_deli, "Matz"))  # Output: Welcome, Matz. You are number 3 in line.

print(line(katz_deli))  # Output: "The line is currently: 1. Grace 2. Kent 3. Matz"

print(now_serving(katz_deli))  # Output: "Currently serving Grace."

print(line(katz_deli))  # Output: "The line is currently: 1. Kent 2. Matz"
