# Creating a HashMap (dictionary in Python)
hash_map = {}

# Insert operation
def insert(key, value):
    hash_map[key] = value
    print(f"Inserted ({key}: {value})")

# Update operation
def update(key, value):
    if key in hash_map:
        hash_map[key] = value
        print(f"Updated ({key}: {value})")
    else:
        print(f"Key '{key}' not found. Cannot update.")

# Delete operation
def delete(key):
    if key in hash_map:
        del hash_map[key]
        print(f"Deleted key '{key}'")
    else:
        print(f"Key '{key}' not found. Cannot delete.")

# Search operation
def search(key):
    if key in hash_map:
        print(f"Found: ({key}: {hash_map[key]})")
    else:
        print(f"Key '{key}' not found.")

# Display the hashmap
def display():
    if not hash_map:
        print("HashMap is empty.")
    else:
        print("Current HashMap contents:")
        for key, value in hash_map.items():
            print(f"{key}: {value}")

# Example usage:
insert("name", "Alice")
insert("age", 30)
search("name")
update("age", 31)
delete("name")
display()
