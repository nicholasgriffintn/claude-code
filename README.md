# Claude Code Workflow Plugin

A Claude Code plugin that enhances your development workflow with specialized agents, skills, and hooks for code quality, testing, documentation, and more.

## Installation

```bash
# Clone this repository
git clone https://github.com/nicholasgriffintn/claude-code.git

# Install from the local directory
/plugin marketplace add ./claude-code
/plugin install ng-workflow@claude-code

# Verify installation
> /plugin
# (Press tab to see installed plugins)
```

## Features

### Agents

The plugin includes seven specialized agents that can be invoked to handle specific development tasks:

#### 1. Orchestrator Agent

**Command**: Available as `ng-workflow:orchestrator`

A high-level agent that coordinates multiple specialized agents to manage complex coding tasks from start to finish.

**Use cases**:

- Complex multi-step features requiring coordination
- Large refactoring projects
- Full-stack implementations

#### 2. Reviewer Agent

**Command**: Available as `ng-workflow:reviewer`

Analyzes code for quality, security, performance, and maintainability issues.

**Use cases**:

- Pre-commit code reviews
- Pull request analysis
- Security audits

#### 3. Debugger Agent

**Command**: Available as `ng-workflow:debugger`

Identifies, diagnoses, and resolves bugs systematically.

**Use cases**:

- Troubleshooting production issues
- Analyzing stack traces
- Root cause analysis

#### 4. Tester Agent

**Command**: Available as `ng-workflow:tester`

Designs and implements comprehensive testing strategies.

**Use cases**:

- Creating test suites
- Improving test coverage
- Test strategy planning

#### 5. Documentor Agent

**Command**: Available as `ng-workflow:documentor`

Creates and maintains comprehensive documentation.

**Use cases**:

- API documentation
- README files
- Technical specifications
- User guides

#### 6. Refactorer Agent

**Command**: Available as `ng-workflow:refactorer`

Improves code structure and maintainability without changing behavior.

**Use cases**:

- Code smell elimination
- Technical debt reduction
- Architecture improvements

#### 7. Security Agent

**Command**: Available as `ng-workflow:security`

Performs security reviews, threat modeling, and remediation guidance.

**Use cases**:

- Authentication/authorization changes
- Handling secrets or PII
- Public endpoint or API exposure
- Dependency upgrades and supply-chain risk checks

### Skills

Skills provide specialized knowledge and workflows that agents can use:

#### 1. Project Analysis

**Skill**: `ng-workflow:project-analysis`

Analyzes codebases to understand structure, dependencies, and architecture.

**Use when**:

- Starting a new project
- Onboarding to existing codebases
- Planning major refactors

**How to invoke**: "Please use the project-analysis skill to analyze this codebase"

#### 2. Architecture Patterns

**Skill**: `ng-workflow:architecture-patterns`

Recognizes and applies software architecture patterns (MVC, Layered, Event-Driven, etc.).

**Includes**:

- Pattern selection framework
- Visual diagrams
- Trade-off analysis templates

**How to invoke**: "Apply the architecture-patterns skill to help design this feature"

#### 3. Git Workflow

**Skill**: `ng-workflow:git-workflow`

Best practices for Git collaboration including branching strategies and commit conventions.

**Features**:

- Conventional Commits format
- Branch naming conventions
- PR workflow guidelines
- Squash merge strategy

**How to invoke**: "Use the git-workflow skill to help me create a proper commit"

#### 4. Testing Strategy

**Skill**: `ng-workflow:testing-strategy`

Comprehensive testing strategy design and implementation.

**Includes**:

- Testing pyramid approach
- Framework selection guide
- Coverage thresholds
- Mocking strategies

**How to invoke**: "Apply the testing-strategy skill to help design tests"

#### 5. Performance Optimization

**Skill**: `ng-workflow:performance-optimisation`

Analyzes and optimizes performance across frontend, backend, and database.

**Focus areas**:

- Bottleneck identification
- Algorithm optimization
- Database query performance
- Frontend rendering optimization

**How to invoke**: "Use the performance-optimisation skill to analyze bottlenecks"

#### 6. Security Review

**Skill**: `ng-workflow:security-review`

Performs security reviews, threat modeling, and remediation guidance.

**Use when**:

- Authentication/authorization changes
- Handling secrets or PII
- Public endpoints or APIs
- Dependency upgrades

**How to invoke**: "Use the security-review skill to assess security risks"

### Hooks

The plugin includes several hooks that automatically run during your workflow:

#### Pre-Tool Use Hooks

**For Edit/Write operations**:

- `protect-files.py`: Prevents modification of protected files
- `security-check.py`: Scans for security issues

**For Bash operations**:

- `log-commands.sh`: Logs all bash commands for audit trail

#### Post-Tool Use Hooks

**For Edit/Write operations**:

- `format-on-edit.py`: Automatically formats code after editing

#### Event Hooks

- `validate-environment.py`: Validates environment on session start
- `validate-prompt.py`: Validates user prompts before submission
- `notify-input.sh`: Provides notifications for user input
- `notify-complete.sh`: Notifies when tasks complete

## Usage

### Using Agents

Agents are automatically available when the plugin is installed and can be invoked by the Claude Code orchestrator when appropriate for your task.

You can also explicitly request an agent:

```
Please use the reviewer agent to check my code changes
```

### Using Skills

Skills are invoked automatically by agents when needed.

To use a skill, simply ask Claude to use it in natural language:

```
Please use the project-analysis skill to analyze this codebase
Can you apply the architecture-patterns skill to help design this feature?
Use the git-workflow skill to help me create a proper commit
```

Skills are automatically available to agents based on their configuration (see agent definitions in the `/agents/` directory).

### Hook Configuration

Hooks are automatically configured via the [hooks/hooks.json](hooks/hooks.json) file. They run transparently during your workflow to ensure code quality and security.

To disable a specific hook, modify the hooks configuration file.

## Examples

### Code Review Workflow

```
# Make your code changes
git add .

# Request a review before committing
"Please use the reviewer agent to check my changes"

# The reviewer will analyze your code and provide feedback
# Address any issues found, then commit with proper conventions
```

### Testing Workflow

```
# After implementing a feature
"Please use the tester agent to create tests for my new feature"

# The tester agent will:
# - Analyze your code
# - Design appropriate test cases
# - Implement unit, integration, and E2E tests
# - Verify coverage thresholds
```

### Debugging Workflow

```
# When encountering a bug
"I'm getting an error: [error message]. Please use the debugger agent to help"

# The debugger will:
# - Reproduce the issue
# - Isolate the problem
# - Diagnose root cause
# - Implement and verify a fix
```

### Refactoring Workflow

```
# To improve code quality
"Please use the refactorer agent to clean up this code"

# The refactorer will:
# - Identify code smells
# - Apply refactoring patterns
# - Ensure tests still pass
# - Improve maintainability
```
