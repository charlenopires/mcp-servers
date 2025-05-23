# Guia de Instalação MCP Servers

## 📋 Requisitos do Sistema

Antes de instalar o MCP Servers, certifique-se de que seu sistema atende aos seguintes requisitos:

- Python 3.8 ou superior
- uv (Universal Python Package Manager)
- Git (para clonar o repositório)
- 500MB de espaço em disco para o projeto e suas dependências
- Conexão com internet (para instalação dos pacotes)

## 🚀 Instalação Rápida

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/user/mcp-servers.git
cd mcp-servers
```

### Passo 2: Instalar Dependências

#### Usando pip

```bash
pip install -r requirements.txt
```

#### Usando uv (Recomendado)

```bash
# Instalar uv se ainda não estiver instalado
pip install uv

# Instalar dependências com uv
uv pip install -r requirements.txt
```

### Passo 3: Verificar a Instalação

```bash
python run_tests.py --verify-install
```

Este comando executará um teste rápido para verificar se todas as dependências foram instaladas corretamente.

## 🔧 Instalação Avançada

### Instalação com Ambientes Virtuais

Recomendamos o uso de ambientes virtuais para isolamento de dependências:

#### Usando venv

```bash
# Criar ambiente virtual
python -m venv mcp-env

# Ativar ambiente virtual
# No macOS/Linux
source mcp-env/bin/activate
# No Windows
mcp-env\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

#### Usando Conda

```bash
# Criar ambiente conda
conda create -n mcp-env python=3.10
conda activate mcp-env

# Instalar dependências
pip install -r requirements.txt
```

### Instalação em Modo Desenvolvimento

Para contribuidores e desenvolvedores que desejam modificar o código:

```bash
# Instalar em modo desenvolvimento
pip install -e .

# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt
```

## 📦 Dependências Principais

O projeto MCP Servers utiliza as seguintes bibliotecas principais:

| Biblioteca | Versão   | Descrição                                        |
| ---------- | -------- | ------------------------------------------------ |
| FastMCP    | >=0.6.0  | Framework para desenvolvimento de servidores MCP |
| Pydantic   | >=2.0.0  | Validação de dados e configurações               |
| Typer      | >=0.9.0  | Interfaces de linha de comando                   |
| Rich       | >=13.0.0 | Formatação rica de texto em terminal             |
| Pytest     | >=7.0.0  | Framework de testes                              |

## 🔍 Solução de Problemas de Instalação

### Erros Comuns

#### 1. Erro na instalação de dependências

**Problema:**

```
ERROR: Could not find a version that satisfies the requirement fastmcp>=0.6.0
```

**Solução:**
Verifique se você está usando uma versão compatível do Python (3.8+) e se seu pip está atualizado:

```bash
python --version
pip --version
pip install --upgrade pip
```

#### 2. Conflitos de versão

**Problema:**

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed...
```

**Solução:**
Use um ambiente virtual limpo para evitar conflitos:

```bash
python -m venv fresh-env
source fresh-env/bin/activate
pip install -r requirements.txt
```

#### 3. Problemas com uv

**Problema:**
Erros ao instalar pacotes com uv

**Solução:**
Verifique se você tem a versão mais recente do uv:

```bash
pip install --upgrade uv
```

### Verificação Manual de Dependências

Para verificar manualmente se todas as dependências estão instaladas corretamente:

```bash
# Criar script de verificação temporário
echo "import sys; import pkg_resources; [pkg_resources.get_distribution(p.strip()) for p in open('requirements.txt') if not p.startswith('#')]" > check_deps.py

# Executar verificação
python check_deps.py
```

## 🌐 Instalação em Diferentes Sistemas Operacionais

### macOS

#### Pré-requisitos adicionais:

```bash
# Instalar Homebrew (se não estiver instalado)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python e pip
brew install python

# Instalar uv
pip install uv
```

### Linux (Ubuntu/Debian)

#### Pré-requisitos adicionais:

```bash
# Atualizar repositórios
sudo apt update

# Instalar Python e pip
sudo apt install python3 python3-pip python3-venv

# Instalar uv
pip3 install uv
```

### Windows

#### Pré-requisitos adicionais:

1. Baixe e instale Python do [site oficial](https://www.python.org/downloads/windows/)
2. Durante a instalação, marque a opção "Add Python to PATH"
3. Abra o PowerShell ou CMD como administrador:

```powershell
# Instalar uv
pip install uv

# Configurar scripts PowerShell (se necessário)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🔧 Configuração Avançada

### Configuração do Ambiente de Desenvolvimento

Para desenvolvedores que desejam contribuir ou estender os servidores MCP, recomendamos a seguinte configuração:

#### 1. Ambiente de Desenvolvimento VSCode

```bash
# Instalar extensões recomendadas para VSCode
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension matangover.mypy
```

#### 2. Pré-commit Hooks

Instale pre-commit para garantir qualidade de código antes dos commits:

```bash
# Instalar pre-commit
pip install pre-commit

# Configurar hooks
pre-commit install

# Executar manualmente em todos os arquivos
pre-commit run --all-files
```

#### 3. Configuração para Contribuidores

Crie um ambiente de desenvolvimento completo:

```bash
# Clonar repositório com submódulos
git clone --recurse-submodules https://github.com/user/mcp-servers.git
cd mcp-servers

# Criar ambiente virtual dedicado
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows

# Instalar em modo editável com dependências de desenvolvimento
pip install -e ".[dev,test]"
```

### Verificação de Instalação Detalhada

Para verificar se sua instalação está completamente funcional, execute o script de verificação incluído:

```bash
python scripts/verify_installation.py --verbose
```

Este script realiza as seguintes verificações:

1. **Dependências**: Verifica se todas as bibliotecas necessárias estão instaladas
2. **Versões**: Confirma que as versões são compatíveis
3. **Acesso ao Sistema**: Testa permissões de leitura/escrita em diretórios necessários
4. **Conectividade**: Verifica se servidores conseguem se comunicar (se aplicável)
5. **Validação Básica**: Executa testes simples de cada servidor

### Configuração Multi-ambiente

Para trabalhar com diferentes configurações de ambiente:

#### Criando Perfis de Configuração

```bash
# Criar diretório de configurações
mkdir -p configs/{dev,staging,prod}

# Criar arquivos de configuração para cada ambiente
cat > configs/dev/config.env << EOF
MCP_LOG_LEVEL=DEBUG
MCP_SERVER_PORT=8000
EOF

cat > configs/prod/config.env << EOF
MCP_LOG_LEVEL=WARNING
MCP_SERVER_PORT=80
EOF
```

#### Carregando Configurações Específicas

```bash
# Carregar ambiente de desenvolvimento
source configs/dev/config.env
./run_servers.sh

# Ou para produção
source configs/prod/config.env
./run_servers.sh
```

## 📊 Verificação de Requisitos do Sistema

Para garantir que seu sistema atenda todos os requisitos para uma execução ideal dos servidores MCP, execute:

```bash
# Verificar requisitos do sistema
python -c 'from servers.utils.system_check import verify_system; verify_system(verbose=True)'
```

Este comando verifica:

- **Hardware**: Memória disponível, espaço em disco, etc.
- **Sistema Operacional**: Versão e compatibilidade
- **Python**: Versão e configuração
- **Rede**: Disponibilidade de portas necessárias
- **Permissões**: Acesso a diretórios e recursos

---

**Desenvolvido para o projeto MCP Servers**
