# 🖥️ Setup 02 — Criando a VM Ubuntu Server

> **Execute no seu PC (Windows, Mac ou Linux) — não na VM.**

---

## 🎯 Objetivo

Baixar o Ubuntu Server 24.04 LTS e criar a VM que será usada durante todo o curso.

---

## 📥 Download da ISO

Acesse o site oficial e baixe a ISO:

```
https://ubuntu.com/download/server
```

Clique em **Download Ubuntu Server 24.04 LTS**.

> Arquivo: `ubuntu-24.04.x-live-server-amd64.iso` (~2.5 GB)
> Aguarde o download completo antes de prosseguir.

---

## 🆕 Criar a VM no VirtualBox

### 1. Abrir o assistente de criação

No VirtualBox, clique em **New** (ou `Ctrl + N`).

---

### 2. Nome e sistema operacional

| Campo             | Valor                        |
|-------------------|------------------------------|
| Name              | `devops-vm`                  |
| Folder            | Deixe o padrão               |
| ISO Image         | Selecione a ISO baixada       |
| Type              | Linux                        |
| Version           | Ubuntu (64-bit)              |

Marque a opção **Skip Unattended Installation**.

> Isso garante que você vai passar pela instalação manualmente,
> aprendendo o processo real de configuração de um servidor.

Clique em **Next**.

---

### 3. Hardware

| Recurso | Valor recomendado | Mínimo |
|---------|-------------------|--------|
| RAM     | 2048 MB (2 GB)    | 1024 MB |
| CPUs    | 2                 | 1      |

Clique em **Next**.

---

### 4. Disco

| Campo       | Valor       |
|-------------|-------------|
| Tipo        | VDI         |
| Alocação    | Dynamically allocated |
| Tamanho     | 20 GB       |

Clique em **Next** → **Finish**.

---

## 🌐 Configurar as interfaces de rede

A VM precisa de **duas interfaces de rede**:

| Adaptador | Tipo      | Para quê                              |
|-----------|-----------|---------------------------------------|
| 1         | NAT       | Acesso à internet (apt, git, docker)  |
| 2         | Host-Only | IP fixo para SSH e acesso às apps     |

### Configurar Adaptador 1 (NAT)

1. Selecione a VM `devops-vm` → clique em **Settings**
2. Vá em **Network → Adapter 1**
3. Marque **Enable Network Adapter**
4. Attached to: **NAT**
5. Clique em **OK**

### Criar a rede Host-Only (se não existir)

1. No menu do VirtualBox: **File → Tools → Network Manager**
2. Clique em **Create** (ícone +)
3. Confirme que a rede `vboxnet0` foi criada com:
   - IPv4: `192.168.56.1`
   - Mask: `255.255.255.0`
   - DHCP: **desabilitado**
4. Feche o Network Manager

### Configurar Adaptador 2 (Host-Only)

1. Volte em **Settings → Network → Adapter 2**
2. Marque **Enable Network Adapter**
3. Attached to: **Host-Only Adapter**
4. Name: **vboxnet0**
5. Clique em **OK**

---

## 🚀 Iniciar a instalação

### 1. Iniciar a VM

Selecione `devops-vm` e clique em **Start**.

A VM vai iniciar a partir da ISO do Ubuntu.

---

### 2. Tela de boot

Selecione **Try or Install Ubuntu Server** e pressione `Enter`.

Aguarde o carregamento (pode levar 1-2 minutos).

---

### 3. Idioma

Selecione **English** e pressione `Enter`.

> Mantenha inglês — todos os comandos do curso usam saídas em inglês,
> o que facilita pesquisar erros e documentação.

---

### 4. Atualização do instalador

Se aparecer a mensagem **"Installer update available"**:

Selecione **Continue without updating** e pressione `Enter`.

---

### 5. Layout do teclado

| Campo    | Valor          |
|----------|----------------|
| Layout   | Portuguese (Brazil) ou English (US) |
| Variant  | Deixe o padrão |

Selecione **Done** e pressione `Enter`.

---

### 6. Tipo de instalação

Selecione **Ubuntu Server** (opção padrão) e pressione `Enter`.

---

### 7. Configuração de rede

O instalador vai detectar as duas interfaces automaticamente:

- `enp0s3` → NAT (deve ter recebido IP via DHCP)
- `enp0s8` → Host-Only (vamos configurar IP fixo)

**Configurar IP fixo no enp0s8:**

1. Selecione `enp0s8` → **Edit IPv4**
2. Method: **Manual**
3. Preencha:

| Campo   | Valor             |
|---------|-------------------|
| Subnet  | `192.168.56.0/24` |
| Address | `192.168.56.10`   |
| Gateway | Deixe vazio       |
| DNS     | Deixe vazio       |

4. Selecione **Save** → **Done**

> O IP `192.168.56.10` será o endereço fixo da sua VM durante todo o curso.

---

### 8. Proxy

Deixe vazio e selecione **Done**.

---

### 9. Mirror do Ubuntu

Deixe o padrão e selecione **Done**.

> O instalador vai testar a conexão com o mirror. Aguarde.

---

### 10. Disco

Selecione **Use an entire disk** → **Done** → **Continue**.

> Isso vai usar todo o disco virtual de 20 GB criado anteriormente.

---

### 11. Perfil do usuário

| Campo           | Valor              |
|-----------------|--------------------|
| Your name       | `DevOps`           |
| Server name     | `devops-vm`        |
| Username        | `devops`           |
| Password        | Escolha uma senha  |
| Confirm password| Repita a senha     |

Selecione **Done**.

> Anote a senha — você vai precisar dela no primeiro acesso.

---

### 12. Ubuntu Pro

Selecione **Skip for now** → **Continue**.

---

### 13. SSH

Marque **Install OpenSSH server** (pressione `Space` para marcar).

Selecione **Done**.

> Isso habilita o acesso SSH à VM — essencial para o VS Code Remote.

---

### 14. Snaps adicionais

Não selecione nada. Selecione **Done**.

---

### 15. Instalação

Aguarde a instalação concluir. Pode levar 5-15 minutos dependendo da sua internet.

Quando aparecer **"Installation complete!"**, selecione **Reboot Now**.

> O instalador vai pedir para remover a mídia de instalação.
> No VirtualBox isso acontece automaticamente. Pressione `Enter`.

---

## ✅ Checklist

- [ ] ISO do Ubuntu 24.04 baixada
- [ ] VM criada com 2 GB RAM e 20 GB disco
- [ ] Adaptador 1 configurado como NAT
- [ ] Adaptador 2 configurado como Host-Only (192.168.56.10)
- [ ] Ubuntu Server instalado com usuário `devops`
- [ ] OpenSSH Server instalado durante a instalação
- [ ] VM reiniciada após a instalação

---

## ➡️ Próximo passo

👉 Abra `03-first-boot.md` para configurar a VM após o primeiro boot.