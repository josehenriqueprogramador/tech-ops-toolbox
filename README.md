# Tech Ops Toolbox 🛠️

Este repositório contém uma coleção de scripts essenciais para automação de infraestrutura, monitorização de serviços e validação de conectividade. Ideal para ambientes de administração de sistemas e suporte técnico avançado.

## 📂 Estrutura do Projeto

### 1. Automação em Bash (`/bash`)
* **`verificar_servico.sh`**: Script para monitorizar o estado de serviços do sistema (systemd).
    * **Caso de uso**: Pode ser configurado num agendador de tarefas (Cron) para validar a cada 5 minutos se serviços críticos (como Docker, Nginx ou SSH) estão ativos.
    * **Execução**: `./bash/verificar_servico.sh [nome-do-servico]`

### 2. Monitorização em Python (`/python`)
* **`valida_api.py`**: Ferramenta para validação de endpoints e APIs.
    * **Caso de uso**: Integrar em fluxos de CI/CD ou monitorização de saúde (Health Checks) para garantir que as APIs de integração estão a responder corretamente (Status 200).
    * **Execução**: `python python/valida_api.py [url-da-api]`

## 🚀 Como Utilizar

### Pré-requisitos
* Sistema operativo Linux ou ambiente Termux.
* Python 3.x instalado.
* Biblioteca `requests` (instalar via `pip install requests`).

### Passos Rápidos
1. Clone o repositório:
   ```bash
   git clone [https://github.com/josehenriqueprogramador/tech-ops-toolbox.git](https://github.com/josehenriqueprogramador/tech-ops-toolbox.git)
2. Dê permissão de execução aos scripts:

```bash
chmod +x bash/verificar_servico.sh

### Documentação desenvolvida por José Henrique Jardim.