#!/usr/bin/env python3
"""
Pre-commit security check hook.
Blocks commits that might contain secrets or security issues.

Original Source: https://github.com/CloudAI-X/claude-workflow
"""
import sys
import re
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'lib'))

from base_hook import BaseHook
from config import get_secret_patterns
from pattern_matcher import is_test_file


class SecurityCheckHook(BaseHook):
    """Hook to check for secrets and security issues."""

    def __init__(self):
        super().__init__('security-check')
        self.secret_patterns, self.skip_files = get_secret_patterns()

    def execute(self) -> int:
        file_path = self.get_file_path()
        content = self.get_content()

        if not file_path or not content:
            return 0

        issues = self.check_for_secrets(content, file_path)

        if issues:
            print(f"🚫 BLOCKED - Security issue detected in {file_path}:")
            for issue in issues:
                print(f"  - {issue}")
            print("\nThis edit has been BLOCKED to prevent committing secrets.")
            print("If this is a false positive, review and adjust patterns in config/secret-patterns.yaml")
            return 2

        return 0

    def check_for_secrets(self, content: str, file_path: str):
        """Check content for potential secrets."""
        issues = []

        if os.path.basename(file_path) in self.skip_files:
            return issues

        if is_test_file(file_path):
            return issues

        for pattern, secret_type in self.secret_patterns:
            matches = re.findall(pattern, content)
            if matches:
                issues.append(f"Potential {secret_type} detected")

        return issues


if __name__ == "__main__":
    SecurityCheckHook().run()
