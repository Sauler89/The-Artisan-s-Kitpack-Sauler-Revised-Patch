# Live Patch Area

This directory is reserved for **temporary development/test patches** that may be useful on an already-modded installation while a Sauler Revised component is being validated.

Rules:

- live patches are not the canonical implementation;
- permanent fixes belong in the normal Artisan/Sauler component source;
- every live patch must document the exact component/version/install state it expects;
- live patches must not be included in a stable release unless they have been promoted into the main installer architecture;
- save-migration or retrofit patches should be clearly separated from clean-install code.

There is currently no supported live patch for Berserker #1003. The integrated component should be tested on a clean/reproducible mod installation first.
