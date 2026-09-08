# The Artisan's Kitpack — Sauler Revised Patch

A curated downstream revision of **The Artisan's Kitpack** by AionZ / The Artisan.

The original kits, artwork, resources, architecture, and core design belong to their original author(s). This fork keeps The Artisan's Kitpack as its foundation and changes only components that are explicitly documented as **Sauler Revised**. Components not listed below are intended to remain aligned with upstream.

- **Original project:** https://github.com/TheArtisanBG/The-Artisan-s-Kitpack
- **Sauler Revised fork:** https://github.com/Sauler89/The-Artisan-s-Kitpack-Sauler-Revised-Patch
- **Current upstream baseline:** `85928f964f6965fd37980bf679d7eeb9af410256`

> **Development status:** early alpha. The current Berserker implementation has undergone static source auditing, but still requires a real WeiDU install/uninstall test and in-game verification before a stable release.

## Project goals

Sauler Revised is not intended to replace every design decision in The Artisan's Kitpack. Its goals are to:

- retain the upstream Kitpack as the base;
- revise selected kits one at a time;
- document every intentional divergence from upstream;
- improve balance, mechanical consistency, bug resistance, and compatibility where useful;
- preserve compatibility with heavily modded BG2EE/EET installations whenever practical;
- make future upstream synchronization reviewable instead of silently overwriting downstream changes.

## Sauler Revised components

### #1003 — Berserker Overhaul

**Status:** implemented on the development branch; installer/in-game testing pending.

The upstream Berserker has been redesigned around a lower-powered, risk/reward **In Extremis** progression and the stock Enhanced Edition one-turn Enrage chassis.

#### In Extremis

| Hit Points | Melee attack roll | Melee damage | AC penalty | APR |
|---|---:|---:|---:|---:|
| 75% or less | -1 | +1 | 2 | — |
| below 50% | -2 | +2 | 3 | +0.5 |
| 25% or less | -4 | +4 | 4 | +1 |

While Enraged, only the In Extremis melee damage bonus doubles, to **+2 / +4 / +8**.

Additional progression:

- **Level 7:** movement rate +1 / +2 / +4.
- **Level 10:** all Saving Throws +1 / +2 / +4.
- **Level 14:** 3% / 6% / 10% physical resistance; doubled while Enraged to 6% / 12% / 20%.
- **Level 20:** Luck 0 / +1 / +2.
- Permanent immunity to involuntary berserk effects.

#### Enrage

The revised component patches the installed game's `SPCL321` rather than installing Artisan's custom two-round, self-draining Rage engine.

- duration: **1 turn**;
- retains +15 temporary Hit Points;
- retains the normal post-Enrage Winded/cooldown machinery;
- no continuous self-damage;
- no missing-HP percentage damage ladder;
- no melee-hit duration refresh;
- no Reckless Frenzy;
- no Extend Rage HLA;
- Hardiness remains available;
- wizard and priest spellcasting is disabled while Enraged.

Enrage protects against charm, confusion, fear, hold, paralysis, sleep, unconsciousness, stun, Power Word: Stun, and morale failure. It deliberately does **not** protect against feeblemind, Maze, Imprisonment, level drain, or death effects.

#### Ranged weapons

Ranged-only weapon groups are capped at one proficiency point. Throwing axes, daggers, and hammers remain usable through their normal melee weapon proficiencies. In Extremis offensive bonuses are melee-only.

Full design and implementation notes: [docs/plans/berserker-revised-design.md](docs/plans/berserker-revised-design.md)

### Red Wizard

**Status:** planned / next revision target.

The Red Wizard will be integrated using the same rule: preserve upstream architecture unless a documented Sauler revision intentionally changes it.

## Components not listed above

Unless explicitly recorded in [SAULER-REVISIONS.md](SAULER-REVISIONS.md), components are intended to remain based on The Artisan's Kitpack upstream implementation.

## Compatibility and install order

The Berserker revision is being designed for BG2EE/EET mod stacks that can include EE Fixpack, SCS, and Skills and Abilities.

Recommended high-level order for the current development build:

1. base fixes / EE Fixpack;
2. The Artisan's Kitpack — Sauler Revised Patch, including **#1003 Berserker Overhaul**;
3. SCS;
4. other late gameplay mods;
5. Skills and Abilities v5.4;
6. `EET_END`, if applicable.

The exact S&A v5.4 compatibility notes are documented in [docs/compatibility/skills-and-abilities.md](docs/compatibility/skills-and-abilities.md).

### Skills and Abilities v5.4

The compatibility audit is based on the exact **Skills and Abilities v5.4 release archive**, not an arbitrary GitHub snapshot.

- #150 Fighter abilities are expected to coexist with the Berserker progression.
- #311/#312/#313 proficiency overhauls are recognized through their consolidated `BOW` / `MISSILE` rows.
- S&A `THROWN` and `ARCHERY` styles are intentionally left untouched.
- #710/#720 HLA changes coexist because the revised Berserker does not replace the Fighter HLA table or patch Hardiness (`SPCL907`).
- S&A #190 (Berserker Enrage update) is disabled in the audited v5.4 release. If re-enabled by an older/custom build, it conflicts with this Berserker revision and should not be installed.

## Upstream maintenance

The fork records a known upstream baseline in [docs/upstream/BASELINE.md](docs/upstream/BASELINE.md). A GitHub Actions workflow checks for new upstream commits and highlights changes that overlap Sauler-owned files.

The intended synchronization policy is:

- upstream changes to untouched components: normally importable;
- upstream changes to a Sauler Revised component: manual review required;
- downstream-only implementation files: never overwritten automatically.

## Development and QA

Static checks live under `tests/` and are intended to catch accidental regressions such as restoring Reckless Frenzy, removing Hardiness, losing `SPCL321`, exceeding the Infinity Engine eight-character resource limit, or overwriting S&A-specific proficiency styles.

Static QA does **not** replace testing on a real BG2EE/EET installation. Before the first public beta, #1003 must pass at minimum:

- WeiDU install, reinstall, uninstall, and rollback;
- BG2EE and/or EET launch;
- levels 1, 7, 10, 14, and 20;
- HP thresholds 75%, 50%, and 25%;
- Enrage start/end and Winded behavior;
- dual-class progression;
- SCS AI/Detectable Spells behavior;
- Skills and Abilities v5.4 interaction;
- Hardiness/HLA availability.

## Credits

- **AionZ / The Artisan / Artemius_I** — The Artisan's Kitpack, original kits, code, assets, architecture, and design.
- **Chrizhermann** — reference downstream-fork structure and useful prior balance/compatibility research.
- **Morpheus562** — Skills and Abilities.
- **Gibberlings3 contributors** — EE Fixpack and Infinity Engine modding resources.
- **WeiDU contributors** — installer framework.
- **Sauler89** — Sauler Revised design, balancing, integration, compatibility work, and maintenance.

This fork is a downstream derivative project. Original authorship should remain clearly credited wherever the project is distributed.
