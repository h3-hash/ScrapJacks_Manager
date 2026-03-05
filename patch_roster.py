import re

with open('index.html', 'r') as f:
    text = f.read()

# I need to format the character name as LAST NAME, FIRST NAME + record number.
# In the `printLayout === 'roster'` block:

old_roster_name = """                                                    <div className="print-row">
                                                        <div className="print-col"><strong>NAME/CALL SIGN:</strong> <span style={{borderBottom: '1px solid black', width:'100%', display:'inline-block'}}>{char.name || '\u00A0'}</span></div>
                                                    </div>"""

new_roster_name = """                                                    <div className="print-row">
                                                        <div className="print-col">
                                                            <strong>NAME/RECORD NO.:</strong>
                                                            <span style={{borderBottom: '1px solid black', width:'100%', display:'inline-block', fontWeight: 'bold', fontSize: '14px', paddingTop: '2px'}}>
                                                                {(() => {
                                                                    const parts = (char.name || 'UNKNOWN').split(' ');
                                                                    const lastName = parts.length > 1 ? parts.pop().toUpperCase() : parts[0].toUpperCase();
                                                                    const firstName = parts.length > 0 ? parts.join(' ').toUpperCase() : '';
                                                                    const recordNo = char.id ? char.id.substring(0, 6).toUpperCase() : '000000';
                                                                    return `${lastName}, ${firstName} [#SJ-${recordNo}]`;
                                                                })()}
                                                            </span>
                                                        </div>
                                                    </div>"""
text = text.replace(old_roster_name, new_roster_name)

with open('index.html', 'w') as f:
    f.write(text)
