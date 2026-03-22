# 🧩 Aula 03 — Desafio: Linux na Prática

> **Resolva sem consultar o gabarito. Tente primeiro.**  
> Gabarito em: `solution/README.md`

---

## 🎯 Objetivo

Aplicar de forma independente tudo que foi visto no módulo — usuários, permissões, serviços, logs e automação.

---

## 🧪 Desafio 1 — Novo usuário com restrições

Crie um usuário chamado `auditor` com as seguintes características:

- Deve ter diretório home
- Não deve ter acesso ao sudo
- Deve pertencer a um grupo chamado `auditoria`
- Deve conseguir fazer login via SSH com chave (não senha)

```bash
# Escreva os comandos aqui
```

**Critério:** `id auditor` deve mostrar o grupo `auditoria` e `groups auditor` não deve incluir `sudo`.

---

## 🧪 Desafio 2 — Estrutura de projeto com permissões

Crie a seguinte estrutura em `/opt/projeto/`:

```
/opt/projeto/
├── app/         → dono: deploy, permissão: 755
├── config/      → dono: deploy, permissão: 750
├── logs/        → dono: deploy, permissão: 755
└── secrets/     → dono: deploy, permissão: 700
```

**Critério:** `ls -la /opt/projeto/` deve mostrar as permissões e donos corretos.

---

## 🧪 Desafio 3 — Script de setup do servidor

Crie um script `/opt/projeto/setup.sh` que execute automaticamente:

1. Atualiza a lista de pacotes
2. Instala `curl`, `git` e `htop` se não estiverem instalados
3. Cria o usuário `deploy` se não existir
4. Cria o diretório `/opt/app` se não existir
5. Imprime `Setup concluído em: <data e hora>` ao final

```bash
#!/bin/bash
# escreva o script aqui
```

**Critério:** o script deve ser idempotente — executar 2 vezes seguidas deve dar o mesmo resultado sem erros.

---

## 🧪 Desafio 4 — Diagnóstico de serviço

O nginx foi parado propositalmente:

```bash
sudo systemctl stop nginx
```

Sem iniciar o nginx manualmente, descubra e execute:

1. Qual comando confirma que o nginx está parado?
2. Qual comando mostra os últimos logs do nginx?
3. Qual comando inicia o nginx E garante que vai subir no próximo boot?
4. Como confirmar que está acessível externamente?

```bash
# Suas respostas aqui
```

---

## 🧪 Desafio 5 — Análise de logs

Execute os comandos abaixo e responda as perguntas:

```bash
# Gerar algumas requisições
for i in {1..10}; do curl -s http://localhost > /dev/null; done
curl http://localhost/rota-inexistente
```

Responda usando comandos (não pesquise, execute):

1. Quantas requisições chegaram ao nginx nos últimos 5 minutos?
2. Houve algum erro 404? Em qual rota?
3. Qual o tamanho atual do arquivo de log do nginx?

```bash
# Seus comandos aqui
```

---

## 🧪 Desafio 6 — Script de monitoramento avançado

Melhore o script `healthcheck.sh` do laboratório adicionando:

1. Verificação de uso de disco — alerta se passar de 80%
2. Verificação de uso de memória — alerta se passar de 80%
3. Teste de conectividade HTTP — verifica se `http://localhost` responde 200
4. Salva o resultado em `/opt/app/logs/healthcheck.log` com timestamp

```bash
#!/bin/bash
# escreva o script melhorado aqui
```

**Critério:** executar o script deve produzir saída formatada com ✅ para OK e ❌ para problema.

---

## 🧪 Desafio 7 — Crontab de manutenção

Configure o crontab do usuário `deploy` com as seguintes tarefas:

| Tarefa | Frequência |
|---|---|
| Executar `healthcheck.sh` | A cada 5 minutos |
| Limpar logs antigos de `/opt/app/logs/` | Todo dia às 02:00 |
| Fazer `apt update` | Todo domingo às 03:00 |

```bash
# Escreva as linhas do crontab aqui
```

---

## ✅ Critério de conclusão

- [ ] Usuário `auditor` criado sem sudo, no grupo `auditoria`
- [ ] Estrutura `/opt/projeto/` com permissões corretas
- [ ] Script `setup.sh` idempotente funcionando
- [ ] Nginx diagnosticado, reiniciado e habilitado no boot
- [ ] Análise de logs executada com comandos
- [ ] Script `healthcheck.sh` melhorado com alertas
- [ ] Crontab com as 3 tarefas configuradas

---

## ➡️ Próximo passo

Confira o gabarito em `solution/README.md`