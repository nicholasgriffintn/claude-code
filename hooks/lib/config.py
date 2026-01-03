#!/usr/bin/env python3
"""Configuration loader for hooks (no external dependencies)."""
from typing import Dict, Any, List, Tuple


def get_protected_patterns() -> Tuple[List[str], List[str]]:
    """Get protected file patterns."""
    blocked = [
        'package-lock.json',
        'yarn.lock',
        'pnpm-lock.yaml',
        'Gemfile.lock',
        'poetry.lock',
        'Cargo.lock',
        '.env',
        '.env.local',
        '.env.production',
        '**/secrets/*',
        '**/credentials/*',
        '.git/*',
    ]

    warned = [
        '.github/workflows/*',
        'docker-compose.yml',
        'Dockerfile',
        '**/production/*',
    ]

    return blocked, warned


def get_secret_patterns() -> Tuple[List[Tuple[str, str]], set]:
    """Get secret detection patterns."""
    patterns = [
        (r'(?i)(api[_-]?key|apikey)\s*[:=]\s*["\']?[a-zA-Z0-9_-]{10,}', 'API key'),
        (r'(?i)(secret|password|passwd|pwd)\s*[:=]\s*["\'][^"\']+["\']', 'Password/Secret (quoted)'),
        (r'(?i)(secret|password|passwd|pwd)\s*[:=]\s*[^"\'\s]{8,}', 'Password/Secret (unquoted)'),
        (r'(?i)bearer\s+[a-zA-Z0-9_-]{20,}', 'Bearer token'),
        (r'ghp_[a-zA-Z0-9]{36}', 'GitHub Personal Access Token'),
        (r'github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}', 'GitHub PAT (fine-grained)'),
        (r'gho_[a-zA-Z0-9]{36}', 'GitHub OAuth Access Token'),
        (r'ghs_[a-zA-Z0-9]{36}', 'GitHub Server-to-Server Token'),
        (r'sk-[a-zA-Z0-9]{48}', 'OpenAI API Key'),
        (r'sk-ant-[a-zA-Z0-9-]{90,}', 'Anthropic API Key'),
        (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'Private key'),
        (r'-----BEGIN CERTIFICATE-----', 'Certificate'),
        (r'(?i)aws[_-]?access[_-]?key[_-]?id\s*[:=]\s*[A-Z0-9]{20}', 'AWS Access Key'),
        (r'(?i)aws[_-]?secret[_-]?access[_-]?key\s*[:=]\s*[a-zA-Z0-9/+=]{40}', 'AWS Secret Key'),
        (r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24,}', 'Slack Token'),
        (r'AIza[0-9A-Za-z_-]{35}', 'Google API Key'),
        (r'ya29\.[0-9A-Za-z_-]+', 'Google OAuth Access Token'),
        (r'[0-9]+-[0-9A-Za-z_-]{32}\.apps\.googleusercontent\.com', 'Google OAuth2 ID'),
        (r'AIza[0-9A-Za-z\\-_]{35}', 'Firebase API Key'),
        (r'eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*', 'JWT Token'),
        (r'(?i)(postgres|mysql|mongodb)://[^:]+:[^@]+@', 'Database URL with credentials'),
        (r'(?i)jdbc:[^:]+://[^:]+:[^@]+@', 'JDBC URL with credentials'),
        (r'(?i)redis://:[^@]+@', 'Redis URL with password'),
    ]

    skip_files = {
        '.env.example',
        '.env.template',
        '.env.sample',
        'package-lock.json',
        'yarn.lock',
        'pnpm-lock.yaml',
    }

    return patterns, skip_files


def get_formatters() -> Dict[str, Dict[str, Any]]:
    """Get formatter configuration."""
    return {
        '.js': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.jsx': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.ts': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.tsx': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.json': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.css': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.scss': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.md': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.yaml': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.yml': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        '.py': {'command': ['black', '--quiet'], 'timeout': 10},
        '.go': {'command': ['gofmt', '-w'], 'timeout': 10},
        '.rs': {'command': ['rustfmt'], 'timeout': 10},
    }


def get_agent_hints() -> Tuple[Dict[str, str], List[Tuple[str, str]]]:
    """Get agent hints and dangerous patterns."""
    hints = {
        r'\b(review|check|look at)\b.*\b(code|changes|pr|pull request)\b':
            'Tip: Consider using the reviewer agent for thorough code reviews.',
        r'\b(bug|error|crash|fail|broken)\b':
            'Tip: The debugger agent specializes in systematic root cause analysis.',
        r'\b(test|coverage|spec)\b':
            'Tip: The tester agent can help design comprehensive test strategies.',
        r'\b(security|auth|vulnerab|owasp)\b':
            'Tip: The security-auditor agent can perform OWASP Top 10 checks.',
        r'\b(refactor|clean|improve|simplify)\b.*\b(code)\b':
            'Tip: The refactorer agent specializes in code structure improvements.',
        r'\b(document|readme|api docs)\b':
            'Tip: The documentor agent creates clear technical documentation.',
    }

    dangerous = [
        (r'\brm\s+-rf\s+[/~]', '⚠️ Warning: Recursive delete from root/home detected'),
        (r'\bgit\s+push\s+.*--force', '⚠️ Warning: Force push detected - this rewrites history'),
        (r'\bgit\s+reset\s+--hard', '⚠️ Warning: Hard reset will lose uncommitted changes'),
        (r'\bdrop\s+database\b', '⚠️ Warning: DROP DATABASE command detected'),
        (r'\btruncate\s+table\b', '⚠️ Warning: TRUNCATE TABLE will delete all data'),
    ]

    return hints, dangerous
