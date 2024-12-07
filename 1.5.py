total_tasks = 20

for tasks_ok in [20, 11, 10, 9, 0]:
    test_passed = False

    if tasks_ok >= total_tasks / 2:
        test_passed = True

    if test_passed:
        print(f'{tasks_ok} tasks: Congratulations! You passed the test.')
    else:
        print(f'{tasks_ok} tasks: Unfortunately, you failed the test.')
