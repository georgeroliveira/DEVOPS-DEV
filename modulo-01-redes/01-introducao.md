# 📘 Aula 01 — Conceitos de Redes para DevOps

> **Foco:** Apenas o que você vai usar no dia a dia como DevOps.

---

## 🌐 O que é uma rede?

Rede é quando duas ou mais máquinas conseguem se comunicar.

Exemplo real:

```
Seu PC  →  SSH  →  VM (servidor)
Browser →  HTTP →  Aplicação rodando na VM
```

---

## 🔹 IP — Endereço da máquina

O IP identifica uma máquina na rede.

```
192.168.0.10   → IP privado (rede local / VM)
8.8.8.8        → IP público (Google DNS)
127.0.0.1      → localhost (a própria máquina)
```

> No contexto do curso: sua VM terá um IP na rede do VirtualBox.
> Você vai usar esse IP para conectar via SSH e acessar aplicações.

---

## 🔹 Porta — Endereço do serviço

A porta identifica **qual serviço** dentro da máquina está sendo acessado.

| Porta | Serviço    |
|-------|------------|
| 22    | SSH        |
| 80    | HTTP       |
| 443   | HTTPS      |
| 3000  | Node.js    |
| 5432  | PostgreSQL |
| 8080  | HTTP alt   |

> Exemplo: `192.168.0.10:8080` → acessa o serviço na porta 8080 da VM.

---

## 🔹 DNS — Tradução de nomes

DNS converte um nome legível em IP.

```
google.com   →  142.250.x.x
github.com   →  140.82.x.x
```

> Sem DNS, você teria que lembrar o IP de cada site.

---

## 🔹 HTTP vs HTTPS

| Protocolo | Criptografia | Uso                   |
|-----------|--------------|-----------------------|
| HTTP      | ❌ Não        | Desenvolvimento local |
| HTTPS     | ✅ Sim        | Produção              |

> No curso, vamos usar HTTP localmente e entender por que HTTPS é obrigatório em produção.

---

## 🔹 SSH — Como você acessa servidores remotos

SSH (Secure Shell) é o protocolo usado para acessar servidores Linux remotamente com segurança.

**É exatamente isso que você está fazendo quando conecta no VS Code à VM.**

```
Seu PC  →  SSH (porta 22)  →  VM Ubuntu
```

Na cloud, é o mesmo fluxo:

```
Seu PC  →  SSH (porta 22)  →  EC2 (AWS)
Seu PC  →  SSH (porta 22)  →  VM (Azure)
Seu PC  →  SSH (porta 22)  →  Instance (GCP)
```

### Como o SSH autentica

SSH usa um par de chaves criptográficas:

```
🔑 Chave privada  → fica no SEU PC (nunca compartilhe)
🔓 Chave pública  → fica no SERVIDOR (VM / EC2)
```

Fluxo de autenticação:

```
1. Você tenta conectar: ssh usuario@192.168.56.10
2. O servidor verifica se sua chave pública está cadastrada
3. Seu PC prova que tem a chave privada correspondente
4. Conexão estabelecida — sem digitar senha
```

### Comandos essenciais de SSH

```bash
# Gerar par de chaves
ssh-keygen -t ed25519 -C "seu-email@email.com"

# Exibir chave pública gerada (você copia para o servidor)
cat ~/.ssh/id_ed25519.pub

# Conectar em um servidor
ssh usuario@192.168.56.10

# Conectar com chave específica
ssh -i ~/.ssh/id_ed25519 usuario@192.168.56.10

# Copiar chave pública para o servidor
ssh-copy-id usuario@192.168.56.10
```

### Arquivo de configuração SSH

Para não precisar digitar IP e usuário toda vez:

```bash
# ~/.ssh/config
Host minha-vm
    HostName 192.168.56.10
    User devops
    IdentityFile ~/.ssh/id_ed25519
```

Depois é só:

```bash
ssh minha-vm
```

> Isso é exatamente o que o VS Code Remote SSH usa por baixo dos panos.

---

## 🔹 Modelo de comunicação

Toda comunicação na rede segue este fluxo:

```
Cliente  →  [IP:Porta]  →  Servidor  →  Resposta
```

Exemplos práticos do curso:

```
VS Code   →  192.168.56.10:22    →  VM (SSH)
Browser   →  192.168.56.10:8080  →  App na VM (HTTP)
Pipeline  →  192.168.56.10:22    →  VM (deploy via SSH no módulo 07)
```

---

## 🧠 Resumo

| Conceito | O que faz                         | Exemplo                  |
|----------|-----------------------------------|--------------------------|
| IP       | Identifica a máquina              | 192.168.56.10            |
| Porta    | Identifica o serviço              | :8080                    |
| DNS      | Traduz nome em IP                 | google.com               |
| HTTP     | Protocolo de comunicação web      | http://localhost         |
| HTTPS    | HTTP com criptografia             | https://site.com         |
| SSH      | Acesso remoto seguro a servidores | ssh devops@192.168.56.10 |

---

## ➡️ Próximo passo

👉 Abra `02-pratica.md` e execute os comandos na VM.