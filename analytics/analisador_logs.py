import re
from collections import Counter
import json

# Caminho do log
LOG_PATH = "logs/access.log"

# Regex para capturar: IP, Data/Hora, Método, URL e Status Code
# Exemplo de linha: 192.168.1.1 - - [16/May/2026:10:00:01] "GET /home HTTP/1.1" 200
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\[(?P<data>.*?)\]\s"(?P<metodo>\w+)\s(?P<url>.*?)\s.*?\"\s(?P<status>\d+)')

def analisar_servidor():
    ips = []
    status_codes = []
    total_linhas = 0

    try:
        with open(LOG_PATH, "r") as f:
            for linha in f:
                match = log_pattern.match(linha)
                if match:
                    ips.append(match.group("ip"))
                    status_codes.append(match.group("status"))
                    total_linhas += 1

        # Processamento Estatístico
        contagem_ips = Counter(ips)
        contagem_status = Counter(status_codes)

        print("-" * 30)
        print(f"📊 RELATÓRIO DE ACESSOS ({total_linhas} linhas)")
        print("-" * 30)
        
        print("\n🔝 Top 3 IPs com mais acessos:")
        for ip, count in contagem_ips.most_common(3):
            print(f"  {ip}: {count} requisições")

        print("\n🚦 Status HTTP detectados:")
        for status, count in contagem_status.items():
            print(f"  Code {status}: {count} vezes")

        # Exportando para JSON (Formato de Dado Estruturado)
        resultado = {
            "total_analisado": total_linhas,
            "ips": dict(contagem_ips),
            "status": dict(contagem_status)
        }
        
        with open("logs/resumo_estatistico.json", "w") as j:
            json.dump(resultado, j, indent=4)
        
        print("\n✅ Resumo exportado para: logs/resumo_estatistico.json")

    except FileNotFoundError:
        print("❌ Erro: Arquivo de log não encontrado.")

if __name__ == "__main__":
    analisar_servidor()
