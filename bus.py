import os
import random
import time

CORES = {
    "LARANJA": "\033[38;5;214m",
    "VERDE": "\033[32m", 
    "AZUL": "\033[34m",
    "AMARELO": "\033[33m",
    "VERMELHO": "\033[31m",
    "ROXO": "\033[35m",
    "RESET": "\033[0m",
    "NEGRITO": "\033[1m"
}

def desenhar_buses(pos_mclaren, pos_lamborghini):
    output = []
    
    output.append(115 * "▬")
    
    output.append((pos_mclaren * " ") + "    🚍 MCLAREN     " + ((95 - pos_mclaren) * " ") + "🏁")
    output.append((pos_mclaren * " ") + "   _____________   " + ((95 - pos_mclaren) * " ") + "|")
    output.append((pos_mclaren * " ") + "  |█████████████|  " + ((94 - pos_mclaren) * " ") + "|") 
    output.append((pos_mclaren * " ") + " _|_____________|_ " + ((94 - pos_mclaren) * " ") + "|")
    output.append((pos_mclaren * " ") + "|  🏎️ MCLAREN F1  | " + ((93 - pos_mclaren) * " ") + "|")
    output.append((pos_mclaren * " ") + "|💨____________💨| " + ((93 - pos_mclaren) * " ") + "|")
    
    output.append(115 * "─")
    
    output.append((pos_lamborghini * " ") + "   🚍 LAMBORGHINI  " + ((95 - pos_lamborghini) * " ") + "🏁")
    output.append((pos_lamborghini * " ") + "   _____________   " + ((95 - pos_lamborghini) * " ") + "|")
    output.append((pos_lamborghini * " ") + "  |█████████████|  " + ((94 - pos_lamborghini) * " ") + "|")
    output.append((pos_lamborghini * " ") + " _|_____________|_ " + ((94 - pos_lamborghini) * " ") + "|")
    output.append((pos_lamborghini * " ") + "| 🐂 LAMBORGHINI | " + ((93 - pos_lamborghini) * " ") + "|")
    output.append((pos_lamborghini * " ") + "|💨____________💨| " + ((93 - pos_lamborghini) * " ") + "|")
    
    output.append(115 * "▬")
    
    return "\n".join(output)

def animacao_inicio():
    os.system("cls" if os.name == "nt" else "clear")
    
    titulo = f"""
{CORES['NEGRITO']}{CORES['LARANJA']}
    ╔══════════════════════════════════════╗
    ║         CORRIDA DE BUSÕES           ║
    ║      MCLAREN vs LAMBORGHINI         ║
    ╚══════════════════════════════════════╝
{CORES['RESET']}
"""
    print(titulo)
    
    for i in range(3, 0, -1):
        print(f"{CORES['AMARELO']}A corrida começa em {i}...{CORES['RESET']}")
        time.sleep(1)
    
    print(f"{CORES['VERDE']}🎌 GO! 🎌{CORES['RESET']}")
    time.sleep(1)

def mostrar_info(mclaren, lamborghini, rodada):
    print(f"\n{CORES['AZUL']}▬ INFO DA CORRIDA ▬{CORES['RESET']}")
    print(f"{CORES['LARANJA']}MCLAREN:    {mclaren:3d} metros{CORES['RESET']}")
    print(f"{CORES['AMARELO']}LAMBORGHINI: {lamborghini:3d} metros{CORES['RESET']}")
    print(f"Rodada: {rodada}")

def iniciar_corrida():
    pos_mclaren = 0
    pos_lamborghini = 0
    rodada = 0
    meta = 97
    vencedor = None
    
    animacao_inicio()
    
    while pos_mclaren < meta and pos_lamborghini < meta:
        rodada += 1
        
        avanco_mclaren = random.choices([0, 1, 2, 3], weights=[15, 50, 30, 5])[0]
        avanco_lamborghini = random.choices([0, 1, 2, 3], weights=[10, 45, 40, 5])[0]
        
        pos_mclaren += avanco_mclaren
        pos_lamborghini += avanco_lamborghini
        
        pos_mclaren = min(pos_mclaren, meta)
        pos_lamborghini = min(pos_lamborghini, meta)
        
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{CORES['NEGRITO']}CORRIDA DE BUSÕES ESPORTIVOS - Rodada {rodada}{CORES['RESET']}\n")
        print(desenhar_buses(pos_mclaren, pos_lamborghini))
        mostrar_info(pos_mclaren, pos_lamborghini, rodada)
        
        if avanco_mclaren > 0 or avanco_lamborghini > 0:
            print(f"\n{CORES['VERDE']}Avanços nesta rodada:")
            if avanco_mclaren > 0:
                print(f"  MCLAREN: +{avanco_mclaren} metros")
            if avanco_lamborghini > 0:
                print(f"  LAMBORGHINI: +{avanco_lamborghini} metros{CORES['RESET']}")
        
        time.sleep(0.1)
    
    if pos_mclaren >= meta and pos_lamborghini >= meta:
        vencedor = "EMPATE"
    elif pos_mclaren >= meta:
        vencedor = "MCLAREN"
    else:
        vencedor = "LAMBORGHINI"
    
    return vencedor, rodada

def mostrar_resultado(vencedor, rodadas):
    os.system("cls" if os.name == "nt" else "clear")
    
    if vencedor == "EMPATE":
        cor = CORES['ROXO']
        mensagem = "EMPATOU! INCRÍVEL!"
    elif vencedor == "MCLAREN":
        cor = CORES['LARANJA']
        mensagem = "MCLAREN VENCEU! 🏆"
    else:
        cor = CORES['AMARELO'] 
        mensagem = "LAMBORGHINI VENCEU! 🏆"
    
    print(f"""
{cor}{CORES['NEGRITO']}
    ╔══════════════════════════════════════╗
    ║           RESULTADO FINAL            ║
    ║                                      ║
    ║          {mensagem:^20}        ║
    ║                                      ║
    ║           Corrida terminou           ║
    ║            em {rodadas:3d} rodadas            ║
    ║                                      ║
    ╚══════════════════════════════════════╝
{CORES['RESET']}
""")

def jogar_novamente():
    while True:
        resposta = input(f"\n{CORES['AZUL']}Jogar novamente? (s/n): {CORES['RESET']}").lower()
        if resposta in ['s', 'si', 'sí', 'sim', 'y', 'yes']:
            return True
        elif resposta in ['n', 'nao', 'não', 'no']:
            return False
        else:
            print(f"{CORES['VERMELHO']}Digite 's' ou 'n'{CORES['RESET']}")

def main():
    while True:
        vencedor, rodadas = iniciar_corrida()
        mostrar_resultado(vencedor, rodadas)
        
        if not jogar_novamente():
            print(f"\n{CORES['VERDE']}Obrigado por jogar! Até a próxima! 🚍{CORES['RESET']}")
            break

if __name__ == "__main__":
    main()