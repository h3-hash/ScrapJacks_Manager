import re

with open("index.html", "r") as f:
    content = f.read()

# Implement Condition 4 note in hazard text
# Damaged Subsystems - The Environmental Hazard in MHU 2 costs 2 AC (or Power Cells) to restore instead of the normal amount.
hazard_logic = """                                                return (
                                                    <div key={hazard.id} className="bg-slate-900 border border-amber-900 rounded p-3 relative flex flex-col justify-between">
                                                        <div>
                                                            <div className="flex justify-between items-start mb-2">
                                                                <div className="font-bold text-amber-400 flex items-center gap-2">
                                                                    <IconAlert /> {hazard.type}
                                                                </div>
                                                            </div>
                                                            <div className="text-[10px] text-slate-300 italic min-h-[30px] mb-3">
                                                                {hData.rules}
                                                                {siteConditions[missionLevel] === 4 && missionLevel === 2 && (
                                                                    <div className="text-amber-500 font-bold mt-1">Damaged Subsystems: Costs 2 AC (or Power Cells) to clear.</div>
                                                                )}
                                                            </div>
                                                        </div>"""

content = re.sub(
    r"return \(\s*<div key=\{hazard.id\} className=\"bg-slate-900 border border-amber-900 rounded p-3 relative flex flex-col justify-between\">\s*<div>\s*<div className=\"flex justify-between items-start mb-2\">\s*<div className=\"font-bold text-amber-400 flex items-center gap-2\">\s*<IconAlert /> \{hazard.type\}\s*</div>\s*</div>\s*<div className=\"text-\[10px\] text-slate-300 italic min-h-\[30px\] mb-3\">\s*\{hData.rules\}\s*</div>\s*</div>",
    hazard_logic,
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)
