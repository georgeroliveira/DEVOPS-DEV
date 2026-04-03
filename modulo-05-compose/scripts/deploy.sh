#!/bin/bash
set -e

echo "Criando backup antes do deploy..."
./scripts/backup.sh

echo "Build da aplicação..."
docker compose build --no-cache app

echo "Subindo serviços..."
docker compose up -d --remove-orphans

echo "Aguardando health check..."
sleep 30

if curl -f http://localhost/health > /dev/null 2>&1; then
    echo "Deploy concluído com sucesso."
else
    echo "Erro: health check falhou após o deploy."
    docker compose logs app
    exit 1
fi
