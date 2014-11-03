# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "eads-portfolio"

# Descriptive title of project
TITLE = "Mago Torres"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Google spreadsheet key
SPREADSHEET_KEY = "1xeUJcdOBIcDPqeuunyHlzdOVjJcJp4RVMGrGx5ni-0o"

# Spreadsheet cache lifetime in seconds. (Default: 4)
SPREADSHEET_CACHE_TTL = 60

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "www.inforight.net",
    "staging": "staging.inforight.net",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'eads-portfolio',
    'title': 'Mago Torres'
}
