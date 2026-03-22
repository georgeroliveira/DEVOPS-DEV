# 🐧 Módulo 02 — Linux para DevOps

## 🎯 Objetivo

Dominar o Linux no nível necessário para trabalhar como DevOps — gerenciar servidores, automatizar tarefas, diagnosticar problemas e fazer deploy de aplicações, tudo via linha de comando.

---

## 🖥️ Contexto do curso

Todo este módulo é executado **dentro da VM via VS Code Remote SSH**.

```
Seu PC
   │
   │  VS Code Remote SSH
   ▼
VM Ubuntu 24.04  ←  você está aqui
   │
   │  É aqui que o DevOps trabalha
   ▼
Aplicações, containers, serviços
```

> O Linux que você aprende aqui é o mesmo que roda em EC2 (AWS),
> VM (Azure) e Compute Engine (GCP).

---

## 🧠 O que você vai aprender

- Navegar e entender a estrutura de diretórios do Linux
- Manipular arquivos e diretórios via terminal
- Editar arquivos com vim e nano
- Gerenciar usuários, grupos e permissões
- Instalar e remover pacotes com apt
- Gerenciar serviços com systemctl
- Ler e analisar logs com journalctl e tail
- Monitorar processos e recursos do sistema
- Escrever scripts Bash para automação
- Agendar tarefas com crontab

---

## 🚀 Pré-requisitos

- Módulo 01 concluído
- VM Ubuntu rodando no VirtualBox
- VS Code conectado via Remote SSH

---

## ▶️ Como iniciar

```bash
# Dentro da VM via VS Code Remote SSH
git clone <url-do-repositorio>
cd modulo-02-linux
```

---

## 📚 Estrutura do módulo

```
modulo-02-linux/
├── README.md                    ← você está aqui
├── aula/
│   ├── 01-introducao.md         ← o que é Linux e por que DevOps usa
│   ├── 02-diretorios.md         ← estrutura /etc /var /home /opt
│   ├── 03-comandos.md           ← ls, cp, mv, rm, find, grep, vim
│   ├── 04-usuarios.md           ← useradd, groups, sudo
│   ├── 05-permissoes.md         ← chmod, chown, ls -la
│   ├── 06-pacotes.md            ← apt update, install, remove
│   ├── 07-servicos.md           ← systemctl start/stop/enable/status
│   ├── 08-logs.md               ← journalctl, tail -f, grep em logs
│   ├── 09-processos.md          ← ps, top, htop, kill, df -h, free -h
│   ├── 10-shellscript.md        ← variáveis, if, loops, crontab
│   └── 11-desafio.md            ← desafio final integrando tudo
├── scripts/
│   └── setup-server.sh          ← script que o aluno constrói no lab
├── exercises/
│   └── exercicios.md            ← exercícios de fixação
└── solution/
    └── README.md                ← gabarito completo
```

---

## 🔄 Sequência recomendada

```
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11
```

Cada aula depende da anterior. Não pule etapas.

---

## ⏱️ Tempo estimado

| Aula                        | Tempo    |
|-----------------------------|----------|
| 01 — Introdução             | 10 min   |
| 02 — Diretórios             | 15 min   |
| 03 — Comandos essenciais    | 25 min   |
| 04 — Usuários               | 20 min   |
| 05 — Permissões             | 20 min   |
| 06 — Pacotes                | 15 min   |
| 07 — Serviços               | 20 min   |
| 08 — Logs                   | 20 min   |
| 09 — Processos              | 15 min   |
| 10 — Shellscript            | 30 min   |
| 11 — Desafio                | 30 min   |
| **Total**                   | **~3h**  |

---

## 🔌 Referência rápida de comandos

```bash
# Navegação
pwd / ls -la / cd / mkdir / rm -rf / cp / mv

# Busca
find /etc -name "*.conf"
grep -r "error" /var/log/

# Usuários
useradd -m usuario / passwd usuario / usermod -aG sudo usuario

# Permissões
chmod 755 arquivo / chown usuario:grupo arquivo / ls -la

# Pacotes
sudo apt update && sudo apt upgrade -y
sudo apt install pacote / sudo apt remove pacote

# Serviços
sudo systemctl start|stop|restart|enable|status servico

# Logs
sudo journalctl -u servico -f
sudo tail -f /var/log/syslog

# Processos
ps aux / top / htop / kill PID / df -h / free -h

# Crontab
crontab -e / crontab -l
```

---

## 🔗 Conexão com os próximos módulos

| O que você aprende aqui | Onde vai usar |
|---|---|
| `git` instalado via apt | Módulo 03 — Git |
| Permissões de arquivo | Módulo 04 — Docker |
| systemctl + serviços | Módulo 04 — Docker daemon |
| Shellscript + variáveis | Módulo 07 — CI/CD |
| Logs + journalctl | Módulo 08 — Observabilidade |