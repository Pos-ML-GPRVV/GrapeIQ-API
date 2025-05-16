import os
import sys

def validate_env_variables():
    required_vars = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("Error: The following required environment variables were not found:")
        for var in missing_vars:
            print(f"- {var}")
        print("\nPlease set up the environment variables before running the project.")
        sys.exit(1)