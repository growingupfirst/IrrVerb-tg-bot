import os, re, random
def prepare_verbdict():

    cur_path = os.path.dirname(__file__)
    new_path = os.path.join(cur_path, '..', 'wordlists', 'IrregularVerbs.txt')

    with open('/usr/src/app/wordlists/IrregularVerbs.txt','r', encoding="utf8") as f: #'C:\\Users\\Growing\\Desktop\\PythonScripts\\TelegramEnglishBot\\wordlists\\IrregularVerbs.txt','r', encoding="utf8") as f:
            IrrVerbsStory = f.read()
            f.close()
    
            IrrVerbsDict = {}
        
            ReText = re.compile('[a-zA-z]+-[a-zA-z]+-[a-zA-z]+')
            result1 = ReText.findall(IrrVerbsStory)
            IrrVerbsStory1 = IrrVerbsStory.split(sep='\n')
            for i in result1:
                for n in IrrVerbsStory1:
                        if i in n:
                            IrrVerbsDict[i] = n
                            IrrVerbsStory1.remove(n)
                            break
    return IrrVerbsDict
            
# Функция которая генерирует строчку и ответ. Возвращает строку и правильный ответ
def get_random_line(VerbDict):
    randomDictLine = random.choice(list(VerbDict.values()))
    for x in VerbDict.keys():
                if x in randomDictLine:
                        IrregularVerb = x.lower()
                        resultLine = randomDictLine.replace(x, '()')
                        _answer = IrregularVerb
    return resultLine, _answer

def check_answer(answer, correct_answer):
    if answer.lower().lstrip() == correct_answer.lower().lstrip():
        return True
    else:
        return False