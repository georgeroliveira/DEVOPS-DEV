# 💻 Setup 04 — VS Code Remote SSH

> **Execute no seu PC (Windows, Mac ou Linux).**

---

## 🎯 Objetivo

Conectar o VS Code à VM via SSH para editar arquivos e executar comandos remotamente — exatamente como profissionais DevOps trabalham com servidores em produção.

```
Seu PC (VS Code)
       │
       │  Remote SSH
       ▼
VM Ubuntu 24.04 (192.168.56.10)
       │
       ├── Arquivos editados remotamente
       ├── Terminal integrado roda na VM
       └── Docker, Git, apps rodam na VM
```

---

## 🔹 1. Instalar o VS Code

Se ainda não tiver o VS Code instalado:

```
https://code.visualstudio.com/download
```

| Sistema | Arquivo           |
|---------|-------------------|
| Windows | `.exe` (User Installer) |
| macOS   | `.dmg`            |
| Linux   | `.deb` ou `.rpm`  |

---

## 🔹 2. Instalar a extensão Remote SSH

1. Abra o VS Code
2. Clique no ícone de **Extensions** na barra lateral (ou `Ctrl + Shift + X`)
3. Pesquise: `Remote - SSH`
4. Clique em **Install** na extensão da Microsoft

> Identificador oficial: `ms-vscode-remote.remote-ssh`

**Após instalar**, você verá um ícone verde `><` no canto inferior esquerdo do VS Code.

---

## 🔹 3. Configurar o host SSH no VS Code

1. Pressione `Ctrl + Shift + P` para abrir a **Command Palette**
2. Digite: `Remote-SSH: Open SSH Configuration File`
3. Selecione o arquivo `~/.ssh/config` (Linux/Mac) ou `C:\Users\SeuUsuario\.ssh\config` (Windows)

Confirme que o conteúdo está assim (configurado no passo anterior):

```
Host devops-vm
    HostName 192.168.56.10
    User devops
    IdentityFile ~/.ssh/id_ed25519
```

Salve o arquivo (`Ctrl + S`).

---

## 🔹 4. Conectar na VM

1. Pressione `Ctrl + Shift + P`
2. Digite: `Remote-SSH: Connect to Host`
3. Selecione **devops-vm**

Uma nova janela do VS Code vai abrir.

**Na primeira conexão:**
- O VS Code vai perguntar o tipo de SO: selecione **Linux**
- Vai instalar o VS Code Server na VM automaticamente (aguarde ~1 minuto)

**Conexão estabelecida quando:**
- O canto inferior esquerdo mostrar: `SSH: devops-vm`
- O terminal integrado mostrar o prompt da VM

---

## 🔹 5. Abrir o terminal integrado

Com o VS Code conectado na VM:

```
Ctrl + J   (ou  Ctrl + `)
```

Você verá o prompt da VM:

```
devops@devops-vm:~$
```

**Confirme que está dentro da VM:**

```bash
hostname
# devops-vm

whoami
# devops

ip a | grep 192.168.56
# inet 192.168.56.10/24
```

> Todos os comandos digitados neste terminal rodam **dentro da VM**,
> não no seu PC. Isso simula exatamente o trabalho com servidores remotos.

---

## 🔹 6. Abrir uma pasta na VM

1. No VS Code conectado, clique em **File → Open Folder**
2. Digite o caminho: `/home/devops`
3. Clique em **OK**

Você verá os arquivos da VM no painel lateral do VS Code.

---

## 🔹 7. Criar um arquivo de teste

No terminal integrado:

```bash
mkdir -p ~/workspace
cd ~/workspace
echo "# Meu DevOps Bootcamp" > README.md
```

No VS Code, navegue até `/home/devops/workspace/README.md` e edite o arquivo.

> Você está editando um arquivo que existe **dentro da VM**, usando a interface
> do VS Code no seu PC. Esse é o fluxo de trabalho do curso inteiro.

---

## 🔹 8. Extensões recomendadas

Com o VS Code conectado na VM, instale estas extensões **no contexto remoto**:

| Extensão              | Para quê                        |
|-----------------------|---------------------------------|
| Docker                | Gerenciar containers            |
| GitLens               | Visualizar histórico Git        |
| YAML                  | Syntax highlighting para YAML   |
| Shell Script          | Syntax para scripts bash        |
| Python                | Suporte a Python/Flask          |

Para instalar:
1. `Ctrl + Shift + X`
2. Pesquise a extensão
3. Clique em **Install in SSH: devops-vm**

> As extensões instaladas no contexto remoto rodam na VM, não no seu PC.

---

## 🔹 9. Testar o fluxo completo

Execute no terminal integrado do VS Code:

```bash
# Confirmar que está na VM
hostname && whoami

# Testar internet
ping -c 2 google.com

# Testar git
git --version

# Ver espaço em disco
df -h /

# Ver memória
free -h
```

**Resultado esperado:**

```
devops-vm
devops
PING google.com ... 0% packet loss
git version 2.x.x
/dev/sda1  20G  5.x G  14G  xx% /
              total  used  free
Mem:          1.9Gi  ...
```

---

## 🔹 10. Reconectar após reiniciar a VM

Sempre que reiniciar a VM ou o PC:

1. Inicie a VM no VirtualBox (pode ser em modo **headless** — sem abrir a janela)
2. Aguarde ~30 segundos para a VM inicializar
3. No VS Code: `Ctrl + Shift + P` → `Remote-SSH: Connect to Host` → `devops-vm`

**Iniciar VM em modo headless (sem janela):**

No VirtualBox, clique com o botão direito na VM → **Start → Headless Start**.

> Headless é o modo padrão em produção — servidores não têm monitor.

---

## ✅ Checklist

- [ ] VS Code instalado
- [ ] Extensão Remote SSH instalada
- [ ] Host `devops-vm` configurado no `~/.ssh/config`
- [ ] Conexão SSH estabelecida (canto inferior esquerdo: `SSH: devops-vm`)
- [ ] Terminal integrado abrindo com prompt da VM
- [ ] `hostname` retorna `devops-vm`
- [ ] Pasta `/home/devops` aberta no VS Code
- [ ] Arquivo criado e editado remotamente
- [ ] Extensões instaladas no contexto remoto

---

## 🆘 Troubleshooting

### "Could not establish connection to devops-vm"

```bash
# No seu PC, teste a conexão SSH manualmente
ssh devops-vm

# Se falhar, verifique se a VM está rodando
# No VirtualBox: a VM deve aparecer como "Running"

# Verifique o IP
ssh devops@192.168.56.10
```

---

### Canto inferior esquerdo não mostra "SSH: devops-vm"

A conexão não foi estabelecida. Tente:

1. `Ctrl + Shift + P` → `Remote-SSH: Kill VS Code Server on Host`
2. Aguarde 10 segundos
3. `Ctrl + Shift + P` → `Remote-SSH: Connect to Host` → `devops-vm`

---

### "Permission denied (publickey)"

A chave SSH não está configurada corretamente. Verifique:

```bash
# No seu PC
cat ~/.ssh/id_ed25519.pub

# Na VM (via console do VirtualBox)
cat ~/.ssh/authorized_keys
```

Os conteúdos devem ser iguais. Se não forem, refaça o passo 8 do `03-first-boot.md`.

---

### Terminal integrado abre no PC, não na VM

Verifique se o VS Code está conectado: o canto inferior esquerdo deve mostrar `SSH: devops-vm` em verde. Se mostrar apenas `><`, você está local.

Clique no `><` e selecione **Connect to Host → devops-vm**.

---

### VS Code muito lento após conectar

O VS Code Server está sendo instalado na VM na primeira conexão. Aguarde a barra de progresso completar. Nas próximas conexões será instantâneo.

---

## ➡️ Ambiente configurado

✅ **Seu ambiente de desenvolvimento está pronto.**

```
Seu PC (VS Code)  ──SSH──▶  VM Ubuntu 24.04 (192.168.56.10)
                               └── Terminal integrado
                               └── Arquivos remotos
                               └── Docker (módulo 04)
                               └── Git (módulo 03)
```

👉 Volte ao `README.md` do módulo 01 e inicie as aulas.