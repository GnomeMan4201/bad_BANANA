#!/usr/bin/env python3
import os
import re

# Define paths and constants
ROOT_DIR = os.path.expanduser("~/exfil")
TARGET_EXT = ('.py',)
REQUIRED_IMPORTS = [
    "import os",
    "from datetime import datetime",
    "import argparse"
]

ARG_FLAGS = {
    "--lab":    'parser.add_argument("--lab", action="store_true", help="Enable lab mode")',
    "--field":  'parser.add_argument("--field", action="store_true", help="Field mode (exfil+persistence)")',
    "--kill":   'parser.add_argument("--kill", action="store_true", help="Trigger kill switch")',
    "--consent":'parser.add_argument("--consent", action="store_true", help="Confirm operator consent")'
}

def normalize_indentation(content):
    """Strip trailing whitespace from lines."""
    lines = content.splitlines()
    return '\n'.join([line.rstrip() for line in lines]) + '\n'

def ensure_imports(content):
    """Ensure essential imports exist at the top of the file."""
    modified = False
    for imp in REQUIRED_IMPORTS:
        if imp not in content:
            content = imp + "\n" + content
            modified = True
    return content, modified

def remove_conflicting_args(content):
    """Remove duplicate argparse declarations (e.g. multiple --field)."""
    pattern = re.compile(r'^\s*parser\.add_argument
