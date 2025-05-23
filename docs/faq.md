# Perguntas Frequentes (FAQ)

## 📋 Perguntas Gerais

### O que é o MCP (Model Context Protocol)?

O MCP (Model Context Protocol) é um protocolo que permite estender modelos de linguagem com ferramentas personalizadas. Ele define padrões para como os modelos interagem com ferramentas externas, permitindo a criação de servidores especializados que fornecem funcionalidades adicionais aos modelos.

### Quais são os principais servidores MCP neste projeto?

O projeto MCP Servers contém três servidores principais:

1. **Analisador de Prompts MCP**: Avalia a qualidade dos prompts para criação de servidores MCP
2. **Servidor de Engenharia de Prompts**: Otimiza prompts usando estratégias avançadas
3. **Servidor Tailwind CSS v4.1**: Fornece suporte para desenvolvimento com Tailwind CSS v4.1

### Quais são os requisitos mínimos para executar os servidores?

- **Sistema Operacional**: Windows, macOS ou Linux
- **Python**: Versão 3.8 ou superior
- **Espaço em Disco**: Aproximadamente 500MB para o projeto e dependências
- **Memória**: Mínimo de 2GB RAM (4GB recomendado)
- **Dependências**: Conforme listado no arquivo `requirements.txt`

### Posso usar os servidores em projetos comerciais?

Sim, o projeto é licenciado sob a Licença MIT, o que permite uso comercial. Consulte o arquivo `LICENSE` para mais detalhes.

## 🔧 Perguntas Técnicas

### Como posso executar todos os servidores ao mesmo tempo?

Use o script launcher interativo incluído no projeto:

```bash
./run_servers.sh
```

Quando solicitado, digite `all` para iniciar todos os servidores ou selecione servidores específicos digitando seus números (ex: `1 3`).

### Os servidores podem ser acessados remotamente?

Por padrão, os servidores são configurados para aceitar conexões apenas de localhost (127.0.0.1). Para permitir acesso remoto, você precisaria:

1. Modificar a configuração para escutar em todas as interfaces (0.0.0.0)
2. Implementar autenticação adequada
3. Considerar o uso de HTTPS

Observe que abrir os servidores para acesso remoto requer medidas adicionais de segurança.

### Como posso integrar os servidores em minha aplicação existente?

Você pode integrar os servidores MCP de várias maneiras:

1. **Importação direta**: Importe as classes Python em seu código
2. **API HTTP**: Configure os servidores com endpoints HTTP e faça requisições
3. **Biblioteca compartilhada**: Use os componentes principais como biblioteca

Consulte o [Guia de Integração](guides/integration_guide.md) para exemplos detalhados.

### É possível estender os servidores com funcionalidades personalizadas?

Sim, todos os servidores foram projetados para serem extensíveis. Você pode:

1. Adicionar novas ferramentas MCP
2. Estender classes existentes
3. Criar servidores derivados com funcionalidades adicionais

Consulte a [Arquitetura](architecture.md) para entender os pontos de extensão.

## 🚀 Uso e Funcionalidades

### Como o Analisador de Prompts MCP avalia a qualidade dos prompts?

O Analisador de Prompts MCP avalia prompts em 10 critérios principais:

1. Propósito Claro (15%)
2. Design de Ferramentas (15%)
3. Tratamento de Erros (12%)
4. Documentação (10%)
5. Segurança (10%)
6. Esquema de Dados (10%)
7. Eficiência (8%)
8. Extensibilidade (8%)
9. Convenções MCP (7%)
10. Testes (5%)

Cada critério é avaliado usando análise de texto e padrões, resultando em uma pontuação geral de 1 a 10.

### Qual a diferença entre o Analisador MCP e o Engenheiro de Prompts?

- **Analisador de Prompts MCP**: Foca em avaliar a qualidade de prompts para criação de servidores MCP, identificando pontos fortes e fracos.
- **Engenheiro de Prompts**: Concentra-se em otimizar prompts, aplicando estratégias específicas e técnicas de melhorias.

Embora complementares, eles têm propósitos distintos. O Analisador diagnostica enquanto o Engenheiro aprimora.

### O que há de novo no Tailwind CSS v4.1 e como o servidor ajuda?

O Tailwind CSS v4.1 traz diversas novidades como:

- Novo sistema de cores
- API de plugins aprimorada
- Componentes nativos
- Otimizações de desempenho

O Servidor Tailwind CSS v4.1 ajuda com:

1. Resumo das mudanças principais
2. Conversão de código da v3 para v4.1
3. Otimização de classes
4. Geração de componentes seguindo as melhores práticas da v4.1

### Como posso verificar se meu prompt MCP está seguindo as melhores práticas?

Utilize o Analisador de Prompts MCP:

```python
from servers.mcp_server import AnalisadorPromptMCP

analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt(
    "Seu prompt aqui"
)

print(f"Pontuação: {resultado['pontuacao']}/10")
print("Pontos a melhorar:")
for ponto in resultado['pontos_fracos']:
    print(f"- {ponto}")
```

## 🔍 Solução de Problemas

### Os servidores estão lentos para iniciar. Como posso acelerar?

A lentidão na inicialização pode ser causada por diversos fatores:

1. **Primeira execução**: A primeira inicialização é mais lenta devido ao carregamento de recursos
2. **Recursos limitados**: Verifique a memória disponível e uso de CPU
3. **Conflitos**: Outros processos podem estar interferindo

Soluções:

- Use a opção `--preload` no launcher para pré-carregar recursos
- Desative servidores desnecessários
- Verifique e feche aplicações que consomem muitos recursos

### Estou recebendo erros ao executar os testes. O que fazer?

Se os testes estão falhando:

1. Verifique se todas as dependências estão instaladas:

   ```bash
   pip install -r requirements.txt
   ```

2. Confirme que você está usando a versão correta de Python:

   ```bash
   python --version
   ```

3. Execute apenas os testes problemáticos para diagnóstico:

   ```bash
   python -m pytest tests/test_specific_file.py -v
   ```

4. Verifique os logs para erros específicos:
   ```bash
   cat logs/test_*.log
   ```

### Como posso contribuir para o projeto?

Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-ferramenta`)
3. Faça suas alterações seguindo as convenções do projeto
4. Execute os testes para garantir que tudo funciona
5. Envie um Pull Request com uma descrição detalhada

Consulte o arquivo `CONTRIBUTING.md` para diretrizes completas.

---

**Desenvolvido para o projeto MCP Servers**
