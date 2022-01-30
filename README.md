PRE-QUISITE:
1. prepare the .json files into ./source/json directory
2. Set up connection to PostgreSQL DB on ./tools/pipeline/ref/<staging/ods/dwh>/config.py

TO RUN:
Converting JSON to CSV:
1. from terminal/command prompt, change directory to the workspace dana-test
2. go to ./tools/conversions
3. execute -> python main.py
4. check ./source/csv/ if the files are available

CSV to STAGING:
1. from terminal/command prompt, change directory to the workspace dana-test
2. go to ./tools/pipeline/staging
3. execute -> python main.py --object <<staging table>>