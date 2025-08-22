# CYBERDECK AUTOMATION TOOLS

## 🚀 Visão Geral

Este projeto contém ferramentas Python para gerar animações ASCII e automatizar atualizações do GitHub com estética cyberpunk.

## 📁 Estrutura dos Arquivos

```
tools/
├── cyberdeck.py        # 🎮 Interface principal - dashboard interativo
├── auto_github.py      # 🤖 Automação do GitHub
├── divider_gen.py      # 🎨 Gerador de divisores ASCII
├── scanner_sim.py      # 📡 Simulador de scanner cyberpunk
└── update_readme.py    # 📝 Atualizador do README.md
```

## 🎯 Como Usar

### 1. Dashboard Principal (Recomendado)
```bash
python tools/cyberdeck.py
```
Interface interativa com todas as funcionalidades.

### 2. Automação do GitHub
```bash
# Modo interativo
python tools/auto_github.py

# Atualização direta
python tools/auto_github.py --update

# Verificar status
python tools/auto_github.py --status
```

### 3. Ferramentas Individuais

#### Gerador de ASCII
```bash
# Demo completo
python tools/divider_gen.py

# Estilo específico
python tools/divider_gen.py glitch
python tools/divider_gen.py matrix
python tools/divider_gen.py waves
python tools/divider_gen.py blocks
```

#### Scanner Cyberpunk
```bash
# Demo completo
python tools/scanner_sim.py

# Scans específicos
python tools/scanner_sim.py system
python tools/scanner_sim.py network
python tools/scanner_sim.py security

# Status board
python tools/scanner_sim.py --status
```

#### Atualizar README
```bash
# Demo das animações
python tools/update_readme.py --demo

# Adicionar marcadores ao README
python tools/update_readme.py --add-markers

# Atualizar README com novo conteúdo
python tools/update_readme.py --update
```

## ⚙️ Configuração Inicial

### 1. Configurar o README
```bash
python tools/cyberdeck.py
# Escolha opção [5] para adicionar marcadores
```

### 2. Testar as animações
```bash
python tools/cyberdeck.py
# Escolha opção [4] para demo completo
```

### 3. Configurar Git (se necessário)
```bash
git config user.name "Seu Nome"
git config user.email "seu@email.com"
git remote add origin https://github.com/usuario/repo.git
```

## 🤖 Automação

### Atualização Manual
```bash
python tools/auto_github.py --update
```

### Automação com Task Scheduler (Windows)
1. Abra o Task Scheduler
2. Crie uma nova tarefa
3. Configure para executar:
   ```
   python "C:\caminho\para\projeto\tools\auto_github.py" --schedule
   ```

### Automação com Cron (Linux/Mac)
```bash
# Atualizar a cada hora
0 * * * * cd /caminho/para/projeto && python tools/auto_github.py --schedule

# Atualizar diariamente às 9h
0 9 * * * cd /caminho/para/projeto && python tools/auto_github.py --schedule
```

## 🎨 Personalização

### Novos Estilos ASCII
Edite `divider_gen.py` e adicione novos estilos na função `make_divider()`:

```python
elif style == "novo_estilo":
    chars = ["!", "@", "#", "$", "%"]
    weights = [20, 20, 20, 20, 20]
```

### Novos Perfis de Scanner
Edite `scanner_sim.py` e adicione em `SCAN_PROFILES`:

```python
"custom": [
    "Inicializando processo customizado",
    "Verificando parâmetros",
    "Executando operação"
]
```

### Modificar README
Os marcadores no README permitem atualizações automáticas:
- `<!-- DIVIDER_START -->` ... `<!-- DIVIDER_END -->`
- `<!-- SCANNER_START -->` ... `<!-- SCANNER_END -->`
- `<!-- LAST_UPDATE -->` ... `<!-- /LAST_UPDATE -->`

## 🚨 Solução de Problemas

### Erro: "Not a git repository"
```bash
git init
git remote add origin https://github.com/usuario/repo.git
```

### Erro: "No changes to commit"
O README já está atualizado. Use `--demo` para ver as animações.

### Erro de importação
Certifique-se de estar no diretório correto:
```bash
cd /caminho/para/VertigoFromOuterSpace
python tools/cyberdeck.py
```

## 🎮 Comandos Rápidos

```bash
# Setup completo
python tools/cyberdeck.py --setup
python tools/cyberdeck.py --update

# Ver demo
python tools/cyberdeck.py --demo

# Atualizar GitHub
python tools/auto_github.py --update
```

## 🌟 Features

- ✅ Geração de ASCII art em múltiplos estilos
- ✅ Simulação de scanner cyberpunk animado
- ✅ Atualização automática do README.md
- ✅ Integração com Git/GitHub
- ✅ Interface interativa
- ✅ Timestamps automáticos
- ✅ Configuração flexível
- ✅ Suporte a automação

---

**🚀 CYBERDECK v3.14 - VERTIGO FROM OUTER SPACE 👾**
