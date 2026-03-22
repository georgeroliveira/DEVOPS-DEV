# 🧪 Aula 02 — Laboratório: Testando Rede na VM

> **Execute todos os comandos dentro da VM via SSH ou VS Code Remote.**

---

## 🔹 1. Descobrir o IP da VM

```bash
ip a
```

**O que observar:**
- Interface `eth0` ou `enp0s3` → IP da rede VirtualBox
- `127.0.0.1` → localhost (sempre presente)

**Exemplo de saída:**
```
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.56.101/24
```

> Anote o IP da sua VM. Você vai usar nos próximos passos.

---

## 🔹 2. Testar conectividade

```bash
ping -c 4 google.com
```

**O que observar:**
- `time=` → latência em ms
- `0% packet loss` → conexão estável

> Se falhar: sem acesso à internet na VM. Verifique configuração de rede no VirtualBox.

---

## 🔹 3. Testar resolução DNS

```bash
nslookup google.com
```

**Exemplo de saída:**
```
Server:   127.0.0.53
Name:     google.com
Address:  142.250.x.x
```

> DNS funcionando = nome sendo traduzido para IP.

---

## 🔹 4. Fazer requisição HTTP

```bash
curl -I http://example.com
```

**O que observar:**
- `HTTP/1.1 200 OK` → servidor respondeu com sucesso
- Cabeçalhos da resposta

```bash
# Versão completa (retorna o HTML)
curl http://example.com
```

---

## 🔹 5. Ver portas abertas na VM

```bash
ss -tulnp
```

| Flag | Significado      |
|------|------------------|
| -t   | TCP              |
| -u   | UDP              |
| -l   | apenas escutando |
| -n   | mostra números   |
| -p   | mostra processo  |

**Exemplo de saída:**
```
Netid  State   Local Address:Port
tcp    LISTEN  0.0.0.0:22        ← SSH escutando
```

---

## 🔹 6. Verificar o firewall (UFW)

Antes de subir qualquer serviço, verifique o estado do firewall:

```bash
sudo ufw status
```

**Possíveis saídas:**

```
Status: inactive    ← firewall desativado
Status: active      ← firewall ativo, veja as regras abaixo
```

Se o firewall estiver **ativo**, libere a porta que você vai usar:

```bash
# Liberar porta 8080
sudo ufw allow 8080/tcp

# Confirmar que a regra foi criada
sudo ufw status
```

**Exemplo de saída após liberar:**
```
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
8080/tcp                   ALLOW       Anywhere
```

> **Por que isso importa:** se o firewall bloquear a porta, o servidor sobe normalmente
> dentro da VM mas fica inacessível pelo navegador do seu PC.
> Esse é um dos erros mais comuns em ambientes cloud (EC2, Azure VM, GCP).

---

## 🔹 7. Subir um servidor HTTP simples

```bash
mkdir -p ~/lab-redes
cd ~/lab-redes
echo "<h1>Minha VM DevOps</h1>" > index.html
python3 -m http.server 8080
```

> O servidor vai rodar em primeiro plano. Deixe o terminal aberto.

---

## 🔹 8. Testar o servidor

**Em outro terminal na VM:**

```bash
curl http://localhost:8080
```

**No navegador do seu PC:**

```
http://<IP_DA_VM>:8080
```

> Substitua `<IP_DA_VM>` pelo IP que você anotou no passo 1.

**Resultado esperado:**
```html
<h1>Minha VM DevOps</h1>
```

---

## 🔹 9. Verificar a porta do servidor

```bash
ss -tulnp | grep 8080
```

**Resultado esperado:**
```
tcp   LISTEN  0.0.0.0:8080   users:(("python3",...))
```

---

## 🔹 10. Encerrar o servidor

No terminal onde o servidor está rodando:

```
Ctrl + C
```

---

## 🔹 11. Testar conexão SSH na VM

Simule o fluxo que você vai usar durante todo o curso:

```bash
# Do seu PC, conecte na VM via SSH
ssh devops@<IP_DA_VM>

# Confirme que está dentro da VM
hostname
whoami
```

> Esse é o mesmo fluxo de conectar em uma EC2 na AWS ou VM no Azure.
> O VS Code Remote SSH faz exatamente isso por baixo dos panos.

---

## ✅ Checklist do laboratório

- [ ] IP da VM identificado
- [ ] `ping` funcionando
- [ ] DNS resolvendo nomes
- [ ] `curl` retornando resposta HTTP
- [ ] Portas abertas listadas com `ss -tulnp`
- [ ] Firewall verificado com `ufw status`
- [ ] Porta 8080 liberada no firewall
- [ ] Servidor Python subindo na porta 8080
- [ ] Acesso via `curl` funcionando
- [ ] Acesso via navegador funcionando
- [ ] Porta confirmada com `ss | grep 8080`
- [ ] Conexão SSH testada do PC para a VM

---

## ➡️ Próximo passo

👉 Abra `03-desafio.md` e resolva o desafio.