# Commit Convention

This repository follows simplified [Conventional Commits](https://www.conventionalcommits.org/).

## Format

```
type: description
```

- Lowercase, imperative mood, under 72 characters.

## Types

| Type | Purpose |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `chore` | Maintenance and housekeeping |
| `refactor` | Code restructuring (no behavior change) |
| `test` | Adding or updating tests |
| `ci` | CI/CD changes |

## Scope (optional)

```
feat(api): add health endpoint
```

## Breaking Changes

```
feat!: change response format
```

For full details, see the [governance policies](https://towlion.github.io/platform/governance/#commit-conventions).
