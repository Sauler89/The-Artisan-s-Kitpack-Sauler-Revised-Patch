# Skills and Abilities v5.4 Compatibility

## Source of truth

This compatibility work was audited against the user's exact **Skills and Abilities v5.4 release archive** (`Skills-and-Abilities-5.4.zip`), not against an unrelated or potentially newer GitHub snapshot.

These notes therefore describe **v5.4** specifically.

## Recommended order

For a heavily modded BG2EE/EET installation:

1. base fixes / EE Fixpack;
2. **The Artisan's Kitpack — Sauler Revised Patch #1003 Berserker Overhaul**;
3. SCS;
4. other mods that should precede Skills and Abilities;
5. **Skills and Abilities v5.4**;
6. `EET_END`, when using EET.

Unlike the earlier standalone Berserker Reforged prototype, the integrated fork currently has no separate `#1010` compatibility-tail component. Compatibility is designed into #1003 itself where possible.

## #150 — Add New Fighter Abilities

S&A v5.4 applies its Fighter progression to the vanilla `BERSERKER` kit.

Relevant additions are:

- level 1: `GA_MO2WIND` — Second Wind / Recuperare Energie;
- level 9: `AP_MO#IND01`;
- level 13: `AP_MO#IND02`;
- level 17: `AP_MO#IND03`;
- level 20: `AP_MO#APB01`.

The three `MO#IND` SPL files were inspected directly in the v5.4 archive. Each grants +1 permanently to all five Saving Throws, producing a cumulative progression of +1 / +2 / +3 at levels 9 / 13 / 17.

`MO#APB01` was also inspected directly and grants +0.5 APR permanently.

These bonuses are treated as universal S&A Fighter progression and are allowed to stack with Sauler Revised In Extremis.

### Resulting high-level stacking

At Fighter level 17+, S&A's cumulative +3 all saves combines with In Extremis as follows:

- tier 1: +4 total all-save bonus;
- tier 2: +5;
- tier 3: +7.

At level 20+, S&A's permanent +0.5 APR combines with In Extremis:

- tier 1: +0.5 total extra APR;
- tier 2: +1.0;
- tier 3: +1.5.

This stacking is intentional in the current design.

## #311 / #312 / #313 — Proficiency Overhaul

S&A v5.4 consolidates several stock weapon groups and introduces additional proficiency/style rows.

Relevant consolidated ranged weapon groups include:

- `BOW`;
- `MISSILE`.

Relevant S&A style/progression rows include, among others:

- `ARMOR`;
- `SPELLCRAFT`;
- `DEVOTION`;
- `CONDITIONING`;
- `SWIFTBLADE`;
- `THROWN`;
- `ARCHERY`.

The Sauler Revised Berserker proficiency patch recognizes `BOW` and `MISSILE` and caps those actual ranged-only weapon groups at one pip.

It deliberately does **not** alter `THROWN`, `ARCHERY`, or the other S&A style rows.

### Intended interactions

- S&A Armor/Devotion/Swiftblade investment may offset some of In Extremis' defensive penalties; this costs proficiency choices and is allowed.
- Conditioning movement bonuses may stack with In Extremis movement bonuses.
- Fighter kits in the audited v5.4 configuration do not reach Conditioning rank 4 (Tireless), so the Berserker's Winded drawback remains meaningful.
- S&A Archery/Thrown bonuses improve ranged options, but Sauler Revised In Extremis offensive modifiers remain melee-only.

## #190 — Update Berserker's Enrage Ability

The source file for this component still exists in the v5.4 archive, but the entire TP2 component #190 is commented out/disabled in the audited release.

Therefore a normal S&A v5.4 installation does **not** rewrite `SPCL321` through #190.

If an older or custom S&A build exposes/enables #190, **do not install it with Sauler Revised Berserker #1003**. Its Rage rewrite conflicts directly with this component's `SPCL321` ownership.

## #710 — New HLAs

Compatible by architecture.

Sauler Revised #1003 does not replace the Fighter HLA table, so S&A's additional Fighter/warrior HLA choices can remain available.

## #720 — Update Existing HLAs

Compatible by architecture.

Sauler Revised #1003 does not patch Hardiness (`SPCL907`), so S&A's changes to Hardiness can survive intact.

## Why there is no integrated #1010 tail

The earlier standalone `Berserker Reforged` alpha used a separate S&A compatibility-tail component because it was an independent mod installed around another Kitpack.

Inside the Sauler Revised fork, #1003 owns the Berserker overhaul directly. Its ranged-proficiency code already understands the S&A consolidated labels if S&A happens to be installed earlier, while the recommended order still places S&A later so S&A can add its Fighter progression normally.

If future testing shows that a late post-S&A normalizer is still necessary for a real mega-mod order, it should be introduced as an explicit fork-level compatibility component rather than silently embedding a second ownership pass.

## Test matrix still required

Before beta, verify at least:

- #1003 alone;
- #1003 + S&A #150;
- #1003 + each supported #311/#312/#313 proficiency option;
- #1003 + #150 + proficiency overhaul;
- #1003 + #710/#720;
- full preferred S&A selection;
- EET order with `EET_END`;
- save/APR values at levels 17 and 20;
- BOW/MISSILE caps and THROWN/ARCHERY preservation.
