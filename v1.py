#Extract single log
import re

# Input log file (log1)
input_file = "log1.txt"

# Output file to store deployment status only
output_file = "status_output.txt"

# Keywords to extract the summary section
start_marker = "Deployment Summary"
end_marker = "==================================================="

capturing = False
summary_lines = []

with open(input_file, "r") as f:
    for line in f:
        # Detect start of summary block
        if start_marker in line:
            capturing = True
            continue
        
        # Stop when reaching the end marker
        if capturing and end_marker in line:
            capturing = False
            break
        
        # Capture lines between the two markers
        if capturing:
            summary_lines.append(line.strip())

# Write extracted summary lines to output file
with open(output_file, "w") as f:
    f.write("===== Application Deployment Status (From Log 1) =====\n")
    for line in summary_lines:
        if line:  # skip empty lines
            f.write(line + "\n")

print("Status extracted successfully!")
print(f"Output file created: {output_file}")
