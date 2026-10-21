"""
Read cat information from a comma-separated text file.
Used with a cat_file.txt file containing cat records in the format: "id,name,age".
"""


def get_cats_info(path):
    """Return cat records as dictionaries with id, name and age keys."""
    # Initialize an empty list to store cat records
    cats = []

    try:
        # Read the file
        with open(path, encoding="utf-8") as file:
            # Loop through each line in the file, starting the line number count at 1
            for line_number, line in enumerate(file, start=1):
                # Strip whitespace from the line
                line = line.strip()
                # Skip empty lines
                if not line:
                    continue

                # Split the line into fields using a comma as the delimiter
                fields = line.split(",")
                # Strip whitespace from each field and create a tuple
                cat_tuple = tuple(field.strip() for field in fields)
                # Validate that the tuple has exactly 3 elements and that none of them are empty
                if len(cat_tuple) != 3 or not all(cat_tuple):
                    # Raise a ValueError with a message indicating the line number of the invalid record
                    raise ValueError(f"Invalid cat record on line {line_number}")

                # Unpack the tuple into cat_id, name, and age
                cat_id, name, age = cat_tuple
                # Append a dictionary with the cat's information to the list of cats
                cats.append({"id": cat_id, "name": name, "age": age})
    # Handle the case where the file does not exist
    except FileNotFoundError:
        return []

    return cats

# Assign the result of get_cats_info to cats_info and print the results
cats_info = get_cats_info("cat_file.txt")
print(cats_info)
# [{'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'}, {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'}, {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'}, {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'}, {'id': '60b90c4613067a15887e1ae5', 'name': 'Tessi', 'age': '5'}]
