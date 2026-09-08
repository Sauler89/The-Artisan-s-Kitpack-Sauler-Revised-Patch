# Red Wizard — Sauler Revised Design

## Status

**Planned.** No Red Wizard implementation changes should be made until the current Artisan component, resources, and compatibility dependencies have been audited against the user's intended redesign.

## Integration rule

The Red Wizard will follow the same downstream policy established for Berserker #1003:

1. identify the exact Artisan component number and complete dependency/resource chain;
2. record the current upstream file hashes before divergence;
3. preserve upstream files and behavior that the Sauler design does not intentionally change;
4. isolate the downstream implementation where practical;
5. document every intentional mechanical difference;
6. add compatibility notes for the user's target mod stack;
7. add static regression checks;
8. require WeiDU and in-game validation before beta.

## Design source

The detailed Sauler Red Wizard mechanics will be imported from the existing Red Wizard revision work only after that work is re-audited against the exact current Artisan upstream baseline.

This placeholder exists so the project structure already distinguishes **planned downstream ownership** from ordinary untouched upstream components.
