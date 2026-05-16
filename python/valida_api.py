import requests
import sys

def verificar_endpoint(url):
    print(f"🔍 Verificando: {url}...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"✅ Sucesso: O endpoint está online!")
        else:
            print(f"⚠️ Alerta: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    url_alvo = sys.argv[1] if len(sys.argv) > 1 else "https://api.github.com"
    verificar_endpoint(url_alvo)

