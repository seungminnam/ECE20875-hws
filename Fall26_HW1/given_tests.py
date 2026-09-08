# given_tests.py
# Test functions provided to students for testing their implementations

from hw1 import roster_overlap, histogram, moving_window_stats


def run_problem1_tests():
    """Problem 1: Roster overlap tests"""
    print("=== Problem 1: Roster Overlap Tests ===\n")

    # Test 1
    print("Test 1:")
    sections = {
        "Section1": ["ana", "ben", "cara"],
        "Section2": ["ben", "cara", "dan"],
        "Section3": ["cara", "dan"]
    }
    output = roster_overlap(sections)
    print(f"Sections: {sections}")
    print(f"Output:   {output}")
    print("Expected: {'all_students': {'ana', 'ben', 'cara', 'dan'}, "
          "'in_every_section': {'cara'}, 'in_multiple_sections': {'ben', 'cara', 'dan'}}\n")

    # Test 2
    print("Test 2:")
    sections = {
        "Section1": ["eve", "eve", "frank"],
        "Section2": ["gina"]
    }
    output = roster_overlap(sections)
    print(f"Sections: {sections}")
    print(f"Output:   {output}")
    print("Expected: {'all_students': {'eve', 'frank', 'gina'}, "
          "'in_every_section': set(), 'in_multiple_sections': set()}\n")


def run_problem2_tests():
    """Problem 2: Histogram function tests"""
    print("=== Problem 2: Histogram Tests ===\n")

    # Test 1
    print("Test 1:")
    data = [-2, -2.2, 0, 5.6, 8.3, 10.1, 30, 4.4, 1.9, -3.3, 9, 8]
    input_dictionary = {'data': data, 'n': 15, 'min_val': -5, 'max_val': 10}
    output = histogram(input_dictionary)
    print(f"Data: {data}")
    print(f"Bins: 15, Min: -5, Max: 10")
    print(f"Output:   {output}")
    print(f"Expected: [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 2, 1]\n")

    # Test 2
    print("Test 2:")
    data = [-4, -3.2, 0, 7.6, 1.0, 2.2, 30, 2.2, 1.9, -8.3, 6, 5]
    input_dictionary = {'data': data, 'n': 10, 'min_val': 10, 'max_val': 0}
    output = histogram(input_dictionary)
    print(f"Data: {data}")
    print(f"Bins: 10, Min: 10, Max: 0")
    print(f"Output:   {output}")
    print(f"Expected: [0, 2, 2, 0, 0, 1, 1, 1, 0, 0]\n")

    # Test 3
    print("Test 3:")
    data = [2, 2, 2]
    input_dictionary = {'data': data, 'n': 5, 'min_val': -2, 'max_val': 3}
    output = histogram(input_dictionary)
    print(f"Data: {data}")
    print(f"Bins: 5, Min: -2, Max: 3")
    print(f"Output:   {output}")
    print(f"Expected: [0, 0, 0, 0, 3]\n")

    # Test 4
    print("Test 4:")
    data = [-1, -1, -1, 10, 10]
    input_dictionary = {'data': data, 'n': 5, 'min_val': -1, 'max_val': 10}
    output = histogram(input_dictionary)
    print(f"Data: {data}")
    print(f"Bins: 5, Min: -1, Max: 10")
    print(f"Output:   {output}")
    print(f"Expected: [0, 0, 0, 0, 0]\n")


def run_problem3_tests():
    """Problem 3: Moving Window Statistics tests"""
    print("=== Problem 3: Moving Window Statistics Tests ===\n")

    # Test 1
    print("Test 1:")
    data = {
        "Sensor_A": [1, 2, 3, 4, 5],
        "Sensor_B": [10, 20]
    }
    k = 3
    output = moving_window_stats(data, k)
    expected = {
        "Sensor_A": [(1, 3, 2.0), (2, 4, 3.0), (3, 5, 4.0)],
        "Sensor_B": []
    }
    print(f"Data: {data}, k={k}")
    print(f"Output:   {output}")
    print(f"Expected: {expected}\n")

    # Test 2
    print("Test 2:")
    data = {"Temp": [20.0, 21.0, 22.5]}
    k = 2
    output = moving_window_stats(data, k)
    expected = {"Temp": [(20.0, 21.0, 20.5), (21.0, 22.5, 21.75)]}
    print(f"Data: {data}, k={k}")
    print(f"Output:   {output}")
    print(f"Expected: {expected}\n")

    # Test 3
    print("Test 3:")
    data = {"Pressure": [3, 7, 4]}
    k = 1
    output = moving_window_stats(data, k)
    expected = {"Pressure": [(3, 3, 3.0), (7, 7, 7.0), (4, 4, 4.0)]}
    print(f"Data: {data}, k={k}")
    print(f"Output:   {output}")
    print(f"Expected: {expected}\n")


if __name__ == '__main__':
    # Test your homework implementation
    run_problem1_tests()
    print("\n" + "="*50 + "\n")
    run_problem2_tests()
    print("\n" + "="*50 + "\n")
    run_problem3_tests()
