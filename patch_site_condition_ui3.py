import re

with open("index.html", "r") as f:
    content = f.read()

# Add UI for active site condition right after the "Active Job" block
ui_block = """                                    {activeContract && (
                                        <div className="mb-4 bg-slate-900 border border-amber-900/50 rounded p-3 flex flex-col md:flex-row md:items-center justify-between gap-2 shadow-inner">
                                            <div className="flex items-center gap-2">
                                                <span className="text-[10px] bg-amber-600 text-white px-2 py-1 rounded font-bold uppercase tracking-wider">Active Job</span>
                                                <span className="text-sm text-white font-bold">{activeContract.target}</span>
                                            </div>
                                            <div className="flex gap-4 text-xs text-slate-400">
                                                <span><strong className="text-slate-300">Type:</strong> {activeContract.type}</span>
                                                <span><strong className="text-slate-300">Size:</strong> {activeContract.size}</span>
                                            </div>
                                            {activeContract.complications && activeContract.complications !== 'None' && (
                                                <div className="text-xs text-amber-500 font-bold max-w-xs text-right hidden md:block italic">
                                                    {activeContract.complications}
                                                </div>
                                            )}
                                        </div>
                                    )}

                                    {siteConditions[missionLevel] && (
                                        <div className="mb-4 bg-indigo-950/30 border border-indigo-900/50 rounded p-3 flex flex-col shadow-inner">
                                            <div className="flex items-center gap-2 mb-1">
                                                <span className="text-[10px] bg-indigo-700 text-white px-2 py-0.5 rounded font-bold uppercase tracking-wider">Lvl {missionLevel} Site Condition</span>
                                            </div>
                                            <div className="text-xs text-indigo-200">
                                                <strong className="text-indigo-400">{SITE_CONDITION_TABLE[siteConditions[missionLevel]].split(' - ')[0]}:</strong>
                                                {' ' + SITE_CONDITION_TABLE[siteConditions[missionLevel]].split(' - ').slice(1).join(' - ')}
                                            </div>
                                        </div>
                                    )}"""

content = content.replace(
    """                                    {activeContract && (
                                        <div className="mb-4 bg-slate-900 border border-amber-900/50 rounded p-3 flex flex-col md:flex-row md:items-center justify-between gap-2 shadow-inner">
                                            <div className="flex items-center gap-2">
                                                <span className="text-[10px] bg-amber-600 text-white px-2 py-1 rounded font-bold uppercase tracking-wider">Active Job</span>
                                                <span className="text-sm text-white font-bold">{activeContract.target}</span>
                                            </div>
                                            <div className="flex gap-4 text-xs text-slate-400">
                                                <span><strong className="text-slate-300">Type:</strong> {activeContract.type}</span>
                                                <span><strong className="text-slate-300">Size:</strong> {activeContract.size}</span>
                                            </div>
                                            {activeContract.complications && activeContract.complications !== 'None' && (
                                                <div className="text-xs text-amber-500 font-bold max-w-xs text-right hidden md:block italic">
                                                    {activeContract.complications}
                                                </div>
                                            )}
                                        </div>
                                    )}""",
    ui_block
)

with open("index.html", "w") as f:
    f.write(content)
