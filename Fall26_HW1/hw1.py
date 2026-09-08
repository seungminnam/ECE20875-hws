def roster_overlap(sections: dict) -> dict:
    # sections is a dictionary where keys are section names (strings) and values are lists of student names

    # Edge case: no sections at all -> nothing to union or intersect => results should be empty 
    if not sections:
        return {
            'all_students': set(),
            'in_every_section': set(),
            'in_multiple_sections': set()
        }

    # Convert each section's student list to a set (= collapse duplicates)
    # names within one section (e.g. ["eve", "eve"] -> {"eve"}) before we start counting.
    section_sets = [set(names) for names in sections.values()]

    # Union of every set = every student who appears in at least one section.
    all_students = set.union(*section_sets)

    # Intersection of every set = students common to ALL sections at once.
    in_every_section = set.intersection(*section_sets)

    # "In multiple sections" => count >= 2
    student_cnt = {}
    for students in section_sets:
        for student in students:
            student_cnt[student] = student_cnt.get(student, 0) + 1
    
    in_multiple_sections = set()
    for student, cnt in student_cnt.items():
        if cnt > 1:
            in_multiple_sections.add(student)

    return {
        'all_students': all_students,
        'in_every_section': in_every_section,
        'in_multiple_sections': in_multiple_sections
    }

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here

    #extract data from dictionary:
    data = input_dictionary['data']
    n = input_dictionary['n']
    min_val = input_dictionary['min_val']
    max_val = input_dictionary['max_val']

    #error handling 
    if min_val == max_val:
        print('Error: min_val and max_val are the same value')
        return []
    
    #n should be a positive integer:
    if type(n) != int or n <= 0:
        return []
    
    if min_val > max_val:
        max_val, min_val = min_val, max_val
    
    #initializing histogram as a list of n zeros
    hist = [0] * n

    #calculating bin width
    w = (max_val-min_val)/n 

    #check data and put it on the right bin
    for val in data:
        #range: [min_val, max_val)
        if val <= min_val or val >= max_val:
            continue
        
        #index = floor((value-min_val)/w)
        i = int((val - min_val) / w)
        hist[i] += 1

    # return the variable storing the histogram
    # Output should be a list
    return hist


# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def moving_window_stats(data_dict: dict, k: int) -> dict:
    # data_dict is a dictionary where keys are sensor names (strings) and values are lists of numbers (numerical readings - floats or int)
    # k is the window size (positive integer); assume k>=1

    # Write your code here

    # The function first initializes an empty dictionary to store results.  
    results_dict = {}
    '''
    example:
    data = [1,2,3,4,5] (l=5), k = 3 => 3 sliding windows ([1,2,3], [2,3,4], [3,4,5])

    data = [1,2,3,4,5,6] (l=6), k=2 => 5 sliding windows ([1,2], [2,3],...,[5,6])

    hence, window # = l-k+1 => becomes the param of range()
    '''
    # For each sensor in the input dictionary:
    for sensor, readings in data_dict.items():
        #check if the length of data list is sufficient (k>=1)
        # If the list of readings is shorter than the window size k, the result for that sensor is an empty list.
        if len(readings) < k:
            results_dict[sensor] = []

        #   Otherwise, it iterates through the list using a range that allows for a window of size k.
        else:
            stats_list = []
            
            for start in range(len(readings)-k+1):
                end = start+k
                curr_window = readings[start:end] #list slicing

                #   For each window, it calculates the minimum, maximum, and average values.
                min_val = min(curr_window)
                max_val = max(curr_window)
                avg_val = sum(curr_window) / len(curr_window)

                #   It stores these three values in a tuple and adds the tuple to a result list for that sensor.
                stats_list.append((min_val, max_val, avg_val))

            results_dict[sensor] = stats_list

    # return the dictionary with sensor names as keys and lists of tuples (min, max, avg) as values
    # Finally, it returns the dictionary containing the lists of calculated stats.
    return results_dict


