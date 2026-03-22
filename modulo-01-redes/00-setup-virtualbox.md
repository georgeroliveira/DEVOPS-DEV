# ⚙️ Setup 01 — Instalação do VirtualBox

> **Execute no seu PC (Windows, Mac ou Linux) — não na VM.**

---

## 🎯 Objetivo

Instalar o VirtualBox 7.2 para criar e gerenciar a VM que será usada durante todo o curso.

---

## 📥 Download

Acesse o site oficial e baixe o instalador para o seu sistema operacional:

```
https://www.virtualbox.org/wiki/Downloads
```

| Sistema       | Arquivo para baixar                          |
|---------------|----------------------------------------------|
| Windows       | `VirtualBox-7.2.x-xxxxxx-Win.exe`            |
| macOS (Intel) | `VirtualBox-7.2.x-xxxxxx-OSX.dmg`            |
| macOS (Apple Silicon) | `VirtualBox-7.2.x-xxxxxx-macOSArm64.dmg` |
| Ubuntu/Debian | `virtualbox-7.2_7.2.x-xxxxxx~Ubuntu~noble_amd64.deb` |

> Versão atual: **7.2.6** (Janeiro 2026)

---

## 🪟 Instalação no Windows

1. Execute o `.exe` baixado como **Administrador**
2. Clique em **Next** nas telas iniciais
3. Mantenha as opções padrão
4. Aceite o aviso sobre interfaces de rede temporariamente desconectadas
5. Clique em **Install**
6. Ao finalizar, clique em **Finish**

**Verificar instalação:**
```
VirtualBox → Menu → Help → About VirtualBox
```
Deve mostrar: `Version 7.2.x`

---

## 🍎 Instalação no macOS

1. Abra o `.dmg` baixado
2. Execute o `VirtualBox.pkg`
3. Siga o assistente de instalação
4. Se aparecer aviso de **System Extension Blocked**:
   - Vá em `System Settings → Privacy & Security`
   - Role para baixo e clique em **Allow** para Oracle America
   - Reinicie o Mac se solicitado
5. Abra o VirtualBox para confirmar instalação

---

## 🐧 Instalação no Ubuntu/Debian

```bash
# Instalar o pacote .deb baixado
sudo dpkg -i virtualbox-7.2_*.deb

# Corrigir dependências se necessário
sudo apt --fix-broken install

# Adicionar seu usuário ao grupo vboxusers
sudo usermod -aG vboxusers $USER

# Fazer logout e login novamente para aplicar o grupo
# Verificar instalação
vboxmanage --version
```

---

## 🧩 Extension Pack (recomendado)

O Extension Pack adiciona suporte a USB 3.0 e outras funcionalidades úteis.

1. Na mesma página de downloads, baixe:
   ```
   Oracle VirtualBox Extension Pack
   ```
2. No VirtualBox: `File → Tools → Extension Pack Manager`
3. Clique no ícone de **+** e selecione o arquivo `.vbox-extpack`
4. Aceite os termos e clique em **Install**

---

## ✅ Checklist

- [ ] VirtualBox instalado e abrindo normalmente
- [ ] Versão 7.2.x confirmada
- [ ] Extension Pack instalado

---

## ➡️ Próximo passo

👉 Abra `02-ubuntu-server.md` para baixar e criar a VM com Ubuntu.