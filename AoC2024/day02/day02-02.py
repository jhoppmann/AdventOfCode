

def run():
    with open('input.txt') as file:
        reports = file.read().splitlines()

    max_skip = 3
    safe_reports = 0
    for report in reports:
        if is_safe(report, max_skip):
            safe_reports += 1

    print("Part 2:", safe_reports
          )

def is_safe(report: str, max_skip: int) -> bool:
    report_numbers_list = [int(x) for x in report.split(' ')]
    safe_variants = 0
    for i in range (0, len(report_numbers_list)):
        # check variants if a number is missing
        report_numbers = report_numbers_list[0:i:1] + report_numbers_list[i+1::]
        if not is_ordered(report_numbers):
            continue
        differences = [abs(report_numbers[i] - report_numbers[i+1]) for i in range(0, len(report_numbers) - 1)]
        if all(x <= max_skip for x in differences):
            safe_variants += 1

    return safe_variants >= 1



def is_ordered(list_to_check: list) -> bool:
    return (all(list_to_check[i] < list_to_check[i + 1] for i in range(len(list_to_check) - 1)) or
            all(list_to_check[i] > list_to_check[i + 1] for i in range(len(list_to_check) - 1)))


if __name__ == '__main__':
    run()