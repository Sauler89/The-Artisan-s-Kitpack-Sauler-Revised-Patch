# Berserker #1003 — Sauler Revised Design

## Status

**Development / alpha.** Static source auditing is in progress. Real WeiDU and in-game validation are still required.

## Design goals

The revised Berserker is intended to be a high-risk melee Fighter whose power increases as Hit Points fall, without inheriting the most extreme scaling or self-damage mechanics of the current upstream Artisan overhaul.

The design combines three reference points:

- the stock BG2EE Berserker and its one-turn Enrage chassis;
- selected ideas from The Artisan's Kitpack Berserker overhaul;
- balance concepts previously explored in the Chriz Balance Patch;

with the final numbers and mechanics chosen for Sauler Revised.

## In Extremis

In Extremis is a permanent passive controller with three Hit Point thresholds.

| Threshold | Melee attack roll | Melee damage | AC penalty | APR |
|---|---:|---:|---:|---:|
| 75% HP or less | -1 | +1 | 2 | — |
| below 50% HP | -2 | +2 | 3 | +0.5 |
| 25% HP or less | -4 | +4 | 4 | +1 |

The attack-roll penalty is deliberate: lower health makes the Berserker more dangerous when a hit connects, but less precise and more exposed.

### Enraged damage interaction

While `STATE_ENRAGED` is active, only the melee damage bonus doubles:

| Threshold | Normal | Enraged |
|---|---:|---:|
| 75% HP or less | +1 | +2 |
| below 50% HP | +2 | +4 |
| 25% HP or less | +4 | +8 |

No additional Enrage THAC0, AC, or APR multiplier is applied.

## Level progression

### Level 1

- In Extremis offense/defense/APR tiers become active.
- Permanent immunity to involuntary berserk effects.
- Enrage available once/day, with another use every four levels thereafter.

### Level 7

In Extremis also grants movement-rate bonuses:

- tier 1: +1;
- tier 2: +2;
- tier 3: +4.

### Level 10

In Extremis also grants bonuses to all Saving Throws:

- tier 1: +1;
- tier 2: +2;
- tier 3: +4.

Implementation uses opcode 325 with signed values `-1/-2/-4`.

### Level 14

In Extremis grants resistance to slashing, crushing, piercing, and missile damage:

- tier 1: 3%;
- tier 2: 6%;
- tier 3: 10%.

While Enraged, equal conditional deltas increase the totals to:

- 6%;
- 12%;
- 20%.

### Level 20

In Extremis adds Luck:

- tier 1: none;
- tier 2: +1;
- tier 3: +2.

## Enrage

### Chassis

The Sauler revision deliberately patches the installed game's stock `SPCL321` rather than installing Artisan's custom Rage engine.

Expected behavior:

- duration: 1 turn / 60 seconds;
- +15 temporary Hit Points retained;
- stock/EE delayed Winded/cooldown machinery retained by leaving `SPCL321D` untouched;
- `STATE_ENRAGED` is explicitly normalized for conditional mechanics and general interoperability;
- wizard and priest spellcasting disabled while Enraged.

### Removed Artisan mechanics

The following upstream Artisan Berserker features are intentionally absent:

- 2-round initial Rage duration;
- 1 HP/second Rage self-damage;
- damage scaling by percentage of missing Hit Points;
- melee-hit Rage refresh;
- 10-round custom Rage cap;
- Reckless Frenzy;
- Extend Rage HLA.

### Enrage immunities

Enrage grants protection from:

- charm;
- confusion;
- fear;
- hold;
- paralysis;
- sleep;
- unconsciousness;
- stun;
- Power Word: Stun;
- morale loss/break.

Enrage deliberately does **not** grant immunity to:

- feeblemind;
- Maze;
- Imprisonment;
- level drain;
- death effects.

The implementation removes related EE Fixpack residue for protections that were intentionally dropped, including the Feeblemind VFX protection and the level-drain scripting/feedback mirror.

## SPLSTATE / interoperability markers

The implementation normalizes the following SPLSTATE immunity markers when available:

- charm immunity;
- confusion immunity;
- hold immunity;
- panic immunity;
- sleep immunity;
- stun immunity.

It also explicitly applies `STATE_ENRAGED` (104).

These markers are retained as general Infinity Engine interoperability metadata. They do **not** make SCS class/kit components part of the supported design target.

### SCS scope for this project

The intended personal installation may use SCS only for **general game tweaks**. SCS components that modify classes, kits, Rage/Enrage, class HLAs, or other kit-specific mechanics are intentionally excluded.

Accordingly, the Berserker is not designed around SCS's class/kit rewrites and does not require them for validation. An optional smoke test with the user's final SCS tweak-only selection is sufficient to ensure those general tweaks do not disturb #1003.

## Ranged policy

The Berserker is not completely prohibited from ranged combat.

Ranged-only weapon groups are capped at one proficiency point. The implementation recognizes stock Enhanced Edition labels as well as Skills and Abilities v5.4's consolidated `BOW` and `MISSILE` rows.

Throwing axes, daggers, and hammers remain governed by their normal weapon proficiencies.

In Extremis attack and damage modifiers use melee-only opcodes, so the core passive does not boost ranged attacks.

## Fighter Overhaul interaction

For now, Sauler Revised intentionally retains the existing upstream #1003 interaction with Artisan Fighter Overhaul #1100:

- Power Attack may remain inherited;
- Expertise is removed;
- Rapid Shot is removed;
- the Fighter Overhaul automatic specialization passive is removed.

This is an inherited compatibility decision and can be reviewed later independently from the Berserker redesign.

## HLA policy

- Hardiness remains available.
- No Berserker-specific HLA table replaces the Fighter HLA table.
- Extend Rage is not installed.
- Skills and Abilities #710/#720 can therefore add/update Fighter HLAs without #1003 replacing their table or `SPCL907`.

## CLAB and dual-class design

Five separate permanent controllers are granted at levels:

- 1: `C0BRI1`
- 7: `C0BRI7`
- 10: `C0BRI10`
- 14: `C0BRI14`
- 20: `C0BRI20`

This separation is intentional for dual-class robustness. A character who stops advancing as a Berserker at level 7 should not later gain the level 10/14/20 Berserker progression merely by advancing another class.

## Threshold implementation

HP threshold controllers use opcode 232 with `HPPercentLT` semantics:

- 76 → 75% HP or less;
- 50 → below 50%;
- 26 → 25% HP or less.

Temporary tier resources refresh for 12 seconds and begin with opcode 321 sibling cleanup. This prevents overlapping tiers and cleans up state when crossing thresholds.

## Runtime resources

All Sauler runtime resrefs remain within the engine's eight-character resource-name limit and use the `C0BR` namespace.

The implementation creates runtime SPL shells from the installed game's `SPCL321`, removes inherited effects from those shells, and then builds the revised controllers/effects through WeiDU. This avoids shipping another large binary spell tree for the revised mechanics.

## Required validation before beta

- real WeiDU v251 install;
- uninstall/reinstall safety;
- BG2EE/EET startup;
- level 1/7/10/14/20 progression;
- exact 75/50/25 threshold transitions;
- attack/damage/AC/APR measurements;
- Enrage duration and +15 HP behavior;
- Winded/cooldown behavior;
- all intended immunities and all deliberately missing immunities;
- spellcasting lockout;
- optional SCS general-tweak-only smoke test, with class/kit-changing SCS components excluded;
- S&A v5.4 #150 and proficiency-overhaul interaction;
- HLA/Hardiness availability;
- dual-class cases.
