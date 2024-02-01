#!/usr/bin/env python3
# renameYMDdates.py - Renames filenames with European DD-MM-YYYY date format
# to Chinese YYYY-MM-DD.

import shutil, os, re

# Create a regex that matches files with the DD-MM-YYYY date format.
date_pattern = re.compile(r"""^(.*?)    # all text before the date
                          (\d{2})-      # two digits for the day
                          (\d{2})-      # two digits for the month
                          (\d{4})       # four digits for the year
                          (.*?)$        # all text after the date
                          """, re.VERBOSE)

# Loop over the files in the working directory.
for orig_filename in os.listdir('.'):
    mo = date_pattern.search(orig_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    day_part = mo.group(2)
    month_part = mo.group(3)
    year_part = mo.group(4)
    after_part = mo.group(5)
    
    # Form the European-style filename.
    zh_filename = before_part + year_part + '-' + month_part + '-' + day_part + after_part

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    orig_filename = os.path.join(abs_working_dir, orig_filename)
    zh_filename = os.path.join(abs_working_dir, zh_filename)

    # Rename the files.
    print(f'Renaming "{orig_filename}" to "{zh_filename}"...')
    shutil.move(orig_filename, zh_filename)   # uncomment after testing