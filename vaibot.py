import nltk
import random
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
chatbot_pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "How can I help you today?"]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what is your name|who are you",
        ["I'm a chatbot. You can call me VaiBot.", "I am Vaibot! I represent my creator, Vaibhav :)"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye! Have a great day!"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual chatbot and don't have a physical location. But I can assist you from anywhere!"]
    ],
    [
        r"(.*) (weather|temperature) ?",
        ["I'm sorry, I don't have access to real-time weather information."]
    ],
    [
        r"(.*) (major|studying) ?",
        ["I am studying Computer Engineering at UBC, currently in my 2nd year."]
    ],
      [
        r"(.*) (hobbies|interests|like to do) ?",
        ["I love watching sunsets, playing soccer, doing programming projects, and hanging out with my friends"]
    ],
    [
        r"(.*) (movie|film) ?",
        ["Now You See Me 2 was the best movie I ever watched. The scene where they robbed a chip through doing card tricks lives a special place in my heart (ifykyk)"]
    ],
    [
        r"(.*) (subject|class) ?",
        ["I've always loved Math since a young age, right now my favourite class is CPEN 221: Software Construction I!"]
    ],
    [
        r"(.*) (tv|show|Netflix) ?",
        ["The Office is number one. My go-to in any mood, time, or setting. "]
    ],
    [
        r"(.*) (ideology|moral|belief) ?",
        ["I live by the quote 'Theory can only take you so far' from the very own Oppenheimer. My desire is to always apply my knowledge in any sort of aspect. "]
    ],
    [
        r"(.*) (food|eat|fast) ?",
        ["My favourite food is Shahi Paneer, an indian dish with creamy cottage cheese squares. As for my go-to, Chipotle is undeafated."]
    ],
    [
        r"(.*) (weather|temperature) ?",
        ["I'm sorry, I don't have access to real-time weather information."]
    ],
    [
        r"(.*) (soccer|player|sport) ?",
        ["Having played soccer since I was 6, my favourite sport is soccer. My favourite team is FC Barcelona (Forca Barca!) and my favourite player is Lionel Messi! Catch me on the fields when there's any free time."]
    ],
    [
        r"thank you|thanks",
        ["No problem, anytime!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you please rephrase that?", "Can you tell me more about it?"]
    ]
]

# Create a chatbot using the Chat class
chatbot = Chat(chatbot_pairs, reflections)

# Main loop to interact with the chatbot
initiate = "Hello! I'm VaiBot, Vaibhav's virtual chatbot that can answer general questions you have about him, speaking as himself. \n Note - I am a Beta version so I am currently limited to answering questions on these topics: \n1. General Personal (who I am) \n2. University Major \n3. Hobbies \n4. Favourite Movie \n5. Favourite School Subject \n6. Countries Visited \n7. Favourite TV Show \n8. Ideology \n9. Favourite Food \n10. Soccer  \nYou can type 'bye' to exit."
print(initiate)
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("VaiBot: Goodbye, hope to see you again!")
        break
    response = chatbot.respond(user_input)
    print("VaiBot:", response)
