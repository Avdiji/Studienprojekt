# patterns = [{"label": "CT", "pattern": "dienstags von 20.00 Uhr bis 21.30 Uhr"}]
# patterns = []

reg_eibach_time = "\d"

patterns = [{"label": "time", "pattern": [{'TEXT': {'REGEX': f"{reg_eibach_time}"}}]}]
weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
for day in weekdays:
    patterns.append({"label": "DAY", "pattern": day})
