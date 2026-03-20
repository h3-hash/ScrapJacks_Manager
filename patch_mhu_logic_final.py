import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Add mhuCount to state
state_repl = """            const [missionLevel, setMissionLevel] = useState(1);
            const [mhuCount, setMhuCount] = useState(1);
            const [rolledSiteConditions, setRolledSiteConditions] = useState([]);"""
content = re.sub(
    r"const \[missionLevel, setMissionLevel\] = useState\(1\);\n\s*const \[rolledSiteConditions, setRolledSiteConditions\] = useState\(\[\]\);",
    state_repl,
    content
)

# 2. Add to exportData and handleFileUpload
content = content.replace(
    "turn, phase, playLog, missionLevel, rolledSiteConditions,",
    "turn, phase, playLog, missionLevel, mhuCount, rolledSiteConditions,"
)

load_repl = """                        if(data.missionLevel !== undefined) setMissionLevel(data.missionLevel);
                        if(data.mhuCount !== undefined) setMhuCount(data.mhuCount);"""
content = content.replace(
    "if(data.missionLevel !== undefined) setMissionLevel(data.missionLevel);",
    load_repl
)

# 3. Add to saveHistory and undo
history_repl = """                    playLog: [...playLog],
                    missionLevel,
                    mhuCount,
                    rolledSiteConditions: [...rolledSiteConditions],"""
content = content.replace(
    """                    playLog: [...playLog],
                    rolledSiteConditions: [...rolledSiteConditions],""",
    history_repl
)

undo_repl = """                setPlayLog([`[Turn ${turnHistory.turn} - ${turnHistory.phase}] Undo: Reverted last action.`, ...turnHistory.playLog]);
                if(turnHistory.missionLevel !== undefined) setMissionLevel(turnHistory.missionLevel);
                if(turnHistory.mhuCount !== undefined) setMhuCount(turnHistory.mhuCount);"""
content = content.replace(
    "setPlayLog([`[Turn ${turnHistory.turn} - ${turnHistory.phase}] Undo: Reverted last action.`, ...turnHistory.playLog]);",
    undo_repl
)

# 4. Apply mhuCount when mission level is changed and when breaching
level_select_repl = """<select value={missionLevel} onChange={e => { setMissionLevel(parseInt(e.target.value)); setMhuCount(1); }} className="w-2/3 bg-slate-800 border border-slate-600 rounded text-white text-xs p-1 focus:outline-none">"""
content = re.sub(
    r"<select value=\{missionLevel\} onChange=\{e => setMissionLevel\(parseInt\(e\.target\.value\)\)\} className=\"w-2/3 bg-slate-800 border border-slate-600 rounded text-white text-xs p-1 focus:outline-none\">",
    level_select_repl,
    content
)

breach_repl = """            const breachNextMHU = () => {
                saveHistory();

                const totalBreaches = crew.reduce((sum, c) => sum + c.suitBreaches, 0);
                const airDrain = 1 + totalBreaches;

                setAircharge(prev => Math.max(0, prev - airDrain));
                setTurn(prev => prev + 1);
                setMhuCount(prev => prev + 1);
                setPressureBuilding(false);"""
content = re.sub(
    r"            const breachNextMHU = \(\) => \{\n\s*saveHistory\(\);\n\n\s*const totalBreaches = crew\.reduce\(\(sum, c\) => sum \+ c\.suitBreaches, 0\);\n\s*const airDrain = 1 \+ totalBreaches;\n\s*\n\s*setAircharge\(prev => Math\.max\(0, prev - airDrain\)\);\n\s*setTurn\(prev => prev \+ 1\);\n\s*setPressureBuilding\(false\);",
    breach_repl,
    content
)

# Reset in new mission
content = content.replace("setMissionLevel(1);", "setMissionLevel(1);\n                setMhuCount(1);")

# Fix processHitchEvent Condition 6
content = content.replace(
    "if (siteCondition === 6 && missionLevel === 3) {",
    "if (siteCondition === 6 && mhuCount === 3) {"
)

# Fix resolveObjectiveOrPOI
poi_logic_old = """                    // Site Conditions POI Intercepts
                    const siteCondition = siteConditions[missionLevel];
                    const flags = siteFlags[missionLevel] || {};
                    const isFirstPOI = !flags.poiResolved;

                    if (isFirstPOI) {
                        setSiteFlags(prev => ({
                            ...prev,
                            [missionLevel]: { ...prev[missionLevel], poiResolved: true }
                        }));

                        if (siteCondition === 3 && missionLevel === 1) {
                            gear.push('Power Cell', 'Patch-Kit');
                            special += " [Abandoned Tool Cache: +1 Power Cell, +1 Patch Kit]";
                        }
                        if (siteCondition === 7 && missionLevel === 3) {
                            gear.push('Med-Kit', 'Patch-Kit');
                            special += " [Emergency Medical Supply: +1 Med-Kit, +1 Patch-Kit]";
                        }
                    }

                    if (siteCondition === 5 && missionLevel === 2) {
                        const extraSalvage = rollDice(1, 4);
                        sAdd += extraSalvage;
                        special += ` [Forgotten Salvage Surplus: +${extraSalvage} Salvage]`;
                    }"""

poi_logic_new = """                    // Site Conditions POI Intercepts
                    if (!isObj) {
                        const siteCondition = siteConditions[missionLevel];
                        const flags = siteFlags[missionLevel] || {};
                        const mhuPoiFlags = flags.mhuPOIs || {};
                        const isFirstPOIForThisMHU = !mhuPoiFlags[mhuCount];

                        if (isFirstPOIForThisMHU) {
                            setSiteFlags(prev => ({
                                ...prev,
                                [missionLevel]: {
                                    ...prev[missionLevel],
                                    mhuPOIs: { ...(prev[missionLevel]?.mhuPOIs || {}), [mhuCount]: true }
                                }
                            }));

                            if (siteCondition === 3 && mhuCount === 1) {
                                gear.push('Power Cell', 'Patch-Kit');
                                special += " [Abandoned Tool Cache: +1 Power Cell, +1 Patch Kit]";
                            }
                            if (siteCondition === 7 && mhuCount === 3) {
                                gear.push('Med-Kit', 'Patch-Kit');
                                special += " [Emergency Medical Supply: +1 Med-Kit, +1 Patch-Kit]";
                            }
                        }

                        if (siteCondition === 5 && mhuCount === 2) {
                            const extraSalvage = rollDice(1, 4);
                            sAdd += extraSalvage;
                            special += ` [Forgotten Salvage Surplus: +${extraSalvage} Salvage]`;
                        }
                    }"""
content = content.replace(poi_logic_old, poi_logic_new)

# Initialize mhuPOIs in siteFlags
init_flags = """                setSiteFlags(prev => ({...prev, [missionLevel]: { hostileSpawned: false, mhuPOIs: {} }}));"""
content = content.replace(
    "setSiteFlags(prev => ({...prev, [missionLevel]: { hostileSpawned: false, poiResolved: false }}));",
    init_flags
)

# Update Hazard text UI for Condition 4
hazard_ui_old = """                                                                {siteConditions[missionLevel] === 4 && missionLevel === 2 && (
                                                                    <div className="text-amber-500 font-bold mt-1">Damaged Subsystems: Costs 2 AC (or Power Cells) to clear.</div>
                                                                )}"""
hazard_ui_new = """                                                                {siteConditions[missionLevel] === 4 && mhuCount === 2 && (
                                                                    <div className="text-amber-500 font-bold mt-1">Damaged Subsystems: Costs 2 AC (or Power Cells) to clear.</div>
                                                                )}"""
content = content.replace(hazard_ui_old, hazard_ui_new)

# UI Level update
mhu_ui = """                                                <div className="flex gap-2 items-center mb-2 border-b border-slate-700 pb-2">
                                                    <span className="text-[10px] text-slate-400 font-bold uppercase w-1/3">Mission Level</span>
                                                    <select value={missionLevel} onChange={e => { setMissionLevel(parseInt(e.target.value)); setMhuCount(1); }} className="w-2/3 bg-slate-800 border border-slate-600 rounded text-white text-xs p-1 focus:outline-none">
                                                        <option value={1}>Level 1</option>
                                                        <option value={2}>Level 2</option>
                                                        <option value={3}>Level 3</option>
                                                    </select>
                                                </div>"""

mhu_ui_new = """                                                <div className="flex gap-2 items-center mb-2 border-b border-slate-700 pb-2">
                                                    <div className="flex flex-col w-1/3">
                                                        <span className="text-[10px] text-slate-400 font-bold uppercase">Level</span>
                                                        <span className="text-[9px] text-indigo-400 font-bold">MHU #{mhuCount}</span>
                                                    </div>
                                                    <select value={missionLevel} onChange={e => { setMissionLevel(parseInt(e.target.value)); setMhuCount(1); }} className="w-2/3 bg-slate-800 border border-slate-600 rounded text-white text-xs p-1 focus:outline-none">
                                                        <option value={1}>Level 1</option>
                                                        <option value={2}>Level 2</option>
                                                        <option value={3}>Level 3</option>
                                                    </select>
                                                </div>"""
content = content.replace(mhu_ui, mhu_ui_new)

with open("index.html", "w") as f:
    f.write(content)
