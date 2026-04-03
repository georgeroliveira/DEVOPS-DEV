# 🔧 Setup 03 — Primeiro Boot e Configuração da VM

> **Execute diretamente na VM — pelo console do VirtualBox.**
> Ainda não temos SSH configurado com chave, então acesse pela tela da VM por enquanto.

---

## 🎯 Objetivo

Configurar a VM após a instalação: atualizar o sistema, instalar pacotes essenciais, configurar SSH por chave e preparar o ambiente para o VS Code Remote.

---

## 🔹 1. Primeiro login

Na tela do VirtualBox, faça login com o usuário criado durante a instalação:

```
devops-vm login: devops
Password: (senha que você definiu)
```

Você verá o prompt:

```
devops@devops-vm:~$
```

---

## 🔹 2. Verificar o IP da VM

Confirme que os dois adaptadores de rede estão ativos:

```bash
ip a
```

**O que verificar:**

```
enp0s3   → IP via DHCP (NAT) — acesso à internet
enp0s8   → 192.168.56.10     — IP fixo Host-Only
```

> Se `enp0s8` não aparecer com `192.168.56.10`, a configuração de rede durante
> a instalação não foi salva corretamente. Veja o troubleshooting no final.

---

## 🔹 3. Testar acesso à internet

```bash
ping -c 4 google.com
```

**Resultado esperado:** `0% packet loss`

> Se falhar, o adaptador NAT não está funcionando. Verifique as configurações
> de rede da VM no VirtualBox.

---

## 🔹 4. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

> Isso pode levar alguns minutos dependendo da sua internet.
> É uma boa prática sempre atualizar o sistema após a instalação.

---

## 🔹 5. Instalar pacotes essenciais

```bash
sudo apt install -y \
    curl \
    wget \
    git \
    unzip \
    htop \
    tree \
    net-tools
```

**Para que serve cada um:**

| Pacote     | Uso no curso                              |
|------------|-------------------------------------------|
| curl       | Testar APIs e health checks               |
| wget       | Baixar arquivos                           |
| git        | Versionamento de código (módulo 03)       |
| unzip      | Descompactar arquivos                     |
| htop       | Monitorar processos e recursos            |
| tree       | Visualizar estrutura de diretórios        |
| net-tools  | Comandos de rede (ifconfig, netstat)      |

---

## 🔹 6. Verificar o SSH

O OpenSSH Server foi instalado durante a configuração do Ubuntu. Confirme que está rodando:

```bash
sudo systemctl status ssh
```

**Resultado esperado:**

```
● ssh.service - OpenBSD Secure Shell server
     Active: active (running)
```

Se não estiver rodando:

```bash
sudo systemctl start ssh
sudo systemctl enable ssh
```

---

## 🔹 7. Configurar o firewall

Ative o firewall e libere apenas as portas necessárias:

```bash
# Ativar UFW
sudo ufw enable

# Liberar SSH (obrigatório — sem isso você perde o acesso remoto)
sudo ufw allow 22/tcp

# Verificar regras
sudo ufw status
```

**Resultado esperado:**

```
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
```

> As outras portas serão liberadas conforme o curso avançar.
> No módulo de redes você vai aprender a liberar portas específicas.

---

## 🔹 8. Configurar SSH por chave — no seu PC

Agora saia do console do VirtualBox e abra o terminal **do seu PC**.

### Gerar par de chaves (se ainda não tiver)

**Linux / macOS:**
```bash
ssh-keygen -t ed25519 -C "devops-bootcamp"
```

**Windows (PowerShell):**
```powershell
ssh-keygen -t ed25519 -C "devops-bootcamp"
```

Pressione `Enter` em todas as perguntas (sem senha na chave, para facilitar o uso com VS Code).

**Onde ficam as chaves:**

```
~/.ssh/id_ed25519      ← chave privada (nunca compartilhe)
~/.ssh/id_ed25519.pub  ← chave pública (vai para a VM)
```

---

### Copiar a chave pública para a VM

**Linux / macOS:**
```bash
ssh-copy-id devops@192.168.56.10
```

Digite a senha do usuário `devops` quando solicitado. Isso é a última vez que você vai precisar da senha.

**Windows (PowerShell):**
```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh devops@192.168.56.10 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

---

### Testar conexão por chave

```bash
ssh devops@192.168.56.10
```

**Resultado esperado:** login sem pedir senha.

```
devops@devops-vm:~$
```

---

## 🔹 9. Configurar alias SSH no seu PC

Crie o arquivo de configuração SSH para não precisar digitar o IP toda vez:

**Linux / macOS** — edite `~/.ssh/config`:
```bash
nano ~/.ssh/config
```

**Windows** — edite `C:\Users\SeuUsuario\.ssh\config` no Notepad ou VS Code.

**Conteúdo:**
```
Host devops-vm
    HostName 192.168.56.10
    User devops
    IdentityFile ~/.ssh/id_ed25519
```

Salve o arquivo.

**Testar o alias:**

```bash
ssh devops-vm
```

Deve conectar diretamente, sem IP e sem senha.

---

## 🔹 10. Configurações finais na VM

Conectado via SSH, execute:

```bash
# Configurar timezone para São Paulo
sudo timedatectl set-timezone America/Sao_Paulo

# Confirmar timezone
timedatectl

# Configurar hostname
sudo hostnamectl set-hostname devops-vm

# Confirmar
hostname
```

---

## 🔹 11. Snapshot da VM (recomendado)

Antes de continuar, tire um snapshot da VM no estado atual. Isso permite voltar a este ponto se algo der errado nos próximos módulos.

No VirtualBox:

1. Selecione a VM `devops-vm`
2. Menu **Machine → Take Snapshot**
3. Nome: `setup-inicial`
4. Clique em **OK**

> Dica: tire um snapshot antes de cada módulo. Se algo quebrar, você volta ao estado anterior em segundos.

---

## ✅ Checklist

- [ ] Login realizado com usuário `devops`
- [ ] IP `192.168.56.10` confirmado em `enp0s8`
- [ ] Internet funcionando (`ping google.com`)
- [ ] Sistema atualizado (`apt update && upgrade`)
- [ ] Pacotes essenciais instalados
- [ ] SSH rodando (`systemctl status ssh`)
- [ ] Firewall ativo com porta 22 liberada
- [ ] Par de chaves SSH gerado no PC
- [ ] Chave pública copiada para a VM
- [ ] Login SSH por chave funcionando (sem senha)
- [ ] Alias `devops-vm` configurado no `~/.ssh/config`
- [ ] Timezone configurado para São Paulo
- [ ] Snapshot `setup-inicial` criado

---

## 🆘 Troubleshooting

### IP 192.168.56.10 não aparece

A configuração de rede estática não foi salva durante a instalação. Corrija manualmente:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Adicione a configuração da interface Host-Only:

```yaml
network:
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      addresses:
        - 192.168.56.10/24
  version: 2
```

Aplique:

```bash
sudo netplan apply
ip a
```

---

### SSH: Connection refused

```bash
# Verificar se o serviço está rodando
sudo systemctl status ssh

# Iniciar se necessário
sudo systemctl start ssh
sudo systemctl enable ssh

# Verificar se a porta está aberta
sudo ufw status
sudo ufw allow 22/tcp
```

---

### Permission denied (publickey)

A chave pública não foi copiada corretamente para a VM.

Verifique na VM:

```bash
cat ~/.ssh/authorized_keys
```

Deve conter o conteúdo da sua chave pública (`~/.ssh/id_ed25519.pub`).

Se estiver vazio, copie manualmente:

```bash
# Na VM, crie o diretório e arquivo
mkdir -p ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# No seu PC, exiba a chave pública
cat ~/.ssh/id_ed25519.pub
# Copie o conteúdo e cole na VM:
echo "cole-aqui-o-conteudo-da-chave-publica" >> ~/.ssh/authorized_keys
```

---

## ➡️ Próximo passo

👉 Abra `04-vscode-remote.md` para conectar o VS Code na VM.