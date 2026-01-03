#!/usr/bin/env python3
"""Pattern matching utilities for hooks."""
import os
import fnmatch
from typing import List, Optional


def normalize_file_path(file_path: str) -> str:
    """Normalize file path to prevent traversal attacks."""
    file_path = os.path.normpath(file_path)
    file_path = file_path.lstrip('./')
    file_path = file_path.lstrip('/')
    return file_path


def matches_pattern(file_path: str, patterns: List[str]) -> Optional[str]:
    """Check if file path matches any pattern."""
    file_path = normalize_file_path(file_path)

    for pattern in patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return pattern
        if fnmatch.fnmatch(os.path.basename(file_path), pattern):
            return pattern

    return None


def is_test_file(file_path: str) -> bool:
    """Check if file is a test file."""
    file_path_lower = file_path.lower()
    return 'test' in file_path_lower or 'spec' in file_path_lower
