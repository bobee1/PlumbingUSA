# PipeMend (pipemend.us)

Static site for PipeMend, a nationwide plumbing services brand (repairs, drains, water heaters, sewer and gas lines).

- Build status and what comes next: [STATUS.md](STATUS.md)
- Step-by-step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md)

## Build
```
python3 build.py          # writes public/
python3 scripts/audit.py  # must print "PASS: 0 issues"
```
Cloudflare Pages: build output directory `public`, no build command (output is committed). `functions/api/lead.js` handles the contact form (needs `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`).
