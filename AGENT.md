# Projeto: Controle de Numeração de Documentos (DocCounter)

## Visão Geral
Criar uma aplicação web simples usando **Django** e **SQLite** para controlar a numeração sequencial de documentos administrativos (Memorandos, Circulares, Ofícios, etc.).

O objetivo é substituir o controle manual. A interface deve ser "Single Page" (tudo em uma única tela), focada em utilidade e simplicidade.

## Stack Tecnológico
- **Backend:** Python, Django.
- **Banco de Dados:** SQLite (padrão do Django).
- **Frontend:** HTML simples com Bootstrap (via CDN) para estilização rápida.
- **Javascript:** Mínimo necessário (opcional, pode ser feito apenas com Django Forms/Views).

## Requisitos Funcionais

### 1. Gerenciamento de Tipos de Documento
- O sistema deve permitir cadastrar novos tipos de documentos dinamicamente (ex: "Memorando", "Ofício", "Circular").
- Deve exibir uma lista de todos os tipos cadastrados.

### 2. Controle de Numeração
- Para cada tipo de documento, mostrar o **Número Atual**.
- Deve haver um botão ou link fácil ("+ Próximo") ao lado de cada documento que incrementa o número em +1 imediatamente.
- O sistema deve mostrar qual será o próximo número disponível.

### 3. Zerar Numeração (Virada de Ano)
- Deve haver uma opção (botão de perigo/atenção) para "Zerar Todas as Numerações".
- Ao clicar, todos os contadores voltam para 0 ou 1 (definir como 0 para que o próximo seja 1).

### 4. Interface (UI)
- **Painel Único:** Todas as ações (listar, adicionar, incrementar, zerar) devem acontecer na rota raiz `/`.
- **Layout:**
  - Topo: Título e botão "Zerar Tudo".
  - Centro: Tabela com colunas [Tipo de Documento | Último Número | Ação (+1)].
  - Fundo: Pequeno formulário para adicionar um novo tipo.

## Estrutura de Dados (Modelos)

Sugestão de `models.py`:

```python
class TipoDocumento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    ultimo_numero = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome