# Tests

`check_sauler_revised.py` contains fast static regression checks for downstream-owned source.

Run locally from the repository root with:

```bash
python tests/check_sauler_revised.py
```

GitHub Actions runs the same checks automatically.

These tests currently verify the Berserker #1003 ownership and design invariants, including:

- component #1003 still routes through the Sauler implementation;
- stock `SPCL321` Enrage progression is used;
- permanent `AP_SPCL322` casting-button lock is not restored;
- Reckless Frenzy and Extend Rage remain absent;
- Hardiness/HLA tables are not replaced;
- level 1/7/10/14/20 controllers remain present;
- Enrage state/casting/immunity cleanup remains represented in source;
- S&A v5.4 `BOW`/`MISSILE` support remains present while `THROWN`/`ARCHERY` are not patched;
- Sauler runtime resrefs remain within the eight-character Infinity Engine limit.

## What these tests do not prove

Static tests cannot prove that WeiDU parses every statement correctly or that engine opcodes behave as intended. A public beta still requires real install/uninstall and in-game tests on the supported game/mod configurations.
