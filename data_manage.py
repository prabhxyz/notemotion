def add_data(text, emotion, score):
    import json
    from datetime import datetime

    # Load existing data from the .json file
    existing_data = {}
    filename = "data/record.json"
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        pass

    # Get the current date in "yyyy-mm-dd" format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Collect data for the current date
    new_data = {
        "text": text,
        "emotion": emotion,
        "score": score
    }

    # Update the existing_data dictionary with the new data for the current date
    existing_data[current_date] = new_data

    # Write the updated data back to the .json file
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)

def journal_done():
    import json
    from datetime import datetime

    # Load existing data from the .json file
    existing_data = {}
    filename = "data/record.json"
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        pass

    # Get the current date in "yyyy-mm-dd" format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Check if there is an entry for the current date
    if current_date in existing_data:
        return True
    else:
        return False
