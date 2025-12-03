import re
import glob

# List of log files (you can also use glob to match multiple files)
log_files = [r"C:\Users\Suriya\Mohan Demo Project\log1.txt", 
             r"C:\Users\Suriya\Mohan Demo Project\log2.txt", 
             r"C:\Users\Suriya\Mohan Demo Project\log3.txt"]

# Output file to store deployment status from all logs
output_file = "v2_status_output.txt"

# Keywords to locate summary section
start_marker = "Deployment Summary"
end_marker = "==================================================="

with open(output_file, "w") as out_f:
    out_f.write("===== Application Deployment Status (All Logs) =====\n\n")
    
    # Process each log file
    for log_file in log_files:
        capturing = False
        summary_lines = []
        
        with open(log_file, "r") as f:
            for line in f:
                if start_marker in line:
                    capturing = True
                    continue
                if capturing and end_marker in line:
                    capturing = False
                    break
                if capturing:
                    summary_lines.append(line.strip())
        
        # Write summary for this log
        out_f.write(f"--- From {log_file} ---\n")
        for line in summary_lines:
            if line:  # skip empty lines
                out_f.write(line + "\n")
        out_f.write("\n")

print("Deployment status extracted from all logs successfully!")
print(f"Summary file created: {output_file}")
