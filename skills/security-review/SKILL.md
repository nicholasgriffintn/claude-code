---
name: security-review
description: A specialist skill for security reviews, threat modeling, and remediation guidance. Use for auth/permissions changes, secrets or PII handling, public endpoints, or dependency upgrades.
---

# Security Review Skill

## Workflow

Copy this checklist and use it to track your progress through a security review:

```markdown
Security Review Checklist

- [ ] Scope the Change
  - [ ] Identify entry points, data flows, and trust boundaries.
  - [ ] Note any changes to auth, secrets, or external integrations.
- [ ] Threat Model
  - [ ] Enumerate likely threats (STRIDE or similar).
  - [ ] Focus on inputs, storage, and outputs.
- [ ] Validate Input & Output
  - [ ] Validate and sanitize user-controlled input.
  - [ ] Encode outputs to prevent injection.
  - [ ] Constrain file paths and URLs (avoid traversal/SSRF).
- [ ] AuthN/AuthZ
  - [ ] Authentication checks are present and consistent.
  - [ ] Authorization rules are explicit and least-privilege.
  - [ ] Session/token handling uses secure defaults.
- [ ] Secrets & PII
  - [ ] No hardcoded secrets or credentials.
  - [ ] Logs avoid sensitive data.
  - [ ] Storage and transport are protected.
- [ ] Dependency Risk
  - [ ] New dependencies are minimal and justified.
  - [ ] Lockfiles updated and reviewed.
- [ ] Verification
  - [ ] Add or update tests for security-sensitive behavior.
  - [ ] Confirm error handling does not leak data.
```

## Remediation Notes

When issues are found, propose the smallest safe change that addresses the risk, then add or update tests to prevent regressions.
