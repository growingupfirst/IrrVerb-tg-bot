#! python3
import re, random, pprint, time

IrrVerbsDict = {}

IrrVerbsStory = '''Я кирпичик throw-threw-thrown, (бросать)
Он в окошко fly-flew-flown, (летать)
Меня дядя catch-caught-caught, (ловить)
К папе с мамой bring-brought-brought. (приводить)
До сих пор я удивлен —
Fling-flung-flung откуда он? (выскакивать)
Cling-clung-clung за воротник, (цепляться)
Ох, и вредный же старик!
Я, конечно, say-said-said, (говорить)
Что разбил окно сосед,
Он меня не hear-heard-heard, (слышать)
Как на казнь меня ведет.
Я опасность feel-felt-felt (чувствовать)
И готов был kneel-knelt-knelt… (встать на колени)
Ох, и сильно мне попало —
Cost-cost-cost стекло немало!!! (стоить)
Болван с Прохвостом целый день
Вдвоем играли в «дребедень».
«Я win-won-won». — сказал Болван, (выигрывать)
Ты lose-lost-lost, — сказал Прохвост! (проигрывать)
Забияки fight-fought-fought (драться)
Их никто не разведет
Уже оба weep-wept-wept (плакать, хныкать)
Воспитатель sleep-slept-slept. (спать)
Я в буфете buy-bought-bought (покупать)
Первоклассный бутерброд,
За него я pay-paid-paid, (платить)
В классе в парту lay-laid-laid (класть)
И совсем не think-thought-thought, (думать)
Что сосед его умнет.
А теперь мне очень грустно —
Smell-smelt-smelt он очень вкусно! (пахнуть)
Пол метлою sweep-swept-swept, (подметать)
Дом в порядке keep-kept-kept, (содержать)
Learn-learnt-learnt усердно буду (учиться)
Sew-sewed-sewn и мыть посуду (шить)
Shine-shone-shone все вокруг — (сиять, блестеть)
Будет счастлив мой супруг.
Каждый должен know-knew-known, (знать)
Что когда — то grow-grew-grown. (расти, вырастать)
Так давайте dream-dreamt-dreamt (мечтать)
Выйти замуж без проблем!
Drink-drank-drunk ужасно много (пить)
Наш соседский дядя Гога.
Он forget-forgot-forgotten (забывать)
Про семью и про работу
И, понятно, have-had-had(иметь)
Он ужасно много бед.
Он такое do-did-done, (делать)
Когда был смертельно пьян!!!
По-пластунски creep-crept-crept, (ползать)
Как ребенок weep-wept-wept. (плакать)
Очень многим hurt-hurt-hurt (вредить)
Дядя Гога-обормот.
С управдомом fight-fought-fought (драться)
Угрожал, что shoot-shot-shot. (стрелять)
Своего же друга — Гришку
Strike-struck-struck по носу книжкой. (ударять)
Нос, конечно swell-swelled-swollen — (опухать)
Друг был очень недоволен.
Freeze-froze-frozen в морозилке (замораживать)
Своего кота Мурзилку,
А однажды break-broke-broken (разбивать)
В нашем доме восемь окон.
Объявил в семье войну,
Bind-bound-bound свою жену. (связывать)
Draw-drew-drawn в тетрадке сына (рисовать)
Неприличную картину.
От него жена и дети
Hide-hid-hidden в туалете. (прятаться)
Слух ужасный spread-spread-spread (распространять)
Будто — жулик наш сосед.
Анонимку send-sent-sent, (посылать)
Мол, steal-stole-stolen он цемент. (красть)
Он с балкона взял за моду
Spit-spat-spat на пешеходов. (плевать)
Lean-leant-leant через перила (нагибаться)
И хохочет, как горилла!
Ну, в итоге, fall-fell-fallen (падать)
Прямо с этого балкона.
Write-wrote-written на стене, (писать)
Ride-rode-ridden на слоне, (ездить)
А к тому же, в зоосаде
Be-was-been у львов в ограде. (быть)
Seek-sought-sought чего-то там (искать)
На закуску под сто грамм.
А недавно bite-bit-bitten (кусать)
У подъезда тетю Виту.
Дед и бабка find-found-found (находить)
Пса породы Бассет-Хаунд.
Очень близок старикам
Пес become-became-become. (становиться)
Give-gave-given дед ему (давать)
Дорогую бастурму —
Надо ж псину feed-fed-fed (кормить)
Чем-то вкусным на обед.
Сами сала и котлет
Старики не let-let-let. (позволять)
Раньше бабка sit-sat-sat, (сидеть)
Knit-knit-knit себе жакет, (вязать)
А теперь ей дед велит
Это дело quit-quit-quit; (бросать, прекращать)
Нынче бабушка и дед
Жизнь другую lead-led-led: (вести)
Дед с улыбкой дремлет в ванне,
Бабка dwell-dwelt-dwelt в чулане, (обитать)
Пес в кровати lie-lay-lain, (лежать)
Как эмир страны Бахрейн.
Клад искал один чудак,
Целый месяц dig-dug-dug, (копать)
Find-found-found, устав вконец, (находить)
Металлический ларец!
И, конечно, think-thought-thought, (думать)
Что богато заживет.
Он так страстно strive-strove-striven (стремиться)
Все иметь и thrive-throve-thriven! (процветать)
Take-took-taken он топор (брать)
И сорвал с ларца запор…
Перед тем, как открывать
Go-went-gone домой поспать. (идти)
И всю ночь во сне чудак
Drive-drove-driven «Кадиллак», (водить)
Eat-ate-eaten ананасы (есть)
И копченые колбасы
Fly-flew-flown за облаками, (летать)
Hold-held-held свой клад руками, (держать)
Spend-spent-spent на ветер деньги (тратить)
Build-built-built себе фазенды…(строить)
А когда он wake-woke-woken, (просыпаться)
То ни слова speak-spoke-spoken (говорить)
(ведь минуты сочтены),
Leave-left-left свои штаны, (оставлять, забывать)
Run-ran-run во весь опор, (бежать)
Find-found-found лишь… свой топор! (находить)
Глянь, рогатку Баламут
В свой кармашек put-put-put (положить)
И begin-began-begun (начинать)
Хулиганить хулиган!
Он подушку cut-cut-cut, (резать)
Брата в ванной shut-shut-shut, (закрывать)
Все газеты light-lit-lit, (поджигать)
Собачонку hit-hit-hit, (бить)
Он соседу ring-rang-rung (звонить)
И, конечно, run-ran-run. (бежать)
Он совсем не think-thought-thought, (думать)
Что милиция придет.
Как-то раз в кошмарном сне
Hang-hung-hung я на стене, (висеть)
А в другой раз see-saw-seen, (видеть)
Будто пил я керосин!
Что за чушь мне ночью снится-
То я fly-flew-flown, как птица, (летать)
То я swim-swam-swum в фонтане, (плавать)
Lie-lay-lain одетый в ванне, (лежать)
То учительницу нашу
Teach-taught-taught готовить кашу! (обучать)
То соседку-тетю Глашу
Make-made-made пить простоквашу! (заставлять)
А сегодня be-was-been (быть)
Просто форменный кретин:
Steal-stole-stolen барабан, (красть)
Beat-beat-beaten, как шаман! (колотить)
Не поверите вы мне,
Но однажды я во сне
Speak-spoke-spoken со Сталлоне? (разговаривать)
Sing-sang-sung вдвоем с Мадонной. (петь)
А с актрисой Шерон Стоун
Leap-leapt-leapt, как будто клоун! (скакать)
Tell-told-told об этом маме — (рассказывать)
Мама burst-burst-burst слезами. (разразиться)
Украинскому Премьеру
Sell-sold-sold вагон фанеры! (продавать)
Джуди Фостер — мне она
Weave-wove-woven шарф из льна. (ткать)
Что все это mean-meant-meant, (значить)
Как все это understand-Understood-understood (понимать)
Что за этим stand-stood-stood? (стоять)
Только раз был сон — как сон:
Я get-got-gotten миллион! (получать)'''

ReText = re.compile('[a-zA-z]+-[a-zA-z]+-[a-zA-z]+')
result1 = ReText.findall(IrrVerbsStory)

IrrVerbsStory1 = IrrVerbsStory.split(sep='\n')

for i in result1:
        for n in IrrVerbsStory1:
                if i in n:
                    IrrVerbsDict[i] = n
                    IrrVerbsStory1.remove(n)
                    break


#TODO:A game where you have to write the correct Irregular Verb having a poem
#TODO:Visualization and full poem preview
#TODO:Error handler

def IrrVerbView():      #Irregular Verb of with a corresponding poem line
        randomVerb = random.choice(list(IrrVerbsDict.keys()))
        randomLine = IrrVerbsDict[randomVerb]
        print('Random Irregular Verb for you:\n', randomVerb +'\n\n', randomLine +'\n\n')

#IrrVerbView()
time.sleep(3)
#print('Now I am going to check your knowledge of Irregular Verbs.')
time.sleep(3)

def IrrVerbGame():
        attempts = 5
        score = 0
        print('The game is beginning. Please wait...\n')
        time.sleep(3)
        print('You have {} attempts\n'.format(attempts))
        for z in range(attempts):
                randomDictLine = random.choice(list(IrrVerbsDict.values()))
                print('Attempt number:', z+1)
                time.sleep(3)
                for x in IrrVerbsDict.keys():
                        if x in randomDictLine:
                                time.sleep(1)
                                IrregularVerb = x.lower()
                                resultLine = randomDictLine.replace(x, '()')
                                print('Please write a nessessary verbs with dashes:\n', resultLine)
                                answer = input(str())
                                if answer.lower().lstrip() == IrregularVerb.lower().lstrip():
                                        score = score + 1
                                        print('Good Job! Your score is', score)
                                else:

                                        print('Wrong! The right answer is \n', IrregularVerb)
                                        time.sleep(3)
                                if z+1 == attempts:
                                        print('Your final score is', score)
                                        time.sleep(3)
                                        if score == 5:
                                                print('You are a brilliant student!')
                                        elif score == 4:
                                                print('You are a good student!')
                                        else:
                                                print('You are not a good student.')
                                                time.sleep(1)
                                                print(':(')
                                                time.sleep(1)
                                                print('Try again one more time!')

#IrrVerbGame()




