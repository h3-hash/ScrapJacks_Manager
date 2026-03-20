import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r"(const success = assignGear\(specificGear, charId, true\);.*?if \(success\) \{.*?setCrewLocker\(prev => prev.filter\(g => g.id !== gear.id\)\);.*?\})"

new_code = """const charObj = crew.find(c => c.id === charId);
                                                const hasDeepPockets = charObj && charObj.knack === 'Deep Pocket';

                                                if (hasDeepPockets && category.includes('Utility')) {
                                                    const success1 = assignGear({...specificGear, id: generateId()}, charId, true);
                                                    const success2 = assignGear({...specificGear, id: generateId()}, charId, true);
                                                    if (success1 || success2) {
                                                        setCrewLocker(prev => prev.filter(g => g.id !== gear.id));
                                                    }
                                                } else {
                                                    const success = assignGear(specificGear, charId, true);
                                                    if (success) {
                                                        setCrewLocker(prev => prev.filter(g => g.id !== gear.id));
                                                    }
                                                }"""

content = re.sub(pattern, new_code, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
