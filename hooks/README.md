# Hooks System

This directory contains the hooks system for the Claude Code workflow plugin.

## Structure

```
hooks/
├── lib/                  # Shared Python libraries
│   ├── __init__.py
│   ├── base_hook.py     # Base class for all hooks
│   ├── config.py        # ALL configuration (edit this!)
│   └── pattern_matcher.py # Pattern matching utilities
├── scripts/             # Hook implementations
│   ├── protect-files.py
│   ├── security-check.py
│   ├── format-on-edit.py
│   ├── log-commands.py
│   ├── validate-environment.py
│   ├── validate-prompt.py
│   ├── notify.sh
│   └── test-hooks.py    # Manual testing script
├── tests/               # Unit tests
│   ├── test_protect_files.py
│   └── test_security_check.py
└── hooks.json           # Hook configuration
```

## Configuration

All hook behavior is configured in **one file**: `hooks/lib/config.py`

Edit this file to customize everything:

### Protected Files

```python
def get_protected_patterns():
    blocked = [
        '.env',
        'package-lock.json',
        # Add your patterns here!
    ]
```

### Secret Patterns

```python
def get_secret_patterns():
    patterns = [
        (r'sk-[a-zA-Z0-9]{48}', 'OpenAI API Key'),
        # Add your patterns here!
    ]
```

### Formatters

```python
def get_formatters():
    return {
        '.js': {'command': ['npx', 'prettier', '--write'], 'timeout': 10},
        # Add your formatters here!
    }
```

### Agent Hints

```python
def get_agent_hints():
    hints = {
        r'\b(bug|error)\b': 'Tip: Use the debugger agent',
        # Add your hints here!
    }
```

## Hooks

### PreToolUse Hooks

**protect-files.py** - Blocks edits to sensitive files

- Checks file paths against protected patterns
- Blocks lock files, .env files, secrets directories
- Configurable in `lib/config.py` → `get_protected_patterns()`

**security-check.py** - Scans for secrets and credentials

- Detects API keys, passwords, tokens, private keys
- Supports 23 secret types (AWS, GitHub, OpenAI, Slack, Google, etc.)
- Configurable in `lib/config.py` → `get_secret_patterns()`

**log-commands.py** - Logs all bash commands

- Creates audit trail in `.claude/command-history.log`
- Records commands and descriptions
- Helps track what Claude executes

### PostToolUse Hooks

**format-on-edit.py** - Auto-formats files after editing

- Detects file type and runs appropriate formatter
- Supports Prettier, Black, gofmt, rustfmt
- Only runs if formatter is installed
- Configurable in `lib/config.py` → `get_formatters()`

### Event Hooks

**validate-environment.py** - Validates environment on startup

- Checks for Node.js, Python, Git
- Warns about missing dependencies
- Improved .env file detection (only warns if .env.example exists)

**validate-prompt.py** - Provides helpful hints for prompts

- Suggests appropriate agents based on content
- Warns about dangerous commands
- Pre-compiled regex for performance
- Configurable in `lib/config.py` → `get_agent_hints()`

**notify.sh** - Cross-platform notifications

- Unified notification script
- Supports macOS, Linux, Windows
- Parameterized for different messages

## Development

### Creating a New Hook

1. Inherit from `BaseHook`:

```python
from base_hook import BaseHook

class MyHook(BaseHook):
    def __init__(self):
        super().__init__('my-hook')

    def execute(self) -> int:
        file_path = self.get_file_path()
        # Your logic here
        return 0  # 0=continue, 2=block

if __name__ == '__main__':
    MyHook().run()
```

2. Add to `hooks.json`:

```json
{
  "PreToolUse": [
    {
      "matcher": "Edit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/my-hook.py"
        }
      ]
    }
  ]
}
```

### Testing

Run all tests:

```bash
cd hooks/tests
python -m unittest discover
```

Run specific test:

```bash
python -m unittest test_protect_files.py
```

Manual testing:

```bash
python3 hooks/scripts/test-hooks.py
```

## Logging

All hooks log to `.claude/hooks.log`:

```
[2026-01-03 15:30:45] [protect-files] File .env blocked
[2026-01-03 15:31:12] [security-check] Detected API key in config.py
[2026-01-03 15:32:00] [format-on-edit] Formatted test.py
```

View logs:

```bash
tail -f .claude/hooks.log
```

## Exit Codes

- `0`: Continue (allow operation)
- `1`: Error (but don't block)
- `2`: Block (prevent operation)

## Recent Improvements

### Security Fixes

- ✅ Fixed path traversal vulnerability in protect-files.py
- ✅ Rewrote log-commands in Python (eliminated command injection)
- ✅ Added comprehensive error logging
- ✅ Expanded secret detection patterns (23 types)

### Architecture Improvements

- ✅ Created BaseHook class for shared functionality
- ✅ Centralized all configuration in one file (lib/config.py)
- ✅ Consolidated duplicate notification scripts (40% code reduction)
- ✅ Added shared utility libraries
- ✅ Pre-compiled regex patterns for performance
- ✅ **No external dependencies required**

### Code Reduction

- Before: 532 lines across 8 files
- After: ~340 lines across 7 files
- **36% code reduction** while adding more features

## Troubleshooting

**Hook not executing:**

- Check file has execute permissions (`chmod +x`)
- Verify Python path in shebang
- Check `.claude/hooks.log` for errors

**False positives in security-check:**

- Edit `lib/config.py` → `get_secret_patterns()`
- Add file to `skip_files` set
- Adjust regex patterns

**Formatter not running:**

- Check formatter is installed (`which prettier`, `which black`)
- Edit `lib/config.py` → `get_formatters()` to adjust config
- Check `.claude/hooks.log` for errors

**Customizing patterns:**

- All configuration is in `lib/config.py` - just edit Python lists/dicts
- No YAML files needed
- Changes take effect immediately

## Contributing

When adding new hooks:

1. Use BaseHook class
2. Add configuration to `lib/config.py` (easy to edit!)
3. Include unit tests
4. Update this README
5. Add logging for debugging

## Testing

See [TESTING_HOOKS.md](../TESTING_HOOKS.md) for detailed testing guide.

Quick test:

```bash
# Should block (exit code 2)
echo '{"tool_input": {"file_path": ".env"}}' | python3 hooks/scripts/protect-files.py

# Should allow (exit code 0)
echo '{"tool_input": {"file_path": "app.py"}}' | python3 hooks/scripts/protect-files.py
```
