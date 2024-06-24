from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
     "ExampleBot",
     storage_adapter = "chatterbot.storage.SQLStorageAdapter",
     logic_adapters=[
         "chatterbot.logic.BestMatch",
         "chatterbot.logic.MathematicalEvaluation"
     ],
     database_uri="sqlite:///database.sqlite3"
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response 

if __name__ == "__main__":
    print("Hello, I am ExampleBot. How can I assist you today?")
    while True:
        try: 
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]
                print("ExampleBot: GoodBye!")
                break
            response = get_response(user_input)
            print(f"ExampleBot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("ExampleBot: GoodBye!")
            break

