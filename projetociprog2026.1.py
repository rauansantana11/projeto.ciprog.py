# JOGO INTERATIVO - RESOLVENDO CONFLITOS NA ESCOLA
print("=" * 60)
print("BEM-VINDO À ESCOLA")
print("Faça as escolhas certas e ganhe recompensas")
print("=" * 60)

# Variáveis do jogador
nome = input("\nDigite o seu nome para começar: ").upper().strip()
pontos = 0
conquistas = []
fase_atual = 1

print(f"\nOlá {nome}! Vamos começar.")
print("Regra: Se precisar, peça uma dica quando errar.\n")

# Situação principal
print("-" * 60)
print("FASE 1")
print("SITUAÇÃO: Você chegou na escola e viu dois colegas discutindo muito feio.")
print("O que você faz?")
print("-" * 60)

print("A) Tenta acalmar os dois")
print("B) Filma a discussão para mostrar para os outros")
print("C) Ignora e segue o seu caminho")
print("D) Entra na briga e bate também")

# Loop para responder até acertar
while True:
    resposta = input("\nDigite a sua escolha (A/B/C/D): ").upper().strip()

    if resposta not in ["A", "B", "C", "D"]:
        print("Opção inválida! Digite apenas A, B, C ou D.")
        continue

    if resposta == "A":
        pontos += 20
        print("\nVocê fez a escolha certa!")
        print("Você conseguiu acalmar os dois colegas e ajudou a resolver o problema.")
        print(f"Você ganhou 20 pontos! Pontuação atual: {pontos}")
        
        # Desbloqueia a conquista
        if "Pacificador" not in conquistas:
            conquistas.append("Pacificador")
            print("\nCONQUISTA DESBLOQUEADA: Pacificador")
            print("Você mostrou que sabe resolver conflitos da forma correta!")
        break

    elif resposta == "B":
        print("\nFilmar não resolve nada, só espalha o problema e deixa a situação pior.")
        quer_dica = input("Você quer uma dica? (S/N): ").upper().strip()
        if quer_dica == "S":
            print("Dica: A melhor atitude é sempre tentar ajudar e acalmar as pessoas.")

    elif resposta == "C":
        print("\nIgnorar deixa o problema continuar e pode ficar ainda mais grave depois.")
        quer_dica = input("Você quer uma dica? (S/N): ").upper().strip()
        if quer_dica == "S":
            print("Dica: Quem ajuda a resolver ganha pontos e reconhecimento.")

    elif resposta == "D":
        print("\nSe bater também você só piora tudo e pode se dar mal junto com eles.")
        quer_dica = input("Você quer uma dica? (S/N): ").upper().strip()
        if quer_dica == "S":
            print("Dica: A força não resolve, o diálogo resolve.")

    print("Tente novamente.\n")

# Resultado final
print("\n" + "=" * 60)
print("FIM DA ATIVIDADE")
print("=" * 60)
print(f"NOME DO JOGADOR: {nome}")
print(f"PONTUAÇÃO FINAL: {pontos} pontos")
print("\nCONQUISTAS OBTIDAS:")

if len(conquistas) > 0:
    for c in conquistas:
        print(f"- {c}")
else:
    print("- Nenhuma conquista desbloqueada")

print("\nObrigado por participar!")
print("=" * 60)
