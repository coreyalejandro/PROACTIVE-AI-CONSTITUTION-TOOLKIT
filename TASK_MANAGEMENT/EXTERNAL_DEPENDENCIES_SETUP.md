# External Dependencies: Setup Checklist

## Purpose
Complete this on a GREEN day. Then these aren't blocking you on RED days.

## Required Accounts

### Weights & Biases (Adapter 01)
- [ ] Account created: https://wandb.ai/
- [ ] API key generated: Settings → API Keys
- [ ] API key stored locally: `echo "YOUR_KEY" > ~/.wandb_key`
- [ ] Test login: `wandb login`
- [ ] Test project created: `wandb init`

**Status**: [ ] READY / [ ] BLOCKED BY: ___________

### GitHub with Actions (Adapter 02)
- [ ] Repo exists: /Users/coreyalejandro/Projects/PROACTIVE-AI-CONSTITUTION-TOOLKIT
- [ ] GitHub remote configured: `git remote -v`
- [ ] Actions enabled: Repo → Settings → Actions → General → Allow all actions
- [ ] Test workflow runs: Create `.github/workflows/test.yml`, push, check Actions tab

**Status**: [ ] READY / [ ] BLOCKED BY: ___________

### HELM (Adapter 03)
- [ ] Python environment ready: `python --version` (3.8+)
- [ ] HELM installed: `pip install crfm-helm`
- [ ] Test run: `helm-run --help`
- [ ] Disk space available: HELM datasets can be large (10GB+)

**Status**: [ ] READY / [ ] BLOCKED BY: ___________

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
Last updated: 2026-01-19
Blocking issues: [NONE / LIST]

---
## V&T

- Created: 2026-01-19T06:00:00Z
- Status: COMPLETE
- Blocked by: nothing
