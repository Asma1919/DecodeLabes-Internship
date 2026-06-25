import customtkinter as ctk
def chatbot_reponse(user_input):
    reponces ={
        "hello": "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
        "hi": "Salut ! Quoi de neuf ?",
        "how are you": "Je suis un robot textuel et je fonctionne parfaitement, merci !",
        "what is your name": "Mon nom est AI-Bot, un chatbot basé sur des règles.",
        "help": "Je peux répondre à des salutations, vous demander mon nom, ou vous aider à quitter."
    }
    return reponces.get(user_input.lower(),"Désolé,je peux pas repondre a ta question .....")



def send_message(eveny=None):
    user_message =  user_input.get()
    if user_message.strip()!="":
      chat_history.configure(state="normal")   
      chat_history.insert("end",f" vous {user_message}\n"," user")

      bot_reponce=chatbot_reponse(user_message)
      chat_history.insert("end",f" vous {bot_reponce} \n"," bot")
      chat_history.configure(state="disabled")
      chat_history.see("end")
      user_input.delete(0,"end")

    
app=ctk.CTk() # cree une fenetre 
app.geometry("500x650")
app.title("AI CHATBOOT")
app.resizable(False, False)

header= ctk.CTkLabel(app,text="Bienvenu au chatboot",font=("Arial",22,"bold"))
header.pack(pady=10)

chat_history = ctk.CTkTextbox(app,height=400, state="disabled")
chat_history.tag_config("user",foreground="white")
chat_history.tag_config("user",foreground="green")
chat_history.pack(pady=10,padx=10,fill="both", expand= True)
chat_history.configure(font=("Arial",16))

user_input_frame= ctk.CTkFrame(app)
user_input_frame.pack(pady=10,padx=10,fill="x")

user_input=ctk.CTkEntry(user_input_frame,placeholder_text="Entrez votre message ici....",width=350)
user_input.pack(side="left",padx=5)
send_button=ctk.CTkButton(user_input_frame,text="Envoyer ", command="send_messsage")
send_button.pack(side="left") 

app.bind("<Return>",send_message)
app.mainloop()


