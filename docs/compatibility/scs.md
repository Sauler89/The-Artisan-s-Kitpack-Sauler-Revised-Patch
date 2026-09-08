# Sword Coast Stratagems (SCS) Compatibility Scope

## Project policy

For the intended Sauler89 BG2EE/EET installation, **Sword Coast Stratagems is used only for general game tweaks**.

SCS is **not** used as a class/kit overhaul source in this setup.

Therefore, components that modify or replace any of the following are intentionally outside the target configuration:

- Fighter or Berserker class/kit mechanics;
- Rage / Enrage behavior;
- class or kit HLAs;
- class/kit proficiency progression;
- kit-specific innate abilities;
- other SCS class/kit rewrites that would compete with The Artisan's Kitpack — Sauler Revised Patch or Skills and Abilities.

## Authority for class and kit mechanics

For this project, the intended ownership is:

1. **The Artisan's Kitpack — Sauler Revised Patch** for selected revised Artisan kits, beginning with Berserker #1003;
2. **Skills and Abilities v5.4** for the S&A Fighter progression/proficiency/HLA components explicitly selected by the user;
3. **SCS only for general non-class/kit tweaks**.

If an SCS component would rewrite a class or kit mechanic already owned by Sauler Revised or S&A, that SCS component should be skipped.

## Berserker #1003

The Sauler Revised Berserker does not require SCS class/kit components.

Its `SPLSTATE` and `STATE_ENRAGED` markers are retained as general engine/interoperability metadata, not because the design depends on SCS.

The required Berserker validation matrix therefore does **not** include SCS class/kit testing.

At most, a final optional smoke test should be performed with the user's actual SCS **general-tweak-only** selection to confirm that those chosen general tweaks do not disturb Berserker #1003.

## Recommended high-level order

For the current intended setup:

1. base fixes / EE Fixpack;
2. The Artisan's Kitpack — Sauler Revised Patch;
3. optional SCS general game tweaks only;
4. other late gameplay/tweak mods as appropriate;
5. Skills and Abilities v5.4;
6. `EET_END`, when using EET.

This document describes project scope, not a claim that every possible SCS general tweak has already been individually compatibility-tested.
