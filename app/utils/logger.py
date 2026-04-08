class Logger:
    def __init__(self):
        self.file_path = "logs/cheating_log.csv"
        self.last_event = None

        import os, csv
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Time", "Event", "Score"])

    def log(self, event, score):
        if event == self.last_event:
            return  # skip duplicate

        from datetime import datetime
        import csv

        time_now = datetime.now().strftime("%H:%M:%S")

        with open(self.file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([time_now, event, score])

        self.last_event = event