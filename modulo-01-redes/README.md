# ⚙️ Setup do Ambiente — Pré-requisito do Curso

> **Execute este setup antes da primeira aula.**
> Todo o curso é feito dentro da VM. Sem ela configurada, nada funciona.

---

## 🎯 Objetivo

Configurar o ambiente completo do curso:

```
Seu PC (Windows / Mac / Linux)
        │
        │  VS Code Remote SSH
        ▼
VM Ubuntu 24.04 Server (VirtualBox)
        │
        │  Simula uma EC2 (AWS) / VM (Azure) / Instance (GCP)
        ▼
   Docker + Compose + Git + Apps
```

Tudo que você aprender aqui funciona da mesma forma em qualquer cloud.

---

## 📋 O que você vai instalar

| Etapa | Arquivo                    | O que faz                                       |
|-------|----------------------------|-------------------------------------------------|
| 1     | `00-setup-virtualbox.md`   | Instala o VirtualBox no seu PC                  |
| 2     | `02-ubuntu-server.md`      | Baixa a ISO e cria a VM com as configs do curso  |
| 3     | `03-first-boot.md`         | Primeiro boot, usuário, SSH e hardening básico   |
| 4     | `04-vscode-remote.md`      | Conecta o VS Code na VM via Remote SSH           |

---

## 🖥️ Requisitos mínimos do seu PC

| Recurso | Mínimo       | Recomendado  |
|---------|--------------|--------------|
| CPU     | 4 cores      | 6+ cores     |
| RAM     | 8 GB         | 16 GB        |
| Disco   | 30 GB livre  | 50 GB livre  |
| OS      | Windows 10 / macOS 12 / Ubuntu 20.04 | Qualquer versão atual |

> Virtualização (VT-x / AMD-V) precisa estar habilitada na BIOS.
> Na maioria dos PCs modernos já está ativada por padrão.

---

## 📦 Especificações da VM do curso

```
SO:       Ubuntu 24.04 Server LTS (sem interface gráfica)
RAM:      2 GB
CPU:      2 vCPUs
Disco:    20 GB
Rede 1:   NAT          → acesso à internet (apt, git, docker pull)
Rede 2:   Host-Only    → IP fixo para SSH e acesso às apps
```

> IP padrão do curso: `192.168.56.10`
> Usuário padrão: `devops`

---

## 🔄 Sequência obrigatória

Execute nesta ordem — cada etapa depende da anterior:

```
00-setup-virtualbox.md
      ↓
02-ubuntu-server.md
      ↓
03-first-boot.md
      ↓
04-vscode-remote.md
      ↓
✅ Ambiente pronto — pode começar as aulas
```

---

## ⏱️ Tempo estimado

| Etapa                  | Tempo       |
|------------------------|-------------|
| Instalar VirtualBox    | 10 min      |
| Criar VM + instalar SO | 20 min      |
| First boot + hardening | 15 min      |
| VS Code Remote SSH     | 10 min      |
| **Total**              | **~55 min** |

---

## 🆘 Problemas comuns

| Problema                              | Solução                                               |
|---------------------------------------|-------------------------------------------------------|
| VirtualBox não abre / erro de kernel  | Habilitar VT-x/AMD-V na BIOS                          |
| VM não consegue acessar internet      | Verificar adaptador NAT nas configurações da VM       |
| SSH: `Connection refused`             | Verificar se o serviço SSH está rodando na VM         |
| VS Code não conecta                   | Conferir IP da VM com `ip a` e checar `~/.ssh/config` |
| Tela preta ao iniciar a VM            | Aumentar memória de vídeo nas configurações da VM     |

---

## ➡️ Começar

👉 Abra `00-setup-virtualbox.md`