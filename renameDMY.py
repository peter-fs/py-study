#!/usr/bin/env python3
# renameYMDdates.py - Renames filenames with Chinese YYYY-MM-DD date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the YYYY-MM-DD date format.
date_pattern = re.compile(r"""^(.*?) # all text before the date
                          (\d{4})-  # four digits for the year
                          (\d{2})-  # two digits for the month
                          (\d{2})   # two digits for the day
                          (.*?)$    # all text after the date
                          """, re.VERBOSE)

# Loop over the files in the working directory.
for orig_filename in os.listdir('.'):
    mo = date_pattern.search(orig_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    year_part = mo.group(2)
    month_part = mo.group(3)
    day_part = mo.group(4)
    after_part = mo.group(5)
    
    # Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    orig_filename = os.path.join(abs_working_dir, orig_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # Rename the files.
    print(f'Renaming "{orig_filename}" to "{euro_filename}"...')
    shutil.move(orig_filename, euro_filename)   # uncomment after testing