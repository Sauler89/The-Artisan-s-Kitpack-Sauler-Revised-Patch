# Changelog

All notable downstream changes to **The Artisan's Kitpack — Sauler Revised Patch** are documented here.

This changelog records Sauler Revised changes only. For the complete history of components inherited unchanged from The Artisan's Kitpack, refer to the upstream repository.

## [Unreleased]

### Added

- Established the Sauler Revised downstream project structure.
- Added upstream baseline tracking against `TheArtisanBG/The-Artisan-s-Kitpack`.
- Added documentation for revised components and compatibility policy.
- Added static QA infrastructure and upstream-change monitoring.

### Changed

- Updated mod metadata to identify the package as **The Artisan's Kitpack - Sauler Revised Patch** while retaining explicit original-author credit.
- Component **#1003 Berserker Overhaul** now routes to the downstream `Berserker_Sauler_Revised.tpa` implementation.

### Berserker #1003 — Sauler Revised

- Replaced Artisan's +2/+4/+8 In Extremis offense curve with a risk/reward progression:
  - 75% HP or less: -1 melee attack roll, +1 melee damage, 2 AC penalty;
  - below 50% HP: -2 melee attack roll, +2 melee damage, 3 AC penalty, +0.5 APR;
  - 25% HP or less: -4 melee attack roll, +4 melee damage, 4 AC penalty, +1 APR.
- While Enraged, In Extremis melee damage doubles to +2/+4/+8.
- Level 7 movement progression changed to +1/+2/+4.
- Level 10 Saving Throw progression changed to +1/+2/+4.
- Level 14 now grants 3%/6%/10% physical resistance, doubled while Enraged.
- Level 20 Luck progression changed to 0/+1/+2.
- Restored stock one-turn `SPCL321` Enrage architecture as the base.
- Retained +15 temporary Hit Points and normal Winded/cooldown behavior.
- Removed Artisan continuous Enrage self-damage.
- Removed Artisan missing-HP percentage damage ladder.
- Removed melee-hit Rage-duration refresh.
- Removed Reckless Frenzy.
- Removed Extend Rage HLA.
- Preserved Hardiness.
- Restricted Enrage immunities to selected control/morale effects.
- Removed Feeblemind, Maze, Imprisonment, and Level Drain immunity.
- Added cleanup for EE Fixpack Feeblemind/Level Drain residue that should not survive the revised immunity policy.
- Normalized STATE_ENRAGED and Detectable Spells markers for SCS awareness.
- Disabled wizard and priest spellcasting while Enraged.
- Capped ranged-only weapon groups at one proficiency point while preserving throwing-weapon access.
- Added compatibility handling for Skills and Abilities v5.4 consolidated `BOW`/`MISSILE` proficiency groups while leaving `THROWN` and `ARCHERY` unchanged.
- Preserved the existing Artisan Fighter Overhaul interaction for Expertise, Rapid Shot, and the Fighter specialization passive.
- Added separate level 1/7/10/14/20 controllers for dual-class-safe progression.
- Added anti-stacking cleanup for threshold refreshes and Enrage-only deltas.

### Validation status

- Static source audit: in progress / passing current invariants.
- WeiDU v251.00 real install test: pending.
- In-game BG2EE/EET test: pending.

## [0.1.0-alpha1] — planned

First development release of the Sauler Revised fork, targeted to include the integrated Berserker #1003 revision as the first completed downstream component.
