#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Uso: ./restore.sh <arquivo.sql.gz>"
    echo ""
    echo "Backups disponíveis:"
    ls -lh backups/*.sql.gz 2>/dev/null || echo "Nenhum backup encontrado."
    exit 1
fi

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "Erro: arquivo $BACKUP_FILE não encontrado."
    exit 1
fi

echo "Restaurando $BACKUP_FILE..."
gunzip -c "$BACKUP_FILE" | docker exec -i taskmanager-db psql -U taskuser taskdb

echo "Restore concluído."
