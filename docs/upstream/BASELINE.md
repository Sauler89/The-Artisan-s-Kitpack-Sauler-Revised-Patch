# Upstream Baseline

## Current baseline

- **Upstream repository:** `TheArtisanBG/The-Artisan-s-Kitpack`
- **Upstream branch:** `master`
- **Baseline commit:** `85928f964f6965fd37980bf679d7eeb9af410256`
- **Baseline commit message:** `Update c0ber#00.spl`
- **Baseline commit date:** 2026-05-31

This was the current upstream `master` when the first Sauler Revised component integration began.

## Verification performed before divergence

Before integrating the Sauler Revised Berserker, the following fork resources were verified to match the upstream baseline exactly:

- `ArtisansKitpack/lib/Berserker.tpa`
  - blob SHA: `1fceb421563935634d7a0fa2b4a5d2bcc43cc154`
- `ArtisansKitpack/Fighter/Berserker/2da`
  - tree SHA: `8a19e37b0ca4116f71a598e63323260de6378087`
- `ArtisansKitpack/Fighter/Berserker/bams`
  - tree SHA: `a26e70bd3cb9de31b04acf1bd7ae7ebb20bd5ec2`
- `ArtisansKitpack/Fighter/Berserker/spells`
  - tree SHA: `e1ef7cd6312750f5b9189e2017b0cabcf519ff85`

Therefore component #1003 began from the current Artisan implementation rather than from an older or already-modified fork state.

## Synchronization policy

This project is a downstream revision, not an independent replacement codebase.

When upstream changes:

1. fetch the current upstream `master`;
2. compare changes from the last common/baseline point;
3. automatically regard untouched components as low-risk candidates for synchronization;
4. manually review every change overlapping a Sauler Revised component or a shared helper it depends on;
5. import relevant upstream bug fixes into the downstream implementation where appropriate;
6. update this file only after the synchronization has been reviewed and completed;
7. record the synchronization in `CHANGELOG.md`.

## Current high-review paths

### Directly Sauler-owned

- `ArtisansKitpack/lib/Berserker.tpa`
- `ArtisansKitpack/lib/Berserker_Sauler_Revised.tpa`

### Upstream resources used by the revised Berserker

- `ArtisansKitpack/Fighter/Berserker/bams/C0BER#IC.BAM`

### Shared upstream infrastructure used by #1003

- `ArtisansKitpack/lib/functions.tph`
- `ArtisansKitpack/ArtisansKitpack.TP2`

### Upstream Berserker tree retained for parity/reference

- `ArtisansKitpack/Fighter/Berserker/**`

A change in the retained tree does not necessarily need to be copied into the runtime Sauler implementation, but it must be reviewed for bug fixes, assets, descriptions, or architectural changes that remain relevant.

## Future revised components

When Red Wizard or another component becomes Sauler Revised, add its direct and shared paths here before changing the implementation.
