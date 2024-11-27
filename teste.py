import json
from app_postit.models import Card

cards = Card.objects.all()

for card in cards:
    try:
        # Tenta carregar o conteúdo como JSON
        json.loads(card.conteudo)
    except json.JSONDecodeError:
        # Se falhar, assume que está no formato de dicionário Python
        conteudo_dict = eval(card.conteudo)
        card.conteudo = json.dumps(conteudo_dict)
        card.save()
