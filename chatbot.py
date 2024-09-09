from neuralintents import GenericAssistant
import operator
import wikipedia
import json
import random
import wolframalpha
import os

chatbot = GenericAssistant("intents.json")
chatbot.train_model()
chatbot.save_model()

REPLICATE_API_TOKEN = 'YOUR_API_KEY'

def reply(msg, nm, gali):
    print("reply ke andar hai")
    msg = msg.lower()
    if msg:
        if gali:
            with open("manners.json", 'r') as a:
                precontent = json.load(a)
            precontent[nm] = precontent.get(nm, 0) + 1
            with open("manners.json", 'w') as b:
                json.dump(precontent, b, indent=2)
            return f"@{nm} Ill Mannered Chats+1"

        mylist = ["jeetu", "Jeetu", "jeetendra", "kota factory"]
        for i in mylist:
            if i in msg:
                if "give me question" in msg:
                    try:
                        subject = msg.split("of")[1].strip().lower()
                        with open("questions.json", 'r') as questionread:
                            questions = json.load(questionread)
                        questionsrequired = list(questions[subject])
                        mainreq = [list(i.keys())[0] for i in questionsrequired]
                        return random.choice(mainreq) if mainreq else "no question till now!"
                    except Exception as e:
                        return str(e)

                elif "solve" in msg:
                    try:
                        query = msg.split("solve")[1].lower().strip()
                        client = wolframalpha.Client('Your API Key')
                        res = client.query(query)
                        data = res["pod"]
                        mainData = [i['subpod']['plaintext'] if i['subpod']['plaintext'] else i['subpod']['img']['@src'] for i in data if 'subpod' in i]
                        return mainData
                    except Exception as e:
                        return str(e)

                elif "image of" in msg:
                    try:
                        os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
                        cont = msg.split("image of")[1].lower().strip()
                        model = replicate.models.get("stability-ai/stable-diffusion")
                        version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
                        a = version.predict(prompt=cont)
                        return a[0]
                    except Exception as e:
                        return f"ERROR AA GYA {e}"

                elif "relation of" in msg:
                    import string
                    alphabet = list(string.ascii_lowercase)
                    alpdct = {alphabet[i]: i + 1 for i in range(len(alphabet))}

                    def sumGiver(name):
                        nmlist = list(name.replace(" ", ""))
                        return sum([alpdct[nmlist[i]] for i in range(len(nmlist))])

                    def main(b, c):
                        return -0.0064 * b + 0.0306 * c - 0.955

                    try:
                        first, second = msg.split(" relation of ")[1].split(" with ")
                        first, second = first.strip(), second.strip()
                        req = round(main(sumGiver(first), sumGiver(second)))
                        reqdict = {1: "sister/brother", 2: "enemy", 3: "love", 4: "friend"}
                        return f"{reqdict.get(req, reqdict[random.randint(1, 4)])}\nby the way function used is -0.0064*x + 0.0306*y + -0.955"
                    except Exception as e:
                        return str(e)

                elif "question of" in msg:
                    try:
                        subject = msg.split('question of')[1].split(" is ")[0].strip()
                        answer = msg.split('question of')[1].split('answer')[1].strip()
                        with open("questions.json", 'r') as main1:
                            content = json.load(main1)
                        with open("rankings.json", 'r') as mainm:
                            maindict = json.load(mainm)
                        questioncontent = msg.split(f'question of {subject} is')[1].split("answer")[0].strip() + f"(By {nm})"
                        idd = len(content[subject]) + 1
                        content[subject].append({f"{idd}. {questioncontent}": answer})
                        with open("questions.json", 'w') as main2:
                            json.dump(content, main2, indent=2)
                        maindict[nm] = maindict.get(nm, 0) + 1
                        with open("rankings.json", 'w') as lastmain:
                            json.dump(maindict, lastmain, indent=2)
                        return "thank you bhai for providing question, really appreciate that!"
                    except Exception as e:
                        return str(e)

                elif "what is" in msg or "who is" in msg:
                    try:
                        mainmsg = msg.split("what is")[1].lower().strip() if "what is" in msg else msg.split("who is")[1].lower().strip()
                        content = wikipedia.summary(mainmsg, auto_suggest=False, sentences=2)
                        return content + " information by jeetu bhayiya :)"
                    except Exception as e:
                        return str(e)

                elif "answer of" in msg:
                    try:
                        ansno = int(msg.split("answer of")[1].split(" of ")[0].strip())
                        subject = msg.split("answer of")[1].split(" of ")[1].strip()
                        with open("questions.json", 'r') as questionread:
                            questions = json.load(questionread)
                        questionsrequired = list(questions[subject])
                        ans1 = list(questionsrequired[ansno - 1].items())[0][1]
                        return ans1
                    except Exception as e:
                        return str(e)

                elif 'leaderboard' in msg or 'lb' in msg:
                    with open('rankings.json', 'r') as maindict1:
                        d = json.load(maindict1)
                    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
                    returningString = "\n".join([f"Rank {i}: {name} - {ranks}" for i, (name, ranks) in enumerate(sorted_d.items(), 1)])
                    return "Contributing leaders\n" + returningString

                elif "help" in msg:
                    commands = ('1. for just casual chatting no need for any command just use jeetu in text\n\n'
                                '2. for contributing any question you can use the command like this --> jeetu question of (subject name) is (question content) answer (answer content) [command should be as it is, or it won"t work] \n\n'
                                '3. for checking out the answer of the following question you can use the command for example --> jeetu answer of [question number] of [subject]\n\n'
                                '4. for asking questions use the command --> jeetu give me question of (subject name)\n\n'
                                '5. For asking a biography or theory or history of something/someone use the command for example--> jeetu who is virat kohli "or" jeetu what is sexual intercourse\n\n'
                                '6. for asking any mathematical question or any data related question or any relation of fantasy or any general knowledge question use command for example-->jeetu solve 3x+1=16 or jeetu solve who is the husband of hermione granger or jeetu solve what is the gdp of usa\n'
                                '7. Fun game of SELF using mathematics, you can use the command -> relation of NAME1 with NAME2')
                    return commands

                else:
                    return chatbot.request(msg)
    return None
