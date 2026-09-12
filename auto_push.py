import subprocess
import sys

def rodar_comando(comando):
    """Executa um comando no terminal do Windows e exibe a saída em tempo real."""
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print(f"Erro ao executar: {comando}", file=sys.stderr)
        print(resultado.stderr, file=sys.stderr)
        sys.exit(1)

def main():
    print("--- Iniciando Automação de Push do Git ---")
    
    # 1. Solicita a mensagem do commit
    mensagem = input("Digite a mensagem do commit [Atualização automatica]: ").strip()
    if not mensagem:
        mensagem = "Atualização automatica"
        
    # 2. Executa a sequência de comandos do Git
    print("\n[1/3] Adicionando arquivos (git add .)...")
    rodar_comando("git add .")
    
    print(f"[2/3] Criando commit: \"{mensagem}\"...")
    rodar_comando(f'git commit -m "{mensagem}"')
    
    print("[3/3] Enviando para o GitHub (git push)...")
    rodar_comando("git push")
    
    print("\n Sucesso! Código enviado para o GitHub.")
    input("\nPressione Enter para fechar...")

if __name__ == "__main__":
    main()
