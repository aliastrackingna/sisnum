# SisNum - Controle de Numeração de Documentos

Aplicação Django para controle sequencial de numeração de documentos administrativos.

## Tech Stack

- **Backend**: Django 6.0.2 + Gunicorn
- **Frontend**: HTML + Bootstrap 5
- **Web Server**: Nginx com Gzip e Rate Limiting
- **Container**: Docker + Docker Compose

## Recursos de Segurança

- Rate Limiting: 10 requisições/minuto por IP
- Gzip compression para transferência otimizada
- Headers de segurança (CSP, X-Frame-Options, X-Content-Type-Options)
- Usuário não-root nos containers
- Health checks configurados
- Restart automático em caso de falha

## Instalação no Portainer

### Pré-requisitos

- Docker instalado
- Portainer CE instalado e acessível

### Variáveis de Ambiente

No Portainer, você pode passar as variáveis diretamente na seção "Environment" do stack:

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SECRET_KEY` | Chave secreta do Django (mínimo 50 caracteres) | `sua-chave-aqui...` |
| `DEBUG` | Modo debug (True/False) | `False` |
| `ALLOWED_HOSTS` | Hosts permitidos (separados por vírgula) | `localhost,127.0.0.1,seu-dominio.com` |
| `NGINX_PORT` | Porta do Nginx | `80` |

### Método 1: Usando Stacks (Recomendado)

1. Acesse o Portainer
2. Vá em **Stacks** > **Add stack**
3. Selecione **Web editor**
4. Copie e cole o conteúdo do arquivo `docker-compose.yml`
5. Na seção **Environment variables**, adicione:
   - Clique em "Add environment variable"
   - Adicione cada variável da tabela acima
   - Em **name**: `SECRET_KEY`, **value**: sua chave
   - Repita para as outras variáveis
6. Clique em **Deploy the stack**

**Nota**: Não é necessário criar arquivo `.env` local, as variáveis são passadas diretamente no Portainer.

### Método 2: Usando Git Repository

1. Faça push do projeto para um repositório Git (GitHub, GitLab, etc.)
2. No Portainer, vá em **Stacks** > **Add stack**
3. Selecione **Git repository**
4. Preencha:
   - **Repository URL**: URL do seu repositório
   - **Repository reference**: `refs/heads/master`
   - **Compose path**: `docker-compose.yml`
5. Em "Environment", adicione as variáveis de ambiente
6. Clique em **Deploy the stack**

### Método 3: Build Local + Upload

1. Faça build da imagem localmente:
   ```bash
   docker build -t sisnum .
   ```

2. Tag a imagem:
   ```bash
   docker tag sisnum seu-registry/sisnum:latest
   ```

3. Push para seu registry:
   ```bash
   docker push seu-registry/sisnum:latest
   ```

4. No Portainer, vá em **Images** > **Import**
5. Importe o arquivo .tar ou use o registry

6. Depois crie um stack manualmente com compose

## Primeiro Acesso

Um superusuário padrão é criado automaticamente na primeira execução:

- **Usuário**: `admin`
- **Senha**: `admin`

> **IMPORTANTE**: Altere a senha padrão imediatamente após o primeiro login. Acesse `/admin/` e vá em **Alterar senha** ou use o comando:
> ```bash
> docker-compose exec web python manage.py changepassword admin
> ```

## Acessando a Aplicação

Após deploy, a aplicação estará disponível em:
- `http://seu-servidor:80/` (ou porta configurada)

## Comandos Úteis

### Ver logs
```bash
docker logs sisnum-web-1
docker logs sisnum-nginx-1
```

### Rebuild após alterações
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Executar migrações
```bash
docker-compose exec web python manage.py migrate
```

### Criar superusuário
```bash
docker-compose exec web python manage.py createsuperuser
```

### Coletar static files
```bash
docker-compose exec web python manage.py collectstatic --noinput
```

## Estrutura dos Containers

```
┌─────────────────────────────────────────────┐
│              Nginx (Porta 80)               │
│  - Rate Limiting (10 req/min)              │
│  - Gzip Compression                         │
│  - Security Headers                        │
│  - Serve Static/Media                      │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│         Gunicorn + Django (Porta 8000)      │
│  - WSGI Application                         │
│  - 3 Workers                                │
│  - Health Check                             │
└─────────────────────────────────────────────┘
```

## Troubleshooting

### Container não inicia
- Verifique os logs: `docker-compose logs web`
- Confirme que o `.env` está configurado corretamente

### Erro 502 Bad Gateway
- Verifique se o container web está saudável: `docker-compose ps`
- Check os logs do nginx: `docker-compose logs nginx`

### Rate Limit excedido
- Aguarde 1 minuto (limite zera)
- Ou ajuste em `nginx/nginx.conf`

## Licença

MIT
