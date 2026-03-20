import re

with open("index.html", "r") as f:
    content = f.read()

# 1. State changes
state_changes = """            const [rolledSiteConditions, setRolledSiteConditions] = useState([]);
            const [siteConditions, setSiteConditions] = useState({});
            const [siteFlags, setSiteFlags] = useState({});"""

content = re.sub(
    r"const \[rolledSiteConditions, setRolledSiteConditions\] = useState\(\[\]\);",
    state_changes,
    content
)

# Add them to exportData
content = content.replace(
    "rolledSiteConditions, activeObjectives",
    "rolledSiteConditions, siteConditions, siteFlags, activeObjectives"
)

# Add them to handleFileUpload
load_changes = """                        if(data.rolledSiteConditions !== undefined) setRolledSiteConditions(data.rolledSiteConditions);
                        if(data.siteConditions !== undefined) setSiteConditions(data.siteConditions);
                        if(data.siteFlags !== undefined) setSiteFlags(data.siteFlags);"""
content = content.replace(
    "if(data.rolledSiteConditions !== undefined) setRolledSiteConditions(data.rolledSiteConditions);",
    load_changes
)

# Add them to saveHistory
history_changes = """                    rolledSiteConditions: [...rolledSiteConditions],
                    siteConditions: {...siteConditions},
                    siteFlags: JSON.parse(JSON.stringify(siteFlags)),"""
content = content.replace(
    "rolledSiteConditions: [...rolledSiteConditions],",
    history_changes
)

# Add them to turnHistory restore (if any)
restore_changes = """                if(turnHistory.rolledSiteConditions) setRolledSiteConditions([...turnHistory.rolledSiteConditions]);
                if(turnHistory.siteConditions) setSiteConditions({...turnHistory.siteConditions});
                if(turnHistory.siteFlags) setSiteFlags(JSON.parse(JSON.stringify(turnHistory.siteFlags)));"""
content = content.replace(
    "if(turnHistory.rolledSiteConditions) setRolledSiteConditions([...turnHistory.rolledSiteConditions]);",
    restore_changes
)

# Update rollSiteCondition
roll_site = """            const rollSiteCondition = (manualRollStr) => {
                const roll = getRoll(manualRollStr, 1, 10);
                const condition = SITE_CONDITION_TABLE[roll];

                setSiteConditions(prev => ({...prev, [missionLevel]: roll}));
                setSiteFlags(prev => ({...prev, [missionLevel]: { hostileSpawned: false, poiResolved: false }}));

                addLog(`Site Condition (Level ${missionLevel}) [${manualRollStr ? 'Manual Roll' : 'Roll'}: ${roll}]: ${condition}`);
            };"""
content = re.sub(
    r"const rollSiteCondition = \(manualRollStr\) => \{[^\}]+\};",
    roll_site,
    content
)

with open("index.html", "w") as f:
    f.write(content)
