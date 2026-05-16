import os
import tarfile
import shutil
from datetime import datetime

# Configurações
ORIGEM = "analytics/logs"
DESTINO = "automation/backups"
LIMITE_RETENCAO = 5

def realizar_backup():
    if not os.path.exists(DESTINO):
        os.makedirs(DESTINO)

    # Criando o nome do arquivo: backup_20260516_1200.tar.gz
    data_str = datetime.now().strftime("%Y%m%d_%H%M")
    nome_arquivo = f"backup_logs_{data_str}.tar.gz"
    caminho_completo = os.path.join(DESTINO, nome_arquivo)

    print(f"📦 Iniciando backup de {ORIGEM}...")
    
    try:
        with tarfile.open(caminho_completo, "w:gz") as tar:
            tar.add(ORIGEM, arcname=os.path.basename(ORIGEM))
        print(f"✅ Backup concluído: {caminho_completo}")

        # Rotação de Backups (Retenção)
        gerenciar_retencao()

    except Exception as e:
        print(f"❌ Erro no backup: {e}")

def gerenciar_retencao():
    # Lista todos os arquivos de backup e ordena por data (mais antigos primeiro)
    backups = sorted(
        [os.path.join(DESTINO, f) for f in os.listdir(DESTINO) if f.endswith(".tar.gz")],
        key=os.path.getctime
    )

    while len(backups) > LIMITE_RETENCAO:
        antigo = backups.pop(0)
        os.remove(antigo)
        print(f"♻️  Removendo backup antigo por retenção: {antigo}")

if __name__ == "__main__":
    realizar_backup()
