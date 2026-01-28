#!/usr/bin/env python3
"""
Script to extract JSON files from data/all_json.zip to data/json directory
"""

import zipfile
import os

def extract_json_files():
    # Define paths
    zip_path = 'data/all_json.zip'
    extract_to = 'data/json'
    
    # Check if zip file exists
    if not os.path.exists(zip_path):
        print(f"Error: {zip_path} not found")
        return
    
    # Create extraction directory if it doesn't exist
    os.makedirs(extract_to, exist_ok=True)
    
    # Extract the zip file
    print(f"Extracting {zip_path} to {extract_to}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print(f"Successfully extracted all files to {extract_to}")
    
    # List extracted files
    extracted_files = []
    for root, dirs, files in os.walk(extract_to):
        for file in files:
            extracted_files.append(os.path.join(root, file))
    
    print(f"\nTotal files extracted: {len(extracted_files)}")
    if extracted_files:
        print("\nFirst few files:")
        for file in extracted_files[:5]:
            print(f"  - {file}")
        if len(extracted_files) > 5:
            print(f"  ... and {len(extracted_files) - 5} more")

if __name__ == "__main__":
    extract_json_files()
