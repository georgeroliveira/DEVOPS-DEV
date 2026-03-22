# 🧪 Aula 02 — Laboratório: Linux na VM

> **Execute todos os comandos dentro da VM via VS Code Remote SSH.**  
> Siga a sequência — cada passo prepara o próximo.

---

## 🎯 Objetivo

Ao final deste lab você terá:
- Um usuário `deploy` configurado com as permissões corretas
- Pacotes essenciais instalados
- Um serviço nginx rodando e monitorado
- Um script de setup automatizado
- Tudo documentado em logs

---

## 🔹 1. Reconhecimento do servidor

```bash
# Quem sou eu e onde estou
whoami
hostname
pwd

# Versão do sistema
lsb_release -a
uname -r

# Recursos disponíveis
df -h
free -h
nproc
```

> Anote o IP da VM para usar nos próximos passos:
```bash
ip a | grep "inet " | grep -v "127.0.0.1"
```

---

## 🔹 2. Explorar a estrutura de diretórios

```bash
# Ver estrutura raiz
ls /

# Explorar /etc
ls /etc/ | head -20
cat /etc/hostname
cat /etc/hosts

# Explorar logs disponíveis
ls /var/log/

# Ver diretório home
ls -la ~
```

---

## 🔹 3. Atualizar o sistema e instalar pacotes

```bash
# Atualizar lista de pacotes
sudo apt update

# Instalar pacotes essenciais do curso
sudo apt install -y \
  curl \
  wget \
  git \
  vim \
  net-tools \
  htop \
  tree \
  unzip \
  jq

# Confirmar instalações
curl --version | head -1
git --version
vim --version | head -1
```

---

## 🔹 4. Criar usuário deploy

```bash
# Criar usuário
sudo useradd -m -s /bin/bash -c "Deploy User" deploy

# Definir senha
sudo passwd deploy

# Adicionar ao grupo sudo
sudo usermod -aG sudo deploy

# Verificar
id deploy
groups deploy
ls /home/deploy
```

---

## 🔹 5. Criar estrutura da aplicação

```bash
# Criar diretório da aplicação
sudo mkdir -p /opt/app/{logs,config,scripts}

# Transferir dono para o usuário deploy
sudo chown -R deploy:deploy /opt/app/

# Aplicar permissões corretas
sudo chmod -R 755 /opt/app/

# Verificar
ls -la /opt/app/
```

---

## 🔹 6. Criar arquivo de configuração

```bash
# Criar config da aplicação
sudo -u deploy vim /opt/app/config/app.conf
```

Conteúdo do arquivo (pressione `i` para inserir):
```
APP_NAME=minha-app
APP_PORT=8080
APP_ENV=development
LOG_LEVEL=info
```

Salve com `Esc` → `:wq`

```bash
# Ajustar permissões do arquivo de config
chmod 644 /opt/app/config/app.conf

# Verificar conteúdo
cat /opt/app/config/app.conf
```

---

## 🔹 7. Instalar e configurar nginx

```bash
# Instalar nginx
sudo apt install -y nginx

# Verificar status
sudo systemctl status nginx

# Iniciar e habilitar no boot
sudo systemctl enable --now nginx

# Confirmar que está rodando
sudo systemctl is-active nginx
curl http://localhost
```

---

## 🔹 8. Verificar firewall

```bash
# Ver status do firewall
sudo ufw status

# Se estiver ativo, liberar portas necessárias
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 8080/tcp

# Confirmar regras
sudo ufw status
```

---

## 🔹 9. Monitorar logs do nginx

```bash
# Abra dois terminais na VM

# Terminal 1 — acompanhar logs em tempo real
sudo journalctl -u nginx -f

# Terminal 2 — gerar requisições para ver nos logs
curl http://localhost
curl http://localhost
curl http://localhost/pagina-que-nao-existe
```

```bash
# Buscar erros nos logs
sudo journalctl -u nginx -p err
sudo grep "error" /var/log/nginx/error.log
```

---

## 🔹 10. Monitorar processos e recursos

```bash
# Ver todos os processos
ps aux | head -20

# Filtrar nginx
ps aux | grep nginx

# Monitor interativo (q para sair)
htop

# Disco e memória
df -h
free -h

# Tamanho dos logs
du -sh /var/log/*
```

---

## 🔹 11. Criar script de healthcheck

```bash
vim /opt/app/scripts/healthcheck.sh
```

Conteúdo:
```bash
#!/bin/bash

# Script de healthcheck dos serviços
# Uso: ./healthcheck.sh

SERVICOS=("nginx" "ssh")

echo "=========================================="
echo " Healthcheck — $(hostname) — $(date)"
echo "=========================================="

for SERVICO in "${SERVICOS[@]}"; do
    if systemctl is-active --quiet $SERVICO; then
        echo "✅ $SERVICO — rodando"
    else
        echo "❌ $SERVICO — parado"
    fi
done

echo ""
echo "--- Recursos ---"
echo "Disco:   $(df -h / | awk 'NR==2{print $5}') usado"
echo "Memória: $(free -h | awk '/Mem/{print $3}') / $(free -h | awk '/Mem/{print $2}')"
echo "Uptime:  $(uptime -p)"
```

```bash
# Dar permissão de execução
chmod +x /opt/app/scripts/healthcheck.sh

# Executar
/opt/app/scripts/healthcheck.sh
```

---

## 🔹 12. Agendar healthcheck com crontab

```bash
# Editar crontab do usuário deploy
sudo -u deploy crontab -e
```

Adicionar linha (executa a cada 5 minutos):
```
*/5 * * * * /opt/app/scripts/healthcheck.sh >> /opt/app/logs/healthcheck.log 2>&1
```

```bash
# Verificar que foi salvo
sudo -u deploy crontab -l

# Ver log gerado (aguardar 5 minutos ou testar manualmente)
/opt/app/scripts/healthcheck.sh >> /opt/app/logs/healthcheck.log
cat /opt/app/logs/healthcheck.log
```

---

## 🔹 13. Verificar permissões finais

```bash
# Estrutura completa com permissões
ls -la /opt/app/
ls -la /opt/app/scripts/
ls -la /opt/app/config/
ls -la /opt/app/logs/

# Permissões do .ssh
ls -la ~/.ssh/
```

---

## ✅ Checklist do laboratório

- [ ] IP da VM identificado
- [ ] Sistema atualizado e pacotes instalados
- [ ] Usuário `deploy` criado com sudo
- [ ] Estrutura `/opt/app/` criada com permissões corretas
- [ ] Arquivo de configuração criado com vim
- [ ] Nginx instalado, rodando e habilitado no boot
- [ ] Firewall verificado e portas liberadas
- [ ] Logs do nginx monitorados em tempo real
- [ ] Script `healthcheck.sh` criado e executando
- [ ] Crontab configurado para executar a cada 5 minutos
- [ ] Log de saída do healthcheck confirmado

---

## ➡️ Próximo passo

👉 Abra `03-desafio.md` e resolva o desafio.