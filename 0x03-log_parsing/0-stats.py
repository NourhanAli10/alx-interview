#!/usr/bin/python3
import sys
import signal


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interrupt signal (Ctrl+C)."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 9 or parts[5] != '"GET' or
        parts[6] != '/projects/260' or parts[7] != 'HTTP/1.1"':
            continue

        try:
            status_code = int(parts[8])
            file_size = int(parts[9])
        except (ValueError, IndexError):
            continue
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
