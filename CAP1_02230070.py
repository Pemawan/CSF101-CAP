################################
# Pema Wangmo
# 1st Year Electrical department
# 02230070
################################
# REFERENCES
# https://chat.openai.com/
################################
# SOLUTION
# Your Solution Score:49894
# CSF101-CAP/input_0_cap1.txt
def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            input_file = [line.strip().replace(' ', '') for line in lines]  # Extract and format conditions pairs
            return input_file
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def calculate_score(input_file):
    # Creating a dictionary to store scores for each condition
    scores = {'AX': 3, 'AY': 4, 'AZ': 8,
              'BX': 1, 'BY': 5, 'BZ': 9,
              'CX': 2, 'CY': 6, 'CZ': 7}

    # Initializing total score
    total_score = 0
    
    # Initializing index for while loop
    i = 0
    # Calculating total score using a while loop
    while i < len(input_file):
        condition = input_file[i]
        total_score += scores[condition]
        i += 1

    # Returning the total score
    return total_score

# Input file path
input_file_path = 'CSF101-CAP/input_0_cap1.txt'
input_data = read_input(input_file_path)
if input_data:
    total_score = calculate_score(input_data)
    print(f"Total score: {total_score}")
