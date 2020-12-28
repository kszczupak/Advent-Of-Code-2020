import time

def test_multiple_cases(tested_function, cases):
    passed_cnt = 0
    failed_cnt = 0
    test_suite_start_time = time.monotonic()
    
    for case_idx, (expected, *test_input) in enumerate(cases):
        case_start_time = time.monotonic()
        # supress errors here? may make debugging harder
        actual = tested_function(*test_input)
        case_elapsed_time_ms = (time.monotonic() - case_start_time) * 1000
        
        if expected == actual:
            passed_cnt += 1
            result = "PASSED"
        else:
            failed_cnt += 1
            result = f"FAILED, expected {expected}, got {actual}"
        
        print(f"Case #{case_idx}: {result} ({case_elapsed_time_ms:.2f} [ms])")
        
    print('=' * 40)
    if not failed_cnt:
        print("All tests passed", end='')
    else:
        print(f"Passed: {passed_cnt}; Failed: {failed_cnt}", end='')
    
    elapsed_time_ms = (time.monotonic() - test_suite_start_time) * 1000
    print(f"; Elapsed time: {elapsed_time_ms:.2f} [ms]")

    
def test_single_case(tested_function, expected, *test_inputs):
    test_start_time = time.monotonic()
    # supress errors here? may make debugging harder
    actual = tested_function(*test_inputs)
    test_elapsed_time_ms = (time.monotonic() - test_start_time) * 1000

    if expected == actual:
        result = "PASSED"
    else:
        result = f"FAILED, expected {expected}, got {actual}"

    print(f"{result} (in {test_elapsed_time_ms:.2f} [ms])")