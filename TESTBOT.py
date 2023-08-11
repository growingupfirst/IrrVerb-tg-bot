import telepot
import telepot.helper
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)
import re, random, time

class QuizStarter(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(QuizStarter, self).__init__(*args, **kwargs)
        self._answer = None
        self._score = 0
        self._attempts = 0
        self._resultLine = None


    def open(self, initial_message, seed):
        self._answer, self._resultLine = self.compute()    
        return True
    def on_chat_message(self, msg):
        
        
        print(self._answer, self._resultLine)
        content_type, chat_type, chat_id = telepot.glance(msg)
        #отредактировать обработку ответов
        if msg['text'] == self._answer:
            self._attempts +=1
            self.sender.sendMessage('Correct')
            self._score +=1
            self.sender.sendMessage(f'Your score {self._score}')
            self._answer, self._resultLine = self.compute()
        else:
            self._attempts +=1
            self.sender.sendMessage(f'Try again!\nThe correct answer is {self._answer}')
            self._answer, self._resultLine = self.compute()
        return
    def on__idle(self, event):
        text = f'Final score: {self._score}\nNumber of attempts:{self._attempts}'
        self.sender.sendMessage(text)
        self.close()
    
    def compute(self):
            with open('IrregularVerbs.txt','r', encoding="utf8") as f:
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
            randomDictLine = random.choice(list(IrrVerbsDict.values()))
            for x in IrrVerbsDict.keys():
                    if x in randomDictLine:
                        time.sleep(1)
                        #поменять обработку ответов
                        answer = x.lower()
                        resultLine = randomDictLine.replace(x, '()')
                        self.sender.sendMessage('Guess the Irregular Verb')
                        self.sender.sendMessage(text=f'Please write a nessessary verbs with dashes: {resultLine}\n')
                        return answer, resultLine
                        

TOKEN = 'your_token'
bot = telepot.DelegatorBot(TOKEN,
                           [pave_event_space()(per_chat_id(), create_open, QuizStarter, timeout=60),
                            ])

MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)