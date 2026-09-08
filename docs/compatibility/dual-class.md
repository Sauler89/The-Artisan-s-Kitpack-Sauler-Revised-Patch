# Berserker Dual-Class / Multikit Notes

## SPCL322 policy

The stock Berserker CLAB traditionally includes `AP_SPCL322`, whose purpose is to disable the magic-casting button.

Sauler Revised #1003 deliberately does **not** restore `AP_SPCL322` after rebuilding `CLABFI02` from the Fighter base CLAB.

This is intentional because the revised design has a narrower casting restriction:

- spellcasting should be available normally when the character's other class/kit permits it;
- wizard and priest casting should be disabled **only while Enraged**;
- the temporary Enrage restriction is implemented directly in `SPCL321` with opcode 145;
- once Enrage ends, that temporary restriction expires.

This differs from the earlier standalone Berserker Reforged prototype, which patched the existing Berserker CLAB in place and therefore inherited `AP_SPCL322` automatically.

The integrated implementation is intended to be safer for dual-class and multikit use, but this behavior must still be verified in-game before beta.

## Separate level controllers

Sauler Revised grants its progression through separate CLAB resources at levels 1, 7, 10, 14, and 20 rather than one controller that internally unlocks everything by current Fighter level.

This is intended to prevent a character who stops gaining Berserker levels from later receiving higher-tier Berserker progression because another class continues to advance.

Required tests include at minimum:

- Berserker 7 → Mage;
- Berserker 9 → Mage;
- Berserker 13 → Mage/Cleric where supported by the installed framework;
- regain original class abilities;
- cast wizard/priest spells outside Enrage;
- verify casting is blocked during Enrage;
- verify casting returns after Enrage;
- verify no level 10/14/20 Berserker controllers appear unless those Berserker levels were actually reached;
- A7 MultiKits combinations that use the Berserker kit, if included in the target mod stack.
