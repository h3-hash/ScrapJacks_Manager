import re

with open("index.html", "r") as f:
    content = f.read()

new_table = """        const SITE_CONDITION_TABLE = {
            1: 'Residual Power Grid - Ignore the AC cost to open one MHU this level (player’s choice).',
            2: 'Active Defense Protocol - The first Hitch roll that results in Hostiles generates +1 hostile model per spawn point.',
            3: 'Abandoned Tool Cache - The first POI in MHU 1 yields +1 Power Cell and +1 Patch Kit in addition to its normal result.',
            4: 'Damaged Subsystems - The Environmental Hazard in MHU 2 costs 2 AC (or Power Cells) to restore instead of the normal amount.',
            5: 'Forgotten Salvage Surplus - All POIs in MHU 2 yield +1D4 Salvage.',
            6: 'Unstable Section - All Hazard results from Hitch rolls in MHU 3 are automatically replaced by Hull Shift.',
            7: 'Emergency Medical Supply - The first POI in MHU 3 yields +1 Med Kit and +1 Patch Kit in addition to its normal result.',
            8: 'Tracked Inventory - Any Quiet Pulls this level yield +1D4 Salvage, but automatically generate a Trace, even on a successful Access action.',
            9: 'Functional Air Recycler - Ignore the first Suit Breach AC loss in one MHU (player’s choice).',
            10: 'Rival Claim - The first Hitch roll that would generate Hostiles instead generates Raiders or Pirates (level appropriate).'
        };"""

content = re.sub(r"\s+const SITE_CONDITION_TABLE = \{[^\}]+\};", "\n" + new_table, content, flags=re.MULTILINE)

with open("index.html", "w") as f:
    f.write(content)
