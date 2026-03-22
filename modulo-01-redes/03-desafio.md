# 🧩 Aula 03 — Desafio: Rede na Prática

> **Resolva sem consultar o gabarito. Tente primeiro.**
> Gabarito em: `solution/README.md`

---

## 🎯 Objetivo

Aplicar os conceitos de IP, porta, firewall e SSH de forma independente.

---

## 🧪 Desafio 1 — Servidor em porta diferente

Suba o servidor HTTP na porta `9090` (não na 8080):

```bash
# dica: mesmo comando da prática, troca a porta
```

Antes de testar, libere a porta no firewall:

```bash
# dica: mesmo comando da prática, troca o número da porta
```

Confirme que a porta está aberta:

```bash
# dica: use ss com filtro grep
```

---

## 🧪 Desafio 2 — Diagnóstico

Responda as perguntas **executando comandos na VM** (não pesquise):

1. Qual é o IP da sua VM?
2. Quais portas estão abertas agora?
3. Qual processo está usando a porta 9090?
4. O firewall está ativo? Quais regras existem?

---

## 🧪 Desafio 3 — Acesso externo

Com o servidor rodando na porta `9090`:

1. Acesse via `curl` dentro da própria VM:

```bash
# sua resposta aqui
```

2. Acesse via navegador no seu PC:

```
# escreva a URL completa aqui (com IP e porta)
```

---

## 🧪 Desafio 4 — Conteúdo customizado

Crie um arquivo `index.html` com seu nome e suba o servidor:

```html
<!-- exemplo -->
<h1>Seu Nome — DevOps</h1>
<p>Módulo 01 concluído</p>
```

Acesse via navegador e confirme que o conteúdo aparece.

---

## 🧪 Desafio 5 — DNS manual

Execute:

```bash
nslookup github.com
nslookup hub.docker.com
```

Responda:
- Qual o IP do `github.com`?
- Qual o IP do `hub.docker.com`?

---

## 🧪 Desafio 6 — SSH sem senha

Configure a autenticação SSH por chave entre seu PC e a VM:

1. Gere um par de chaves no seu PC (se ainda não tiver):

```bash
# dica: ssh-keygen
```

2. Copie a chave pública para a VM:

```bash
# dica: ssh-copy-id
```

3. Conecte na VM sem digitar senha:

```bash
ssh devops@<IP_DA_VM>
```

4. Configure o arquivo `~/.ssh/config` no seu PC para se conectar com alias:

```bash
# após configurar, o comando deve funcionar:
ssh minha-vm
```

---

## ✅ Critério de conclusão

- [ ] Servidor rodando na porta 9090
- [ ] Porta 9090 liberada no firewall
- [ ] Porta confirmada com `ss`
- [ ] Acesso via `curl` funcionando
- [ ] Acesso via navegador funcionando com HTML customizado
- [ ] DNS resolvido para os dois domínios
- [ ] SSH por chave funcionando sem senha
- [ ] Alias `minha-vm` configurado no `~/.ssh/config`

---

## ➡️ Próximo passo

Confira o gabarito em `solution/README.md`