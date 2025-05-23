# Guia de Migração: Tailwind CSS v3 → v4.1

Este guia abrangente apresenta as etapas e considerações necessárias para migrar projetos do Tailwind CSS v3.x para a versão 4.1, abordando todas as mudanças significativas e novos recursos.

![Migração Tailwind v4.1](../assets/tailwind_migration.png)

## 🔄 Visão Geral das Mudanças

O Tailwind CSS v4.1 introduz diversas alterações fundamentais na forma como o framework é configurado e utilizado. Este guia o ajudará a entender e implementar essas mudanças de modo eficiente.

## 📋 Checklist de Migração

Siga esta checklist para garantir uma migração tranquila:

- [ ] Atualizar dependências do Tailwind CSS e seus plugins
- [ ] Converter configurações de JavaScript para CSS
- [ ] Revisar e atualizar classes que tiveram alterações de nomenclatura
- [ ] Adaptar plugins personalizados para a nova API
- [ ] Testar componentes para garantir consistência visual
- [ ] Atualizar ferramentas de build e integração

## 🔧 Atualizando as Dependências

```bash
# Usando npm
npm uninstall tailwindcss
npm install tailwindcss@latest

# Usando yarn
yarn remove tailwindcss
yarn add tailwindcss@latest

# Usando pnpm
pnpm remove tailwindcss
pnpm add tailwindcss@latest
```

## 📝 Configuração: De JavaScript para CSS

### Antes (v3.x):

```javascript
// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#3b82f6",
        secondary: "#64748b",
      },
      fontFamily: {
        sans: ["Inter var", "sans-serif"],
      },
    },
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
};
```

### Depois (v4.1):

```css
/* tailwind.config.css */
@config {
  content: [ "./src/**/*.{html,js,jsx,ts,tsx}"];
  prefix: "";
}

@layer base {
  :root {
    --color-primary: #3b82f6;
    --color-secondary: #64748b;
    --font-family-sans: "Inter var", sans-serif;
  }
}

@plugin tailwindcss/forms;
@plugin tailwindcss/typography;
```

## 🎨 Mudanças no Sistema de Cores

### 1. Novos Nomes de Cores

| Versão 3.x | Versão 4.1 | Notas                                   |
| ---------- | ---------- | --------------------------------------- |
| gray-\*    | slate-\*   | A paleta gray foi substituída por slate |
| red-\*     | ruby-\*    | Nome alterado, tonalidades ajustadas    |
| green-\*   | emerald-\* | Nome alterado, tonalidades ajustadas    |
| blue-\*    | sky-\*     | Nome alterado, tonalidades ajustadas    |

### 2. Definição de Cores Customizadas

#### Antes (v3.x):

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: "#1a73e8",
        accent: "#f8fafc",
      },
    },
  },
};
```

#### Depois (v4.1):

```css
/* tailwind.config.css */
@layer base {
  :root {
    --color-brand: #1a73e8;
    --color-accent: #f8fafc;
  }
}
```

## 🧩 Mudanças na API de Plugins

### 1. Estrutura de Plugins

#### Antes (v3.x):

```javascript
// meu-plugin.js
const plugin = require("tailwindcss/plugin");

module.exports = plugin(function ({ addComponents, theme }) {
  addComponents({
    ".btn-fancy": {
      padding: theme("spacing.4"),
      borderRadius: theme("borderRadius.md"),
      backgroundColor: theme("colors.blue.500"),
      color: theme("colors.white"),
      "&:hover": {
        backgroundColor: theme("colors.blue.600"),
      },
    },
  });
});
```

#### Depois (v4.1):

```javascript
// meu-plugin.mjs
export default function ({ h }) {
  return {
    name: "fancy-button-plugin",
    layer: "components",
    components: {
      ".btn-fancy": h.css`
        padding: theme(spacing.4);
        border-radius: theme(borderRadius.md);
        background-color: theme(colors.blue.500);
        color: theme(colors.white);
        &:hover {
          background-color: theme(colors.blue.600);
        }
      `,
    },
  };
}
```

### 2. Importando Plugins

#### Antes (v3.x):

```javascript
// tailwind.config.js
module.exports = {
  plugins: [require("./meu-plugin.js"), require("@tailwindcss/forms")],
};
```

#### Depois (v4.1):

```css
/* tailwind.config.css */
@plugin "./meu-plugin.mjs";
@plugin tailwindcss/forms;
```

## 📏 Classes Utilitárias Atualizadas

### 1. Novas Sintaxes

| Versão 3.x     | Versão 4.1  | Descrição                            |
| -------------- | ----------- | ------------------------------------ |
| ring-2         | outline-2   | Substituição da nomenclatura de ring |
| shadow-lg      | shadow-xl   | Redefinição das escalas de sombra    |
| transition-all | animate-all | Nova abordagem para animações        |
| scale-105      | scale-1.05  | Valores numéricos diretos para scale |

### 2. Container Queries

Nova funcionalidade não disponível no v3:

```html
<div class="@container">
  <div class="@sm:text-lg @md:text-xl @lg:text-2xl">
    Texto responsivo baseado no container pai
  </div>
</div>
```

## 🛠️ Ferramentas e Integrações

### Build Tools

#### Vite

```javascript
// vite.config.js
import { defineConfig } from "vite";
import tailwindcss from "tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

#### Webpack

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          "style-loader",
          "css-loader",
          {
            loader: "tailwindcss-loader",
            options: {
              config: "./tailwind.config.css",
            },
          },
        ],
      },
    ],
  },
};
```

## 💡 Dicas para Migração Tranquila

1. **Migre Progressivamente**: Comece com componentes menos críticos
2. **Teste Exaustivamente**: Verifique se os estilos estão consistentes após a migração
3. **Use o CLI de Migração**: `npx tailwindcss-migrate` ajuda a converter configurações
4. **Atualize IDEs e Extensões**: Garanta que suas ferramentas suportem a sintaxe v4.1
5. **Refatore aos Poucos**: Não tente migrar tudo de uma vez

## 🔍 Solução de Problemas Comuns

### Classes Não Aplicadas

**Problema**: Classes do Tailwind v4.1 não estão sendo aplicadas  
**Solução**: Verifique se sua configuração de conteúdo (`content`) está correta e inclui todos os arquivos necessários

### Erros de Compilação

**Problema**: Erros ao compilar com a nova sintaxe CSS  
**Solução**: Certifique-se de que suas ferramentas de build estão atualizadas e configuradas para a versão 4.1

### Plugins Incompatíveis

**Problema**: Plugins antigos causando erros  
**Solução**: Atualize para versões compatíveis com v4.1 ou refatore para o novo formato

## 📚 Recursos Adicionais

- [Documentação Oficial do Tailwind v4.1](https://tailwindcss.com/docs)
- [Changelog Completo](https://github.com/tailwindlabs/tailwindcss/releases)
- [Repositório de Exemplos de Migração](https://github.com/tailwindlabs/tailwindcss-migration-examples)
- [Fórum da Comunidade](https://github.com/tailwindlabs/tailwindcss/discussions)

---

**Desenvolvido para o projeto MCP Servers**
