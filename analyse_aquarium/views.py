from django.shortcuts import render
import ollama
from django.conf import settings
# Create your views here.
host_ai = settings.LLM_LOCAL

def chat_ollama_remote(request):
    response_text = ""
    prompt = ""

    ollama_api_url = host_ai
    client = ollama.Client(host=ollama_api_url) # exemple: "http://127.0.0.14:11434"
    print(client.list())
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        if prompt:
            try:
                # Appel au modèle 'mistral' sur le serveur distant
                # Assurez-vous que le modèle 'mistral' a été téléchargé sur le serveur distant
                stream = client.chat(
                    model='mistral:7b',
                    messages=[{'role': 'user', 'content': prompt}],
                    stream=True
                )

                # Récupération de la réponse
                full_response = ""
                for chunk in stream:
                    full_response += chunk['message']['content']

                response_text = full_response
            except Exception as e:
                response_text = f"Erreur lors de la communication avec le serveur Ollama : {e}"

    return render(request, 'analyse_aquarium/chat.html', {'response': response_text,
        'prompt': prompt
                                                          })
