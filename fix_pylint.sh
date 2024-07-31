#!/bin/bash

# Find all Python files in the current directory and all subdirectories, excluding venv
find . -name "*.py" -not -path "./venv/*" -not -path "*/venv/*" | while read file; do
  echo "Processing $file"
  
  # Run pylint and capture the output
  pylint_output=$(pylint "$file")
  
  # Check if pylint found any errors
  if [ $? -ne 0 ]; then
    echo "Fixing $file"
    # Use autopep8 to fix the file
    autopep8 --in-place --aggressive --aggressive "$file"
  else
    echo "No issues found in $file"
  fi
done