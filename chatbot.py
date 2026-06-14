import random

responses = {
    'hello': [
        'Hey there! How can I assist you today?',
        'Hello! Great to see you!',
        'Hi! DecoBot is online and ready!'
    ],
    'hi': [
        'Hi! Welcome to DecoBot!',
        'Hey! How can I help you?',
        'Hi there! What can I do for you?'
    ],
    'hey': [
        'Hey! What can I do for you?',
        'Hey there! Ask me anything!',
        'Hello! I am listening.'
    ],

    'what is your name': [
        'I am DecoBot, your AI assistant at DecodeLabs!',
        'They call me DecoBot!',
        'DecoBot at your service!'
    ],
    'who are you': [
        'I am DecoBot — a rule-based AI built at DecodeLabs.',
        'I am your personal AI assistant, DecoBot!',
        'Just a friendly rule-based chatbot from DecodeLabs!'
    ],
    'who made you': [
        'I was built by an AI Engineer intern at DecodeLabs!',
        'A talented DecodeLabs intern created me!',
        'Born from code written at DecodeLabs!'
    ],

    'how are you': [
        'Running at 100% efficiency, thanks for asking!',
        'All systems operational!',
        'I am doing great! How about you?'
    ],
    'are you okay': [
        'All systems operational!',
        'Perfect condition, thank you!',
        'Never been better!'
    ],

    'what is ai': [
        'AI stands for Artificial Intelligence — machines simulating human thinking.',
        'AI is the science of making machines smart!',
        'Artificial Intelligence is programming machines to think and learn.'
    ],
    'what is machine learning': [
        'Machine Learning is AI that learns from data instead of explicit rules.',
        'ML is teaching machines using data patterns!',
        'Machine Learning lets computers learn without being explicitly programmed.'
    ],
    'what is a chatbot': [
        'A chatbot is a program that simulates conversation with humans.',
        'A chatbot is an AI interface for human-computer interaction!',
        'I am a chatbot — a program designed to chat with you!'
    ],

    'what is decodelabs': [
        'DecodeLabs is a tech training company based in Greater Lucknow, India.',
        'DecodeLabs is where future AI engineers are built!',
        'A cutting-edge tech training organization from Lucknow, India.'
    ],
    'what are we building': [
        'We are building a rule-based chatbot as Project 1 of your AI training!',
        'Project 1 — a Rule-Based AI Chatbot. You are doing great!',
        'The foundation of AI — a rule-based chatbot!'
    ],

    'bye': [
        'Goodbye! Keep building great things!',
        'See you later! Happy coding!',
        'Bye! Come back anytime.'
    ],
    'goodbye': [
        'Goodbye! It was great chatting!',
        'See you soon! Keep coding!',
        'Take care! Goodbye!'
    ],
    'see you': [
        'Take care! Come back anytime.',
        'See you later!',
        'Goodbye for now!'
    ],

    'thank you': [
        'You are welcome! Always here to help.',
        'Happy to help!',
        'Anytime! That is what I am here for.'
    ],
    'thanks': [
        'No problem at all!',
        'Glad I could help!',
        'Always happy to assist!'
    ],
    'help': [
        'You can ask me about AI, DecodeLabs, or just say hello!',
        'Try asking: what is ai, who are you, or how are you!',
        'I can answer questions about AI and DecodeLabs. Give it a try!'
    ],

    'tell me a joke': [
        'Why do programmers prefer dark mode? Because light attracts bugs!',
        'Why did the AI break up with the algorithm? Too many if-else conditions!',
        'How many programmers does it take to change a bulb? None — it is a hardware problem!'
    ],
    'tell me a fact': [
        'The first chatbot was ELIZA, created in 1966!',
        'Python was named after Monty Python, not the snake!',
        'The term Artificial Intelligence was coined in 1956 by John McCarthy.'
    ],
}

def get_response(user_input):
    possible_replies = responses.get(user_input, None)

    if possible_replies:
        return random.choice(possible_replies)
    else:
        return "I don't understand that yet. Try asking something else!"


def run_chatbot():
    print("=" * 45)
    print("   Welcome to DecoBot - Rule-Based AI")
    print("   Type 'exit' to quit")
    print("=" * 45)

    while True:

        raw_input_text = input("\nYou: ")

        clean_input = raw_input_text.lower().strip()

        if clean_input in ['exit', 'quit', 'stop']:
            print("DecoBot: Goodbye! Session ended.")
            print("=" * 45)
            break

        if clean_input == '':
            print("DecoBot: Please type something!")
            continue

        reply = get_response(clean_input)
        print(f"DecoBot: {reply}")

if __name__ == "__main__":
    run_chatbot()