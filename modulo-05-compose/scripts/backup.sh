#!/bin/bash
set -e

BACKUP_DIR="backups"
DATE=$(date +%Y%m%d_%H%M%S)
FILE="${BACKUP_DIR}/db_${DATE}.sql"

mkdir -p "$BACKUP_DIR"

echo "Criando backup..."
docker exec taskmanager-db pg_dump -U taskuser taskdb > "$FILE"

gzip "$FILE"
echo "Backup criado: ${FILE}.gz"

# Manter apenas os últimos 7 backups
ls -t "${BACKUP_DIR}"/*.sql.gz | tail -n +8 | xargs -r rm
