import re

with open('index.html', 'r') as f:
    text = f.read()

# I need to add a quick reference card at the end of the roster printout.
quick_ref_card = """
                                    <div className="print-card" style={{marginTop: '24px', pageBreakBefore: 'always'}}>
                                        <div className="print-header">
                                            <span>OPERATIONAL QUICK REFERENCE</span>
                                            <span>FORM VRG-SJ-QR-01</span>
                                        </div>

                                        <div style={{display: 'flex', gap: '12px'}}>
                                            <div style={{flex: 1}}>
                                                <div className="print-section">
                                                    <div className="print-section-title">TURN STRUCTURE</div>
                                                    <ol style={{fontSize: '9px', paddingLeft: '12px', margin: 0}}>
                                                        <li><strong>Breach (Start of MHU):</strong> Roll Entry Hazard. Set MHU baseline.</li>
                                                        <li><strong>Sweep (Player Turn):</strong> Scrapjacks activate. Move + Action Dice (Load, Focus, Grit). Spend dice to succeed on 4+.</li>
                                                        <li><strong>Hitch (Enemy/Environment):</strong> Unused Action Dice become Reserve. Roll D10 for Hitch. Enemies activate. </li>
                                                        <li><strong>Call (Decision Phase):</strong> Choose to extract (End Job) or reset Phase to Breach next MHU.</li>
                                                    </ol>
                                                </div>
                                                <div className="print-section">
                                                    <div className="print-section-title">CRITICAL ROLLS (TDB ONLY)</div>
                                                    <div className="rules-text">
                                                        <strong>Crit-Success:</strong> Roll doubles (e.g. 5,5) and succeed (4+). The action succeeds and the die is NOT expended.<br/>
                                                        <strong>Crit-Fumble:</strong> Roll doubles and fail (<4). Activation ends immediately (lose remaining dice). -1 Aircharge.
                                                    </div>
                                                </div>
                                                <div className="print-section">
                                                    <div className="print-section-title">GRIT REACTIONS</div>
                                                    <div className="rules-text">
                                                        <strong>Resist:</strong> Reaction roll against specific hazards. Grit die is only spent on failure.<br/>
                                                        <strong>Resist Stress:</strong> Roll vs Terror (Prime hostiles) or Redline (fatal wounds).
                                                    </div>
                                                </div>
                                            </div>
                                            <div style={{flex: 1}}>
                                                <div className="print-section">
                                                    <div className="print-section-title">ACTIONS BY DIE TYPE (Target 4+)</div>
                                                    <div className="rules-text" style={{display: 'grid', gridTemplateColumns: 'auto 1fr', gap: '2px 8px'}}>
                                                        <strong>Any Die:</strong><span>Aim (+2 Atk, -2 Enemy DD), Assist (Grants TDB or +2), Interact/Use</span>
                                                        <strong>Load:</strong><span>Move (beyond Free Move), Melee Combat, Break/Brace</span>
                                                        <strong>Focus:</strong><span>Ranged Combat, Repair/Heal, Scan/Hack</span>
                                                        <strong>Grit:</strong><span>Push (Costs 1 AC regardless. On success: regain free move & full dice pool)</span>
                                                    </div>
                                                </div>
                                                <div className="print-section">
                                                    <div className="print-section-title">RESERVE DICE</div>
                                                    <div className="rules-text">
                                                        Unspent dice (Load, Focus, Grit) become Reserve Dice during the Hitch Phase. Can be used as Reactions (e.g. Overwatch) if the situation applies to the specific die type.
                                                    </div>
                                                </div>
                                                <div className="print-section">
                                                    <div className="print-section-title">COMBAT RESOLUTION</div>
                                                    <div className="rules-text">
                                                        <strong>Target Number:</strong> 4+. (Base Attack + Weapon/Mod Modifiers).<br/>
                                                        <strong>Enemy DD (Dodge/Defend):</strong> D10. Must equal or exceed the Scrapjack's final Attack Total to block.<br/>
                                                        <strong>Damage:</strong> Most weapons inflict 1 Wound. Some cause Suit Breaches. 4 Wounds = Redlined.
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
"""

text = text.replace("</>\n                            )}", quick_ref_card + "                                </>\n                            )}")

with open('index.html', 'w') as f:
    f.write(text)
