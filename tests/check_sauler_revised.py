#!/usr/bin/env python3
"""Static source invariants for The Artisan's Kitpack — Sauler Revised Patch.

These checks deliberately do not pretend to replace WeiDU or in-game QA. They
catch accidental source regressions in downstream-owned components.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "ArtisansKitpack" / "lib" / "Berserker.tpa"
BERSERKER = ROOT / "ArtisansKitpack" / "lib" / "Berserker_Sauler_Revised.tpa"
TP2 = ROOT / "ArtisansKitpack" / "ArtisansKitpack.TP2"

failures: list[str] = []
passes: list[str] = []


def check(name: str, condition: bool) -> None:
    (passes if condition else failures).append(name)


def executable_text(text: str) -> str:
    """Remove // comments and /* */ blocks for simple executable-code assertions."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return "\n".join(line.split("//", 1)[0] for line in text.splitlines())


router = ROUTER.read_text(encoding="utf-8")
berserker = BERSERKER.read_text(encoding="utf-8")
code = executable_text(berserker)
tp2 = TP2.read_text(encoding="utf-8")

check("#1003 still exists", "DESIGNATED 1003" in tp2)
check("#1003 still includes upstream Berserker router", "INCLUDE ~%MOD_FOLDER%/lib/Berserker.tpa~" in tp2)
check("Berserker router points to Sauler implementation", "Berserker_Sauler_Revised.tpa" in router)

# Core identity / removed upstream mechanics.
check("uses stock SPCL321 Enrage progression", "GA_SPCL321" in code)
check("does not restore permanent stock AP_SPCL322 casting-button lock", "AP_SPCL322" not in code)
check("does not grant Artisan custom Enrage", "GA_C0BER#00" not in code)
check("does not grant Reckless Frenzy", "GA_C0BER#05" not in code and "Reckless Frenzy" not in code)
check("does not install Extend Rage HLA", "C0BER#H1" not in code and "patch_add_hla" not in code)
check("does not remove Hardiness through HLA helpers", "patch_remove_hla" not in code)
check("does not replace Fighter HLA abbreviation/table", "luabbr.2da" not in code.lower() and "lufi0.2da" not in code.lower())
check("does not patch SPCL907", "spcl907" not in code.lower())
check("does not patch SPCL321D", "spcl321d" not in code.lower())

# Progression controllers.
for level, res in [(1, "C0BRI1"), (7, "C0BRI7"), (10, "C0BRI10"), (14, "C0BRI14"), (20, "C0BRI20")]:
    check(f"level {level} controller present", f"AP_{res}" in code)

check("level 7 movement family present", all(x in code for x in ("C0BRM1", "C0BRM2", "C0BRM3")))
check("level 10 save family present", all(x in code for x in ("C0BRS1", "C0BRS2", "C0BRS3")))
check("level 14 resistance family present", all(x in code for x in ("C0BRR1", "C0BRR2", "C0BRR3", "C0BRX1", "C0BRX2", "C0BRX3")))
check("level 20 Luck family present", all(x in code for x in ("C0BRL1", "C0BRL2", "C0BRL3")))

# Enrage ownership / cleanup.
check("patches SPCL321 in place", "COPY_EXISTING ~spcl321.spl~ ~override~" in code)
check("explicit STATE_ENRAGED support", "parameter2 = 104" in code and "stat = 0x112" in code)
check("spellcasting lockout present", "opcode = 145" in code and "match_parameter2 = 0" in code and "match_parameter2 = 1" in code)
check("Feeblemind immunity is removed", "match_parameter2 = 76" in code and "cdfeeble" in code.lower())
check("Maze immunity is removed", "match_parameter2 = 213" in code)
check("Imprisonment immunity is removed", "match_parameter2 = 211" in code)
check("Level Drain immunity/mirror cleanup present", "match_parameter2 = 216" in code and "match_opcode = 282" in code)

# Ranged/S&A policy.
check("stock ranged groups recognized", all(x in code for x in ("~CROSSBOW~", "~LONGBOW~", "~SHORTBOW~", "~DART~", "~SLING~")))
check("S&A BOW/MISSILE groups recognized", "~BOW~" in code and "~MISSILE~" in code)
check("S&A THROWN style is not patched", "~THROWN~" not in code)
check("S&A ARCHERY style is not patched", "~ARCHERY~" not in code)

# Preserve upstream Fighter Overhaul interaction currently inherited by #1003.
check("Expertise removal retained", "GA_C0FIG02" in code)
check("Rapid Shot removal retained", "GA_C0ARC03" in code and "AP_C0ARC03Z" in code)
check("Fighter specialization-passive removal retained", "AP_C0FIG04" in code)

# Resource namespace safety.
resrefs = sorted(set(re.findall(r"\bC0BR[A-Z0-9]+\b", berserker, flags=re.I)))
check("Sauler runtime resource namespace exists", bool(resrefs))
check("all Sauler C0BR runtime resrefs fit 8-char IE limit", all(len(r) <= 8 for r in resrefs))
check("old Artisan Berserker SPL tree is not bulk-copied", "Fighter/Berserker/SPELLS~ ~OVERRIDE" not in code)
check("only intended upstream Berserker icon namespace is reused", not any(r for r in re.findall(r"\bC0BER#[A-Z0-9]+\b", code, flags=re.I) if r.upper() != "C0BER#IC"))

print(f"Sauler Revised static QA: {len(passes)} PASS, {len(failures)} FAIL")
for name in passes:
    print(f"PASS: {name}")
for name in failures:
    print(f"FAIL: {name}", file=sys.stderr)

if failures:
    sys.exit(1)
