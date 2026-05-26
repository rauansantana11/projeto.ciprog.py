# JOGO INTERATIVO - CONFLITOS NA ESCOLA
print("=" * 60)
print("BEM-VINDO À ESCOLA")
print("5 FASES | PONTOS | CONQUISTAS")
print("=" * 60)

# Dados do jogador
nome = input("\nDigite o seu nome para começar: ").upper().strip()
pontos = 0
fase_atual = 1
total_fases = 5
conquistas = []

print(f"\nVamos começar, {nome}! Você está na FASE {fase_atual} de {total_fases}")
print("Regra: Escolha com sabedoria e ganhe recompensas!\n")

# LISTA COM AS 5 FASES
fases = [
    {
        "fase": 1,
        "situacao": "Você chegou na escola e viu dois colegas discutindo muito forte.",
        "opcoes": [
            "A) Tenta acalmar os dois",
            "B) Filma a discussão para mostrar para os outros",
            "C) Ignora e segue o seu caminho",
            "D) Entra na briga e bate também"
        ],
        "correta": "A",
        "pontos_ganhos": 20,
        "explicacao": "Acalmar é o primeiro passo certo para resolver qualquer conflito.",
        "dica": "Pense: qual atitude faz a briga parar e não piorar?"
    },
    {
        "fase": 2,
        "situacao": "Depois de acalmá-los, eles continuam chateados e não querem se falar.",
        "opcoes": [
            "A) Dá conselhos e pede para eles se entenderem",
            "B) Fica rindo da situação",
            "C) Diz que não é problema seu",
            "D) Fica do lado de um dos dois"
        ],
        "correta": "A",
        "pontos_ganhos": 25,
        "explicacao": "Um bom conselho é o melhor presente para resolver um conflito.",
        "dica": "Resolver problema é ajudar, não julgar ou sair de perto."
    },
    {
        "fase": 3,
        "situacao": "Um professor chega e quer saber o que aconteceu para ajudar.",
        "opcoes": [
            "A) Conta a verdade dos dois lados com calma",
            "B) Inventa uma história errada",
            "C) Fica quieto e não fala nada",
            "D) Fala só o lado que você acha certo"
        ],
        "correta": "A",
        "pontos_ganhos": 25,
        "explicacao": "Contar a verdade completa ajuda a resolver tudo de forma justa.",
        "dica": "Justiça e verdade são sempre a melhor escolha."
    },
    {
        "fase": 4,
        "situacao": "Os dois colegas se resolveram e agradecem a sua ajuda.",
        "opcoes": [
            "A) Diz que foi um prazer ajudar e que todos devem se dar bem",
            "B) Diz que só fez isso para aparecer",
            "C) Ignora o agradecimento",
            "D) Diz que eles são que precisam mudar"
        ],
        "correta": "A",
        "pontos_ganhos": 30,
        "explicacao": "Ser humilde e educado faz de você uma pessoa melhor.",
        "dica": "Quem ajuda de coração recebe o reconhecimento certo."
    },
    {
        "fase": 5,
        "situacao": "No final da semana, a diretora da escola elogia quem ajuda os outros.",
        "opcoes": [
            "A) Aceita o elogio e diz que todos podem fazer o mesmo",
            "B) Se acha melhor que todo mundo",
            "C) Diz que não merece nada",
            "D) Não liga para o elogio"
        ],
        "correta": "A",
        "pontos_ganhos": 30,
        "explicacao": "Reconhecer que a paz vale mais que tudo é a maior vitória.",
        "dica": "Ser um pacificador é uma qualidade que vale ouro."
    }
]

# FUNÇÃO PARA VERIFICAR CONQUISTAS
def verificar_conquistas():
    if fase_atual == 2 and "Iniciante da Paz" not in conquistas:
        conquistas.append("Iniciante da Paz - Concluiu a fase 2")
    if fase_atual == 4 and "Amigo da Verdade" not in conquistas:
        conquistas.append("Amigo da Verdade - Sempre escolheu o caminho certo")
    if fase_atual == 5 and pontos >= 130 and "Pacificador" not in conquistas:
        conquistas.append("Pacificador - Concluiu todas as fases com sucesso")

# EXECUÇÃO DO JOGO
indice = 0
while indice < len(fases):
    fase = fases[indice]
    print("\n" + "-" * 60)
    print(f"STATUS: FASE {fase_atual} de {total_fases} | Pontos: {pontos}")
    print("-" * 60)

    print(f"\nSITUAÇÃO: {fase['situacao']}")
    for opcao in fase["opcoes"]:
        print(opcao)

    # Recebe e valida resposta
    while True:
        resposta = input("\nDigite sua escolha (A/B/C/D): ").upper().strip()
        if resposta in ["A", "B", "C", "D"]:
            break
        print("Opção inválida! Digite apenas A, B, C ou D.")

    # Verifica resultado
    if resposta == fase["correta"]:
        pontos += fase["pontos_ganhos"]
        print("\nEscolha correta!")
        print(fase["explicacao"])
        print(f"Ganhou {fase['pontos_ganhos']} pontos. Total atual: {pontos}")
        
        fase_atual += 1
        indice += 1
        verificar_conquistas()

        if fase_atual <= total_fases:
            print(f"Avançou para a FASE {fase_atual}!")
    else:
        print("\nEssa não é a melhor escolha.")
        quer_dica = input("Você quer uma dica? (S/N): ").upper().strip()
        if quer_dica == "S":
            print(f"Dica: {fase['dica']}")
        print("Tente novamente.\n")

# RESULTADO FINAL COMPLETO
print("\n" + "=" * 60)
print("FIM DE JOGO")
print("=" * 60)
print(f"NOME DO JOGADOR: {nome}")
print(f"PONTUAÇÃO FINAL: {pontos} pontos")
print(f"FASES CONCLUÍDAS: {total_fases} de {total_fases}")

print("\nCONQUISTAS DESBLOQUEADAS:")
if len(conquistas) > 0:
    for conquista in conquistas:
        print(f"- {conquista}")
else:
    print("- Nenhuma conquista desbloqueada")

print("\nCLASSIFICAÇÃO:")
if pontos >= 130:
    print("EXCELENTE - Você é um verdadeiro Pacificador!")
elif pontos >= 90:
    print("BOM - Sabe como resolver problemas na escola.")
else:
    print("REGULAR - Continue tentando para melhorar suas escolhas.")

print("\nObrigado por jogar!")
print("=" * 60)
