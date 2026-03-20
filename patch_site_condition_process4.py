import re

with open("index.html", "r") as f:
    content = f.read()

intercept_hostile = """
                const siteCondition = siteConditions[missionLevel];

                // 6. Unstable Section: All Hazard results from Hitch rolls in MHU 3 are replaced by Hull Shift.
                if (siteCondition === 6 && missionLevel === 3) {
                    const isHazard = (lvl === 3 && [1, 2, 3, 8].includes(rollVal));
                    if (isHazard) {
                        text = "Unstable Section (Site Condition) converts Hazard to Hull Shift! All Scrapjacks roll DD. Fail: suffer 1 Wound.";
                        addHazard('Hull Shift');
                        return text;
                    }
                }

                if (lvl === 1) {"""

content = re.sub(
    r"if \(lvl === 1\) \{",
    intercept_hostile,
    content
)

with open("index.html", "w") as f:
    f.write(content)
