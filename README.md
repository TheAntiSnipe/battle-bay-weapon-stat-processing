# battle-bay-weapon-stat-processing
A script that processes the game data files for Battle Bay and returns output as required.

## Contents:

# 1. Python scripts
- level_rush_chart_generator.py: 
  Contains the code used to generate **levelup-chart.csv** and **level-rush-chart.csv**. Operates upon **costs-per-level.csv**.
- projectile_time_extraction_script.py
  Contains the code used to generate **flighttime-data.csv**. Operates upon **skills-r-1159.csv**.

# 2. Comma Separated Value (CSV) files
# - Input files
    - costs-per-level.csv: Required input for level_rush_chart_generator.py, contains raw, unprocessed data for **costs per item level**.
    - skills-r-1159.csv: Required input for projectile_time_extraction_script.py, contains raw, unprocessed **data from the game files for all weapons in the game**.
 
# - Output files
    - levelup-chart.csv: Contains a processed readable chart of resources needed **per level up**.
    - level-rush-chart.csv: Contains a processed readable chart of resources needed **per level tier of 10 levels each**.
    - flighttime-data.csv: Contains a processed readable chart of **weapons and their flight times**, sorted in ascending order of flight time.

