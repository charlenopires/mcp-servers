# React Optimizer Server - Guia de Uso Rápido

## 🚀 Início Rápido

### 1. Executar o Servidor

```bash
# Usando o launcher principal
python main.py react_optimizer

# Usando o script shell
./run_servers.sh react_optimizer

# Execução direta
uv run python -m servers.react_optimizer_server
```

### 2. Configurar no Claude Desktop

Adicione ao seu arquivo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "react-optimizer": {
      "command": "uv",
      "args": ["run", "python", "-m", "servers.react_optimizer_server"],
      "cwd": "/caminho/para/mcp-servers"
    }
  }
}
```

### 3. Exemplos de Uso

#### Analisar Componente React

```python
# Componente simples
code = """function Button({ children, onClick }) {
    return <button onClick={onClick}>{children}</button>
}"""

# Análise automática com score e recomendações
result = await analyze_react_code(code=code, component_type="component")
```

#### Otimizar Código React

```python
# Aplicar tendências 2025 automaticamente
result = await optimize_react_code(
    code=code,
    focus_areas=["accessibility", "performance", "trends"]
)
```

#### Otimizar Prompts para AI

```python
# Transformar prompt básico em versão otimizada
result = await optimize_react_prompt(
    prompt="Create a contact form",
    target_ai_tool="v0_dev",
    include_accessibility=True
)
```

## 🛠️ Ferramentas Disponíveis

1. **`analyze_react_code`** - Análise de código React existente
2. **`optimize_react_code`** - Otimização automática de componentes
3. **`analyze_react_prompt`** - Análise de qualidade de prompts
4. **`optimize_react_prompt`** - Otimização de prompts para AI tools
5. **`generate_react_workflow`** - Geração de workflows de desenvolvimento
6. **`get_react_best_practices`** - Melhores práticas React 2025
7. **`validate_react_integration`** - Validação de integração de componentes

## 📚 Documentação Completa

- **Documentação Detalhada**: `docs/servers/react_optimizer_server.md`
- **Exemplos Práticos**: `docs/examples/react_optimizer_examples.py`
- **Configuração Claude**: `claude_desktop_config_example.json`

## 🎯 Recursos Especiais

### Tendências UI/UX 2025

- Glassmorphism e dark mode nativo
- Micro-animações e elementos 3D
- Design sustentável e acessível
- Personalização por IA

### Integração com AI Tools

- **v0.dev**: Prompts específicos para Vercel
- **Cursor**: Context-aware development
- **GitHub Copilot**: Enhanced suggestions
- **Visual Copilot**: Figma to React

### Stack Moderno Suportado

- React 18+ com hooks modernos
- TypeScript como padrão
- Tailwind CSS + shadcn/ui
- Next.js 14+ e Vite
- Framer Motion para animações

## 💡 Casos de Uso

- **Refatoração**: Modernizar código React legado
- **Development**: Prompts otimizados para AI tools
- **Code Review**: Análise automática de componentes
- **Mentoria**: Sugestões educativas de melhoria
- **Padronização**: Aplicação uniforme de melhores práticas

## 🔧 Comandos Úteis

```bash
# Listar todos os servidores
python main.py list

# Executar exemplos
python docs/examples/react_optimizer_examples.py

# Executar em modo desenvolvimento
python main.py react_optimizer --dev

# Executar todos os servidores
python main.py all
```
