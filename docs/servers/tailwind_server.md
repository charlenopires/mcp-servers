# Servidor Tailwind CSS v4.1

## 📋 Visão Geral

O Servidor Tailwind CSS v4.1 é uma implementação MCP (Model Context Protocol) especializada em fornecer contexto, assistência e orientações para desenvolvimento com a versão 4.1 do Tailwind CSS. O servidor fornece informações atualizadas sobre novas funcionalidades, migração de versões anteriores e exemplos de uso.

![Tailwind CSS v4.1](../assets/tailwind_server.png)

## 🎯 Propósito

Este servidor foi desenvolvido para facilitar o desenvolvimento com o Tailwind CSS v4.1, fornecendo um contexto especializado para prompts relacionados ao framework. O servidor ajuda a manter o conhecimento atualizado sobre as últimas mudanças, boas práticas e soluções para problemas comuns.

## 🛠️ Ferramentas Disponíveis

### 1. `obter_novidades_tailwind`

**Descrição:** Fornece informações sobre as novas funcionalidades e mudanças no Tailwind CSS v4.1.

**Entradas:**

- `categoria` (string, opcional): Categoria específica de mudanças (configuração, utilidades, plugins, etc.)
- `formato` (string, opcional): Formato da resposta (resumo, detalhado, comparativo)

**Saídas:**

- `novidades` (dict): Descrição detalhada das novas funcionalidades
- `alteracoes_importantes` (list): Mudanças que podem quebrar compatibilidade
- `exemplos` (dict): Exemplos de uso para as novas funcionalidades
- `recursos` (list): Links e recursos adicionais

**Exemplo de Uso:**

```python
novidades = tailwind_server.obter_novidades_tailwind(
    categoria="configuração",
    formato="comparativo"
)
```

### 2. `converter_codigo_tailwind`

**Descrição:** Converte código Tailwind de versões anteriores para a versão 4.1.

**Entradas:**

- `codigo` (string): Código HTML/JSX com classes Tailwind para converter
- `versao_origem` (string, opcional): Versão de origem do código (default: 3.x)
- `incluir_comentarios` (boolean, opcional): Se deve incluir comentários explicativos

**Saídas:**

- `codigo_convertido` (string): Código com classes atualizadas para v4.1
- `alteracoes` (list): Lista de alterações realizadas
- `notas` (list): Notas explicativas sobre as alterações
- `problemas` (list): Possíveis problemas ou incompatibilidades

**Exemplo de Uso:**

```python
resultado = tailwind_server.converter_codigo_tailwind(
    codigo='<div class="bg-gray-100 p-4 shadow-md">Conteúdo</div>',
    incluir_comentarios=True
)
```

### 3. `otimizar_classes_tailwind`

**Descrição:** Otimiza o uso de classes Tailwind para tornar o código mais limpo e eficiente.

**Entradas:**

- `codigo` (string): Código HTML/JSX com classes Tailwind para otimizar
- `nivel_otimizacao` (string, opcional): Nível de otimização (básico, intermediário, avançado)
- `preservar_comentarios` (boolean, opcional): Se deve preservar comentários existentes

**Saídas:**

- `codigo_otimizado` (string): Código com classes otimizadas
- `otimizacoes` (list): Lista de otimizações realizadas
- `metricas` (dict): Métricas de melhoria (redução de tamanho, legibilidade, etc.)
- `recomendacoes` (list): Recomendações adicionais

**Exemplo de Uso:**

```python
otimizado = tailwind_server.otimizar_classes_tailwind(
    codigo='<div class="pt-4 pr-4 pb-4 pl-4 text-blue-500 text-opacity-75">Texto</div>',
    nivel_otimizacao="intermediário"
)
```

### 4. `gerar_componentes_tailwind`

**Descrição:** Gera componentes utilizando Tailwind CSS v4.1 com base em descrições ou requisitos.

**Entradas:**

- `descricao` (string): Descrição do componente desejado
- `framework` (string, opcional): Framework de UI (React, Vue, Angular, HTML)
- `estilo` (string, opcional): Estilo visual desejado (minimal, corporate, playful, etc.)
- `responsivo` (boolean, opcional): Se o componente deve ser responsivo

**Saídas:**

- `codigo` (string): Código do componente gerado
- `preview_url` (string, opcional): URL para preview do componente (se disponível)
- `variacoes` (list, opcional): Variações do componente
- `notas_implementacao` (string): Observações sobre a implementação

**Exemplo de Uso:**

```python
componente = tailwind_server.gerar_componentes_tailwind(
    descricao="Card de produto com imagem, título, preço e botão de compra",
    framework="React",
    responsivo=True
)
```

## 📊 Principais Novidades do Tailwind CSS v4.1

O servidor mantém informações atualizadas sobre as principais mudanças na versão 4.1:

| Categoria             | Mudança                 | Detalhes                                              |
| --------------------- | ----------------------- | ----------------------------------------------------- |
| **Configuração**      | CSS nativo              | Configuração agora usa CSS ao invés de JavaScript     |
| **Sistema de Cores**  | Novas paletas           | Sistema de cores expandido com novas paletas          |
| **Utilitários**       | Novos utilitários       | Adição de novos utilitários para layouts complexos    |
| **Container Queries** | Suporte nativo          | Suporte integrado para container queries              |
| **Variantes**         | Novas variantes         | Novas variantes para estados e condições              |
| **Animações**         | Sistema avançado        | Sistema de animações aprimorado                       |
| **Performance**       | Compilação otimizada    | Melhorias significativas na performance de compilação |
| **Editor**            | IntelliSense aprimorado | Melhor suporte em editores com autocomplete           |
| **Plugins**           | Nova API                | API de plugins redesenhada                            |

## 🔄 Migração de Versões Anteriores

O servidor fornece orientações detalhadas para migração de versões anteriores do Tailwind:

### Principais Alterações de Compatibilidade

1. **Configuração em CSS**

   - Antes: Arquivo `tailwind.config.js`
   - Agora: Configuração diretamente no CSS

2. **Novas Nomenclaturas de Classes**

   - Alterações em nomes de classes para maior consistência
   - Novos prefixos para algumas funcionalidades

3. **Sistema de Plugins**

   - Nova API para criação de plugins
   - Plugins existentes precisam ser atualizados

4. **Build System**
   - Mudanças no processo de compilação
   - Novas opções de configuração

## 🧪 Testes

Os testes para o Servidor Tailwind CSS v4.1 estão disponíveis em `/tests/test_tailwind_server.py` e incluem casos para conversão, otimização e geração de componentes.

## 📝 Exemplos Completos

### Exemplo 1: Conversão de Código

```python
# Código da versão anterior
codigo_antigo = """
<nav class="bg-gray-800 shadow-lg">
  <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <img class="h-8 w-auto" src="/logo.svg" alt="Logo">
      </div>
      <div class="hidden sm:ml-6 sm:flex sm:items-center">
        <div class="px-3 py-2 rounded-md text-sm font-medium text-white bg-gray-900">
          Dashboard
        </div>
      </div>
    </div>
  </div>
</nav>
"""

# Conversão para v4.1
resultado = tailwind_server.converter_codigo_tailwind(
    codigo=codigo_antigo,
    incluir_comentarios=True
)

# Resultado contém o código convertido:
# <nav class="bg-slate-800 shadow-xl"> <!-- Alterado: gray-800 → slate-800, shadow-lg → shadow-xl -->
#   <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
#     <div class="flex justify-between h-16">
#       <div class="flex items-center">
#         <img class="h-8 w-auto" src="/logo.svg" alt="Logo">
#       </div>
#       <div class="hidden sm:ml-6 sm:flex sm:items-center">
#         <div class="px-3 py-2 rounded-md text-sm font-medium text-white bg-slate-900"> <!-- Alterado: gray-900 → slate-900 -->
#           Dashboard
#         </div>
#       </div>
#     </div>
#   </div>
# </nav>
```

### Exemplo 2: Geração de Componente

````python
# Solicitar geração de componente
componente = tailwind_server.gerar_componentes_tailwind(
    descricao="Modal de confirmação com título, mensagem e botões de confirmar/cancelar",
    framework="React",
    estilo="minimal"
)

# Resultado contém o código do componente:
# ```jsx
# import { useState } from 'react';
#
# export default function ConfirmationModal({ isOpen, onClose, onConfirm, title, message }) {
#   if (!isOpen) return null;
#
#   return (
#     <div className="fixed inset-0 bg-black/25 backdrop-blur-sm flex items-center justify-center p-4">
#       <div className="bg-white rounded-xl shadow-2xl max-w-md w-full p-6 animate-in fade-in duration-300">
#         <h2 className="text-xl font-semibold text-slate-900">{title}</h2>
#         <p className="mt-3 text-slate-600">{message}</p>
#
#         <div className="mt-6 flex gap-3 justify-end">
#           <button
#             onClick={onClose}
#             className="px-4 py-2.5 border border-slate-300 rounded-lg text-slate-700 hover:bg-slate-50"
#           >
#             Cancelar
#           </button>
#           <button
#             onClick={() => {
#               onConfirm();
#               onClose();
#             }}
#             className="px-4 py-2.5 bg-blue-600 rounded-lg text-white hover:bg-blue-700"
#           >
#             Confirmar
#           </button>
#         </div>
#       </div>
#     </div>
#   );
# }
# ```
````

## 🔍 Uso Avançado

### Integração com Ferramentas de Build

```javascript
// Exemplo de configuração com o servidor Tailwind v4.1
// tailwind.config.css

@config {
  content: ["./src/**/*.{html,js,jsx,ts,tsx}"];
  plugins: [formPlugin, typographyPlugin];
}

@layer base {
  :root {
    --color-primary: #3b82f6;
    --color-secondary: #64748b;
  }

  h1 {
    @apply text-2xl font-bold text-slate-900;
  }
}

@layer components {
  .btn-primary {
    @apply px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700;
  }
}
```

## 📚 Recursos Adicionais

- [Documentação Completa da API](../api/tailwind_server_api.md)
- [Guia de Migração v3 → v4.1](../guides/tailwind_migration_guide.md)
- [Exemplos de Componentes](../examples/tailwind_components.md)

---

**Desenvolvido para o projeto MCP Servers**
