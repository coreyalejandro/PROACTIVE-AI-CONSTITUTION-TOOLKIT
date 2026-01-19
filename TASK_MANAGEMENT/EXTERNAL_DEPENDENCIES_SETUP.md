# External Dependencies: Setup Checklist

## Purpose
Complete this on a GREEN day. Then these aren't blocking you on RED days.

## Required Accounts

### Weights & Biases (Adapter 01)
- [x] Account created: https://wandb.ai/ (coreyalejandro)
- [x] API key generated: Settings → API Keys (v1 format, 86 chars)
- [x] API key stored locally: ~/.netrc (auto-created by wandb login)
- [x] Test login: `wandb login` ✓ verified 2026-01-19
- [ ] Test project created: `wandb init`

**Status**: [x] READY / [ ] BLOCKED BY: ___________

### GitHub with Actions (Adapter 02)
- [x] Repo exists: /Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT
- [x] GitHub remote configured: `git remote -v` ✓
- [x] Actions enabled: Repo → Settings → Actions → General → Allow all actions ✓
- [x] Test workflow runs: `.github/workflows/test-actions.yml` ✓ (verified 2026-01-19, 8s run)

**Status**: [x] READY / [ ] BLOCKED BY: ___________

### HELM (Adapter 03)
- [x] Python environment ready: `python --version` (3.8+)
- [x] HELM installed: `pip install crfm-helm`
- [x] Test run: `helm-run --help` ✓ (verified 2026-01-19)
- [ ] Disk space available: HELM datasets can be large (10GB+)

**Status**: [x] READY / [ ] BLOCKED BY: ___________

### Anthropic API (General)
- [ ] API key available
- [ ] Key stored securely
- [ ] Test call works: `curl` or Python test

**Status**: [ ] READY / [ ] BLOCKED BY: ___________

## Development Environment

### Python
- [ ] Version: `python --version` → 3.8+ required
- [ ] Virtual environment: `python -m venv .venv && source .venv/bin/activate`
- [ ] Dependencies file: `requirements.txt` exists

### Git
- [ ] Configured: `git config user.email` returns valid email
- [ ] SSH key (if using SSH): `ssh -T git@github.com` succeeds

### Editor/IDE
- [ ] Cursor installed and working
- [ ] Can open project: `cursor /Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT`

## Completion Gate

All items checked = GREEN LIGHT for adapter development

Any item blocked = Document blocker, seek help on YELLOW/GREEN day

---
Last updated: 2026-01-19 (W&B + HELM verified)
Blocking issues: NONE

---
## V&T

- Created: 2026-01-19T06:00:00Z
- Status: COMPLETE
- Blocked by: nothing
