# Sauler Revised Component Registry

This file is the authoritative registry of intentional downstream divergences from **The Artisan's Kitpack**.

If a component or source path is not listed here, the project should treat upstream behavior as authoritative unless a separate documented compatibility fix says otherwise.

## Revision states

- **Upstream** — intended to remain aligned with The Artisan's Kitpack.
- **Planned** — selected for a future Sauler revision but not yet implemented.
- **Development** — downstream implementation exists but has not completed installer/in-game QA.
- **Beta** — installer and basic in-game QA passed; broader compatibility testing ongoing.
- **Stable** — revision is considered release-ready for the supported environments.

## Current registry

| Component | TP2 ID | State | Upstream base | Sauler-owned implementation |
|---|---:|---|---|---|
| Berserker Overhaul | 1003 | **Development** | `ArtisansKitpack/lib/Berserker.tpa` | `ArtisansKitpack/lib/Berserker_Sauler_Revised.tpa` |
| Red Wizard | TBD | **Planned** | Artisan upstream | TBD after audit |
| All other components | — | **Upstream** | Artisan upstream | none unless added here later |

## #1003 Berserker Overhaul

### Upstream ownership boundary

The upstream entry path remains:

`ArtisansKitpack/lib/Berserker.tpa`

In this fork it is intentionally a minimal router to:

`ArtisansKitpack/lib/Berserker_Sauler_Revised.tpa`

This split is deliberate. When Artisan changes the upstream `Berserker.tpa`, the change remains obvious during synchronization instead of being buried inside a large downstream-modified file.

The original `ArtisansKitpack/Fighter/Berserker/` binary/resource tree remains in the repository for upstream parity and review. The Sauler Revised #1003 component does not bulk-install the old Berserker SPL/EFF/2DA package. It currently reuses only the original `C0BER#IC.BAM` In Extremis portrait icon asset.

### Sauler-owned runtime resources

The implementation generates its spell resources at install time from the installed game's `SPCL321` shell. Current runtime resrefs use the `C0BR` namespace and stay within the Infinity Engine eight-character limit.

Controllers:

- `C0BRI1`
- `C0BRI7`
- `C0BRI10`
- `C0BRI14`
- `C0BRI20`

Tier and delta families:

- offense: `C0BRO1`–`C0BRO3`, `C0BRD1`–`C0BRD3`;
- movement: `C0BRM1`–`C0BRM3`;
- saves: `C0BRS1`–`C0BRS3`;
- physical resistance: `C0BRR1`–`C0BRR3`, `C0BRX1`–`C0BRX3`;
- Luck: `C0BRL1`–`C0BRL3`.

### Shared upstream code intentionally reused

The Berserker revision currently relies on shared Artisan infrastructure without modifying it, including:

- `ADD_SPLPROT_ENTRY`;
- `set_clab_2da_entries`;
- `GET_KIT_STRREF`;
- standard spell-effect helper functions.

Changes to these shared functions upstream should therefore be reviewed for compatibility even though they are not Sauler-owned paths.

### Fighter Overhaul #1100 interaction

The current Sauler revision intentionally preserves the upstream #1003 interaction with Artisan's Fighter Overhaul:

- Power Attack remains inherited where upstream grants it;
- Expertise is removed from the Berserker;
- Rapid Shot is removed from the Berserker;
- the Fighter Overhaul's automatic specialization passive is removed from the Berserker.

This behavior is inherited policy, not a new Sauler balance decision, and may be revisited separately in the future.

### HLA policy

Sauler Revised #1003 does not replace the Fighter HLA table, does not remove Hardiness, and does not install Artisan's Extend Rage HLA.

### Compatibility-sensitive files

Any upstream change to these paths requires manual review before synchronization:

- `ArtisansKitpack/lib/Berserker.tpa`
- `ArtisansKitpack/Fighter/Berserker/**`
- `ArtisansKitpack/lib/functions.tph` when changes affect helpers used by #1003
- `ArtisansKitpack/lib/hla_actions.tpa` if HLA helper semantics change
- `ArtisansKitpack/ArtisansKitpack.TP2` if component #1003 wiring/dependencies change

## Adding future revisions

Before modifying another kit:

1. record the current upstream baseline;
2. audit the full component and resource dependency chain;
3. add the component to this registry as **Planned**;
4. isolate downstream implementation where practical;
5. document compatibility-sensitive paths;
6. add/update static QA invariants;
7. complete WeiDU and in-game testing before promoting the state.
