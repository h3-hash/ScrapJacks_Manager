import re

with open('index.html', 'r') as f:
    content = f.read()

# I will add a state `const [rolledSiteConditions, setRolledSiteConditions] = useState([]);`
# Inside applyNewMission and applyNewCrew, reset it to `[]`.
# Inside loadData, load it if available.
# In `advancePhase`:
# if (phase === 'Breach') {
#    if (!rolledSiteConditions.includes(missionLevel)) {
#        rollSiteCondition(manualRolls.site);
#        setRolledSiteConditions(prev => [...prev, missionLevel]);
#    }
#    ...

content = content.replace(
    'const [missionLevel, setMissionLevel] = useState(1);',
    'const [missionLevel, setMissionLevel] = useState(1);\n            const [rolledSiteConditions, setRolledSiteConditions] = useState([]);'
)

content = content.replace(
    'missionLevel, activeObjectives',
    'missionLevel, rolledSiteConditions, activeObjectives'
)

content = content.replace(
    'if(data.missionLevel !== undefined) setMissionLevel(data.missionLevel);',
    'if(data.missionLevel !== undefined) setMissionLevel(data.missionLevel);\n                        if(data.rolledSiteConditions !== undefined) setRolledSiteConditions(data.rolledSiteConditions);'
)

content = content.replace(
    'setMissionLevel(1);\n                setAircharge(SHIPS[shipClass].aircharge);',
    'setMissionLevel(1);\n                setRolledSiteConditions([]);\n                setAircharge(SHIPS[shipClass].aircharge);'
)

content = content.replace(
    'setMissionLevel(1);\n                setAcrDebt(SHIPS[\'Class C - Tug\'].acr);',
    'setMissionLevel(1);\n                setRolledSiteConditions([]);\n                setAcrDebt(SHIPS[\'Class C - Tug\'].acr);'
)

content = content.replace(
    'if (turn === 1) rollSiteCondition(manualRolls.site);',
    'if (!rolledSiteConditions.includes(missionLevel)) {\n                        rollSiteCondition(manualRolls.site);\n                        setRolledSiteConditions(prev => [...prev, missionLevel]);\n                    }'
)

with open('index.html', 'w') as f:
    f.write(content)
