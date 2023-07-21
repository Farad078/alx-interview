#!/usr/bin/python3

import sys
import signal

stat_code = {"200", "301", "400", "401", "403", "404", "405", "500"}
file_sizes = []
status_code_counts = {code: 0 for code in stat_code}


def print_statistics():
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys(), key=int):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")
    print()


def signal_handler(sig, frame):
    print("\nKeyboard interruption detected. Printing statistics:")
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line_number, line in enumerate(sys.stdin, 1):
        line = line.strip()
        parts = line.split()
        if len(parts) == 10 and parts[8].isdigit() and parts[7] in stat_code:
            file_size = int(parts[8])
            status_code = parts[7]
            file_sizes.append(file_size)
            status_code_counts[status_code] += 1

        if line_number % 10 == 0:
            print(f"Statistics after {line_number} lines:")
            print_statistics()

except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing statistics:")
    print_statistics()
