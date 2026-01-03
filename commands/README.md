# Commands

Custom slash commands exposed by the plugin.

## Available Commands

### `/ng-workflow:feature-dev`

Guided feature development workflow with deep codebase discovery, clarification, and architecture design before implementation.

**Usage**:

```
/ng-workflow:feature-dev
/ng-workflow:feature-dev "Add CSV export to reports"
```

### `/ng-workflow:commit-push-pr`

Runs the full git workflow: commit staged changes, push the branch, and open a PR via `gh pr create`.

**Usage**:

```
/ng-workflow:commit-push-pr
```

### `/ng-workflow:review-pr`

Comprehensive PR review using specialized agents. Optionally limit review aspects or run in parallel.

**Usage**:

```
/ng-workflow:review-pr
/ng-workflow:review-pr tests errors
/ng-workflow:review-pr all parallel
```
