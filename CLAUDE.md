# Claude Code Workflow Plugin - Context for Claude

## Repository Purpose

This repository contains the `ng-workflow` Claude Code plugin, a comprehensive workflow automation system designed to enhance development workflows through specialized agents, skills, and hooks.

**Owner**: nicholasgriffintn
**License**: Apache-2.0
**Version**: 1.0.0

## Quick Reference

### What This Plugin Provides

1. **7 Specialized Agents** - Task-specific AI agents for different development activities
2. **8 Skills** - Reusable knowledge modules that agents can leverage
3. **3 Custom Commands** - Slash commands for feature development, PR review, and git workflow
4. **Multiple Hooks** - Automated validation and workflow enforcement

### Repository Structure

```
/agents/          - Agent definitions (orchestrator, reviewer, debugger, tester, documentor, refactorer, security)
/skills/          - Skill modules (project-analysis, architecture-patterns, git-workflow, testing-strategy, performance-optimisation, security-review, frontend-design, backend-design)
/commands/        - Slash command definitions (feature-dev, commit-push-pr, review-pr)
/hooks/           - Hook scripts and configuration
/.claude-plugin/  - Plugin metadata and marketplace info
```

## Agent Overview

### When to Use Each Agent

| Agent | Purpose | When to Invoke |
|-------|---------|---------------|
| **orchestrator** | Coordinates multiple agents for complex tasks | Multi-step features, full-stack implementations |
| **reviewer** | Code quality, security, performance reviews | Pre-commit, PR reviews, security audits |
| **debugger** | Bug identification and resolution | Production issues, failing tests, errors |
| **tester** | Test strategy and implementation | After feature development, coverage improvement |
| **documentor** | Documentation creation | After code completion, API changes |
| **refactorer** | Code structure improvement | Code smells, technical debt, refactoring |
| **security** | Security reviews and threat modeling | Auth/permissions changes, secrets/PII, public endpoints |

### Agent Details

#### Orchestrator
- **Model**: Opus (most powerful)
- **Tools**: Read, Write, Edit, Glob, Grep, Bash, Task, TodoWrite
- **Skills**: project-analysis, architecture-patterns, security-review
- **Use for**: High-level coordination of complex development tasks

#### Reviewer
- **Model**: Sonnet
- **Tools**: Read, Grep, Glob, Bash (read-only)
- **Skills**: git-workflow, testing-strategy
- **Checklist**: Testing, Maintainability, Performance, Security, Correctness

#### Debugger
- **Model**: Sonnet
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Skills**: performance-optimisation
- **Permission**: acceptEdits
- **Process**: Reproduce → Isolate → Diagnose → Test → Fix → Verify

#### Tester
- **Model**: Sonnet
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Skills**: testing-strategy
- **Permission**: acceptEdits
- **Focus**: Testing pyramid (70% unit, 20% integration, 10% E2E)

#### Documentor
- **Model**: Sonnet
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Permission**: acceptEdits
- **Output**: READMEs, API docs, technical specs, user guides

#### Refactorer
- **Model**: Sonnet
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Skills**: architecture-patterns
- **Permission**: acceptEdits
- **Focus**: Code smells, maintainability, design patterns

#### Security
- **Model**: Sonnet
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Skills**: security-review, testing-strategy
- **Permission**: acceptEdits
- **Focus**: Threat modeling, input validation, authN/authZ, secrets and PII handling

## Skills Reference

**IMPORTANT**: Skills are NOT slash commands. They are knowledge modules that agents reference automatically or that you can request in natural language (e.g., "Please use the project-analysis skill").

### project-analysis
**Purpose**: Analyze codebase structure, dependencies, and architecture
**Best for**: New projects, onboarding, planning refactors
**Outputs**: Project overview, tech stack, structure map, dependencies
**How to use**: "Please use the project-analysis skill to analyze this codebase"

### architecture-patterns
**Purpose**: Recognize and apply software architecture patterns
**Patterns**: MVC, Layered, Event-Driven, Microservices
**Outputs**: Architecture decision records, trade-off analysis, diagrams
**How to use**: "Apply the architecture-patterns skill to help design this feature"

### git-workflow
**Purpose**: Git best practices and conventions
**Includes**: Conventional commits, branching strategy, PR workflow
**Format**: `<type>(<scope>): <description>` (feat, fix, docs, etc.)
**How to use**: "Use the git-workflow skill to help me create a proper commit"

### testing-strategy
**Purpose**: Comprehensive testing approach
**Coverage**: Unit (80%), Integration (70%), E2E (60%)
**Frameworks**: Vitest/Playwright (JS/TS), Pytest (Python)
**How to use**: "Apply the testing-strategy skill to help design tests"

### performance-optimisation
**Purpose**: Performance analysis and optimization
**Areas**: Frontend, backend, database, algorithms
**How to use**: "Use the performance-optimisation skill to analyze bottlenecks"

### security-review
**Purpose**: Security reviews, threat modeling, and remediation guidance
**Focus**: AuthN/AuthZ, input validation, secrets/PII, dependency risk
**How to use**: "Use the security-review skill to assess security risks"

### frontend-design
**Purpose**: Create distinctive, production-grade frontend interfaces with strong aesthetic direction
**Focus**: Typography, layout, motion, and visual systems
**How to use**: "Use the frontend-design skill to design this interface"

### backend-design
**Purpose**: Design robust backend systems, APIs, and data models
**Focus**: Contracts, data modeling, reliability, performance, and security
**How to use**: "Use the backend-design skill to plan this service"

## Commands Reference

### feature-dev
**Command**: `/ng-workflow:feature-dev`  
**Purpose**: Guided feature development with discovery, architecture design, and review phases.

### commit-push-pr
**Command**: `/ng-workflow:commit-push-pr`  
**Purpose**: Commit staged changes, push the branch, and open a PR via `gh`.

### review-pr
**Command**: `/ng-workflow:review-pr`  
**Purpose**: Comprehensive PR review using specialized agents (optionally scoped by review aspects).

## Hooks System

### Pre-Tool Use Hooks

**Edit/Write Operations**:
- `protect-files.py` - Prevents modification of protected files
- `security-check.py` - Scans for security vulnerabilities

**Bash Operations**:
- `log-commands.sh` - Logs all commands for audit trail

### Post-Tool Use Hooks

**Edit/Write Operations**:
- `format-on-edit.py` - Auto-formats code after editing

### Event Hooks

- `validate-environment.py` - Session start validation
- `validate-prompt.py` - User prompt validation
- `notify-input.sh` - User input notifications
- `notify-complete.sh` - Task completion notifications

## Development Workflow

### Recommended Task Flow

1. **Analysis Phase**
   - Use `project-analysis` skill for unfamiliar codebases
   - Review architecture with `architecture-patterns` skill

2. **Implementation Phase**
   - Use `orchestrator` for complex, multi-step tasks
   - Develop with `testing-strategy` in mind
   - Create tests using `tester` agent

3. **Quality Assurance Phase**
   - Run `reviewer` agent before commits
   - Use `debugger` for any issues
   - Apply `refactorer` for code improvements

4. **Documentation Phase**
   - Use `documentor` for comprehensive docs
   - Follow `git-workflow` conventions for commits

### Git Conventions

**Branch Naming**:
- `feature/<name>` - New features
- `bugfix/<name>` - Bug fixes
- `hotfix/<name>` - Critical production fixes
- `release/<version>` - Release branches

**Commit Format**:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types**: feat, fix, docs, style, refactor, test, chore

## Important Conventions

### Code Review Standards

All code must pass these checks before commit:
- [ ] Tests written and passing
- [ ] Code is self-documenting
- [ ] No security vulnerabilities
- [ ] Performance considerations addressed
- [ ] Documentation updated

### Testing Requirements

- **Unit Tests**: 80%+ coverage
- **Integration Tests**: 70%+ coverage
- **E2E Tests**: 60%+ coverage
- All edge cases covered
- Error handling tested

### Refactoring Guidelines

Address these code smells:
- Long methods (>20 lines)
- Large classes (>300 lines)
- Long parameter lists (>4 params)
- Duplicated code
- Magic numbers/strings

## File Locations

### Agent Definitions
- [agents/orchestrator.md](agents/orchestrator.md)
- [agents/reviewer.md](agents/reviewer.md)
- [agents/debugger.md](agents/debugger.md)
- [agents/tester.md](agents/tester.md)
- [agents/documentor.md](agents/documentor.md)
- [agents/refactor.md](agents/refactor.md)

### Skill Definitions
- [skills/project-analysis/SKILL.md](skills/project-analysis/SKILL.md)
- [skills/architecture-patterns/SKILL.md](skills/architecture-patterns/SKILL.md)
- [skills/git-workflow/SKILL.md](skills/git-workflow/SKILL.md)
- [skills/testing-strategy/SKILL.md](skills/testing-strategy/SKILL.md)
- [skills/performance-optimisation/SKILL.md](skills/performance-optimisation/SKILL.md)
- [skills/security-review/SKILL.md](skills/security-review/SKILL.md)
- [skills/frontend-design/SKILL.md](skills/frontend-design/SKILL.md)
- [skills/backend-design/SKILL.md](skills/backend-design/SKILL.md)

### Hook Configuration
- [hooks/hooks.json](hooks/hooks.json) - Main hook configuration
- [hooks/scripts/](hooks/scripts/) - Hook implementation scripts

### Plugin Configuration
- [.claude-plugin/plugin.json](.claude-plugin/plugin.json) - Plugin metadata

## Context for Future Sessions

### When Working on This Repository

1. **Understand the Purpose**: This is a plugin FOR Claude Code, not a standalone application
2. **Agent Files Are Prompts**: The .md files in `/agents/` are agent prompts, not documentation
3. **Skills Are Templates**: The SKILL.md files provide reusable workflows and checklists
4. **Hooks Are Automation**: The scripts in `/hooks/scripts/` run automatically during workflows
5. **Follow Conventions**: Use conventional commits, test before committing, document changes

### Key Principles

- **Quality First**: Use reviewer agent before commits
- **Test Coverage**: Maintain high test coverage standards
- **Documentation**: Keep docs up-to-date with code changes
- **Security**: All code changes are scanned for security issues
- **Automation**: Hooks enforce quality standards automatically

### Common Tasks

**Adding a New Agent**:
1. Create `/agents/<name>.md` with frontmatter and prompt
2. Define tools, model, skills, and permissionMode
3. Document use cases and process
4. Update README.md

**Adding a New Skill**:
1. Create `/skills/<name>/SKILL.md` with frontmatter
2. Include checklists, commands, and templates
3. Document when to use the skill
4. Update README.md

**Modifying Hooks**:
1. Edit hook scripts in `/hooks/scripts/`
2. Update `/hooks/hooks.json` if adding new hooks
3. Test thoroughly to avoid workflow disruption
4. Document changes

## Version Information

**Current Version**: 1.0.0
**Last Updated**: 2026-01-03
**Maintained By**: nicholasgriffintn

## References

- Main Documentation: [README.md](README.md)
- License: [LICENSE](LICENSE) (Apache-2.0)
- Repository: https://github.com/nicholasgriffintn/claude-code
