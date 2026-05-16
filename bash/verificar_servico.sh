#!/bin/bash

# Script para monitorar serviços no sistema
SERVICO=$1

if [ -z "$SERVICO" ]; then
    echo "Uso: ./verificar_servico.sh [nome_do_servico]"
    exit 1
fi

if systemctl is-active --quiet "$SERVICO"; then
    echo "✅ O serviço $SERVICO está rodando."
else
    echo "❌ O serviço $SERVICO está PARADO!"
    # Aqui poderia entrar um comando para reiniciar:
    # sudo systemctl restart $SERVICO
fi

