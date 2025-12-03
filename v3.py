import re
import glob
from pathlib import Path
import csv

def extract_deployment_summary(log_file: Path) -> list:
    """
    Extracts the Deployment Summary section from a given log file.

    Args:
        log_file (Path): Path to the log file.

    Returns:
        list: Lines of deployment summary for applications only.
    """
    start_marker = "Deployment Summary"
    end_marker = "==================================================="

    capturing = False
    summary_lines = []

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if start_marker in line:
                capturing = True
                continue
            if capturing and end_marker in line:
                break
            if capturing:
                line = line.strip()
                # Skip OS setup line, capture only app lines
                if line and not line.lower().startswith("os setup"):
                    summary_lines.append(line)
    return summary_lines

def main():
    # Use glob to automatically fetch all log files in current directory
    log_files = sorted(glob.glob("log*.txt"))

    if not log_files:
        print("No log files found matching 'log*.txt'")
        return

    output_csv = "v3_status_output.csv"

    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Log File", "Application", "Status"])  # CSV header
        
        # Process each log file
        for log_file in log_files:
            summary = extract_deployment_summary(Path(log_file))
            writer.writerow([f"--- From {log_file} ---", "", ""])  # Optional section header in CSV
            if summary:
                for line in summary:
                    # Split into application and status if possible
                    if ":" in line:
                        app, status = line.split(":", 1)
                        writer.writerow([log_file, app.strip(), status.strip()])
                    else:
                        writer.writerow([log_file, line, "UNKNOWN"])
            else:
                writer.writerow([log_file, "No application info found", "N/A"])

    print(f"Deployment status extracted from {len(log_files)} log(s).")
    print(f"CSV file created: {output_csv}")

if __name__ == "__main__":
    main()
