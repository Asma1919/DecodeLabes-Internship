def main():
    knowledge_base = {
        "hello": "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
        "hi": "Salut ! Quoi de neuf ?",
        "how are you": "Je suis un robot textuel et je fonctionne parfaitement, merci !",
        "what is your name": "Mon nom est AI-Bot, un chatbot basé sur des règles.",
        "help": "Je peux répondre à des salutations, vous demander mon nom, ou vous aider à quitter."
    }

    print("=== Bienvenue sur le Chatbot (Rule-Based) ===")
    print("Tapez 'exit' ou 'quit' pour quitter le programme.\n")

    while True:
        user_input = input("Vous : ")
        clean_input = user_input.strip().lower()

        if clean_input in ["exit", "quit", "quitter"]:
            print("Bot : Au revoir ! Passez une excellente journée.")
            break

        if clean_input in knowledge_base:
            print(f"Bot : {knowledge_base[clean_input]}")
        else:
            print("Bot : Désolé, je ne comprends pas. Pouvez-vous reformuler ou taper 'help' ?")
            
     
main()

