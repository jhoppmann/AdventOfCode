

def run():
    with open('input.txt') as file:
        reports = file.read().splitlines()

    max_skip = 3
    safe_reports = 0
    for report in reports:
        if is_safe(report, max_skip):
            safe_reports += 1

    print("Part 1:", safe_reports
          )

def is_safe(report: str, max_skip: int) -> bool:
    report_numbers = [int(x) for x in report.split(' ')]
    if not is_ordered(report_numbers):
        return False
    differences = [abs(report_numbers[i] - report_numbers[i+1]) for i in range(0, len(report_numbers) - 1)]
    return all(x <= max_skip for x in differences)


def is_ordered(list_to_check: list) -> bool:
    return all(list_to_check[i] < list_to_check[i + 1] for i in range(len(list_to_check) - 1)) or all(list_to_check[i] > list_to_check[i + 1] for i in range(len(list_to_check) - 1))


if __name__ == '__main__':
    run()