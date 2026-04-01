import os

log_folder = "C:/audit_logs"

suspicious_keywords = ["DELETE", "DROP", "UPDATE"]

print("== SIEM LOG ANALYSIS START ===\n")

for file in os.listdir(log_folder):
    if not file.endswith(".log"):
        continue
    filepath = os.path.join(log_folder, file)

    print(f"\n--- Checking: {file} ---")

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for keyword in suspicious_keywords:
                if keyword in line:
                    print(f"[ALERT] {line.strip()}")

print("\n=== ANALYSIS COMPLETE ===")