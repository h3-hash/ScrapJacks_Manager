import re
with open('index.html', 'r') as f:
    text = f.read()

# Make sure ACTION_TYPES is in the code.
if "const ACTION_TYPES" not in text:
    action_types = """
        const ACTION_TYPES = {
            'Aim': { type: 'Any', desc: '+2 to next Combat action, -2 to enemy DD.' },
            'Assist': { type: 'Any', desc: 'Grants ally TDB or +2 to their next action.' },
            'Interact/Use': { type: 'Any', desc: 'Use items, open doors, minor interactions.' },
            'Move': { type: 'Load', desc: 'Additional movement after Free Move.' },
            'Melee Combat': { type: 'Load', desc: 'Close-quarters fighting.' },
            'Break/Brace': { type: 'Load', desc: 'Forceful dismantling or stabilizing.' },
            'Ranged Combat': { type: 'Focus', desc: 'Attacking with firearms.' },
            'Repair/Heal': { type: 'Focus', desc: 'Treat injuries, patch suits.' },
            'Scan/Hack': { type: 'Focus', desc: 'Technical interaction with systems.' },
            'Resist': { type: 'Grit', desc: 'Reaction. Die spent only on failure.' },
            'Resist Stress': { type: 'Grit', desc: 'Save vs Terror or Redlined.' },
            'Push': { type: 'Grit', desc: 'Costs 1 Aircharge. Success = refresh dice & move.' }
        };
"""
    text = text.replace("const WEAPONS_MELEE", action_types + "\n        const WEAPONS_MELEE")


# Now add the modal UI for actionRollPrompt
modal_ui = """
                    {actionRollPrompt && (() => {
                        const char = crew.find(c => c.id === actionRollPrompt.charId);
                        const vital = actionRollPrompt.vital;

                        // Filter actions based on the selected die
                        const availableActions = Object.entries(ACTION_TYPES).filter(([name, data]) => {
                            return data.type === 'Any' || data.type.toLowerCase() === vital;
                        });

                        return (
                            <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50 no-print">
                                <div className="bg-slate-800 border border-slate-600 p-6 rounded-lg shadow-xl max-w-sm w-full">
                                    <h3 className="text-xl font-bold text-white mb-2">Select Action</h3>
                                    <p className="text-slate-300 mb-4 text-sm">
                                        {char.name} is spending their <span className="font-bold uppercase text-amber-500">{vital}</span> die. What action are they taking?
                                    </p>

                                    <div className="flex flex-col gap-2 max-h-64 overflow-y-auto mb-4 pr-1 custom-scrollbar">
                                        {availableActions.map(([name, data]) => {
                                            // Check if this action triggers TDB for this character
                                            const roleTdbText = ROLES[char.role]?.tdb || '';
                                            const isTdb = roleTdbText.includes(name);

                                            return (
                                                <button
                                                    key={name}
                                                    onClick={() => confirmActionRoll(char.id, vital, name)}
                                                    className="text-left px-4 py-3 bg-slate-900 hover:bg-slate-700 border border-slate-700 rounded transition-colors group relative"
                                                >
                                                    <div className="flex justify-between items-center mb-1">
                                                        <span className="font-bold text-sm text-white">{name}</span>
                                                        {isTdb && <span className="text-[9px] px-1.5 py-0.5 bg-amber-600 text-white rounded font-bold uppercase shadow-[0_0_8px_rgba(217,119,6,0.5)] border border-amber-400">Two Dice Bonus</span>}
                                                    </div>
                                                    <span className="text-[10px] text-slate-400 block leading-tight">{data.desc}</span>
                                                </button>
                                            );
                                        })}
                                    </div>

                                    <button onClick={() => setActionRollPrompt(null)} className="w-full px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded text-white text-sm font-bold shadow">Cancel</button>
                                </div>
                            </div>
                        );
                    })()}
"""

text = text.replace("{redlinePrompt &&", modal_ui + "\n                    {redlinePrompt &&")

with open('index.html', 'w') as f:
    f.write(text)
