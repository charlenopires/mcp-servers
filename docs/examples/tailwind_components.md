# Exemplos de Componentes Tailwind CSS v4.1

Esta página contém exemplos de componentes criados com o Tailwind CSS v4.1 usando o Servidor Tailwind CSS MCP.

## 📋 Visão Geral

Os exemplos abaixo demonstram a implementação de componentes comuns utilizando as novas funcionalidades do Tailwind CSS v4.1. Cada exemplo inclui o código completo, explicação das técnicas utilizadas e uma demonstração visual.

## 🎯 Cards

### Card de Produto

Um card de produto moderno com imagem, título, preço e botão de compra.

```jsx
// React Component
export default function ProductCard({ product }) {
  const { name, price, image, category } = product;

  return (
    <div className="group flex flex-col overflow-hidden rounded-xl bg-white shadow-md transition hover:shadow-lg dark:bg-slate-800">
      {/* Badge */}
      <div className="absolute right-2 top-2 z-10">
        <span className="rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800 dark:bg-blue-900/30 dark:text-blue-300">
          {category}
        </span>
      </div>

      {/* Image container */}
      <div className="relative aspect-square overflow-hidden bg-slate-100">
        <img
          src={image}
          alt={name}
          className="absolute inset-0 h-full w-full object-cover object-center transition duration-300 group-hover:scale-105"
        />
      </div>

      {/* Content */}
      <div className="flex flex-1 flex-col justify-between p-4">
        <h3 className="mb-2 text-lg font-medium text-slate-900 dark:text-white">
          {name}
        </h3>

        <div className="mt-auto flex items-center justify-between">
          <p className="text-xl font-bold text-slate-900 dark:text-white">
            ${price}
          </p>

          <button className="rounded-lg bg-blue-600 px-3.5 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:ring-offset-2 dark:shadow-blue-900/20">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}
```

**Técnicas destacadas:**

- Uso do novo sistema de cores com `slate-` e variações atualizadas
- Container queries com `@container`
- Animações aprimoradas com `transition duration-300`
- Suporte nativo para dark mode com `dark:`
- Novos espaçamentos e sistemas de sombra

### Card de Blog

Card para postagens de blog com imagem, categoria, título, resumo e link.

```jsx
// React Component
export default function BlogCard({ post }) {
  const { title, excerpt, category, image, date, author } = post;

  return (
    <div className="@container flex flex-col overflow-hidden rounded-xl bg-white shadow-md dark:bg-slate-800">
      {/* Image */}
      <div className="aspect-video overflow-hidden bg-slate-200">
        <img
          src={image}
          alt={title}
          className="h-full w-full object-cover object-center"
        />
      </div>

      <div className="flex flex-1 flex-col p-5">
        {/* Category & Date */}
        <div className="mb-3 flex items-center justify-between">
          <span className="rounded-full bg-emerald-100 px-2.5 py-0.5 text-xs font-medium text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-300">
            {category}
          </span>
          <time className="text-xs text-slate-500 dark:text-slate-400">
            {date}
          </time>
        </div>

        {/* Title */}
        <h3 className="mb-2 text-xl font-semibold text-slate-900 dark:text-white @md:text-2xl">
          {title}
        </h3>

        {/* Excerpt */}
        <p className="mb-4 text-slate-500 dark:text-slate-400 @lg:text-base @sm:line-clamp-2 @md:line-clamp-3">
          {excerpt}
        </p>

        {/* Author & Read More */}
        <div className="mt-auto flex items-center justify-between">
          <div className="flex items-center gap-2">
            <img
              src={author.avatar}
              alt={author.name}
              className="h-8 w-8 rounded-full"
            />
            <span className="text-sm font-medium text-slate-700 dark:text-slate-300">
              {author.name}
            </span>
          </div>

          <a
            href="#"
            className="text-sm font-medium text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300"
          >
            Read More →
          </a>
        </div>
      </div>
    </div>
  );
}
```

**Técnicas destacadas:**

- Containers responsivos com `@container`, `@sm`, `@md` e `@lg`
- Nova sintaxe `line-clamp-` para truncar texto
- Novos tons de cores `emerald-` em vez de `green-`
- Uso de `aspect-video` para proporções de imagem

## 🔄 Modais e Diálogos

### Modal de Confirmação

Um modal moderno e acessível com efeitos de backdrop blur.

```jsx
// React Component
import { useState, Fragment } from "react";

export default function ConfirmationModal({
  isOpen,
  onClose,
  onConfirm,
  title = "Confirm Action",
  message = "Are you sure you want to proceed with this action?",
}) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/25 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div
        className="relative w-full max-w-md rounded-xl bg-white p-6 shadow-2xl animate-in fade-in zoom-in duration-200 dark:bg-slate-800"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
      >
        <h2
          id="modal-title"
          className="text-xl font-semibold text-slate-900 dark:text-white"
        >
          {title}
        </h2>

        <p className="mt-3 text-slate-600 dark:text-slate-300">{message}</p>

        <div className="mt-6 flex gap-3 justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2.5 border border-slate-300 rounded-lg text-slate-700 hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-blue-600/50 dark:border-slate-600 dark:text-slate-300 dark:hover:bg-slate-700/50"
          >
            Cancel
          </button>

          <button
            onClick={() => {
              onConfirm();
              onClose();
            }}
            className="px-4 py-2.5 bg-blue-600 rounded-lg text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600/50 focus:ring-offset-2 dark:bg-blue-600 dark:hover:bg-blue-700"
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  );
}
```

**Técnicas destacadas:**

- Novo sistema de animações com `animate-in`, `fade-in` e `zoom-in`
- Efeito `backdrop-blur-sm` para fundo desfocado
- Duração de animação com `duration-200`
- Uso de `focus:ring-` para melhor acessibilidade

## 📝 Formulários

### Formulário de Contato

Um formulário de contato responsivo com validação visual.

```jsx
// React Component
import { useState } from "react";

export default function ContactForm() {
  const [formState, setFormState] = useState({
    name: "",
    email: "",
    message: "",
    submitted: false,
    errors: {},
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Validation logic here
    setFormState((prev) => ({ ...prev, submitted: true }));
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="rounded-xl bg-white p-6 shadow-lg dark:bg-slate-800 @lg:p-8"
    >
      <h2 className="mb-6 text-2xl font-bold text-slate-900 dark:text-white">
        Get in Touch
      </h2>

      <div className="space-y-5">
        {/* Name Field */}
        <div>
          <label
            htmlFor="name"
            className="mb-1.5 block text-sm font-medium text-slate-700 dark:text-slate-300"
          >
            Your Name
          </label>
          <input
            type="text"
            id="name"
            value={formState.name}
            onChange={(e) =>
              setFormState({ ...formState, name: e.target.value })
            }
            className="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-slate-800 placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 dark:border-slate-600 dark:bg-slate-700/50 dark:text-white dark:placeholder:text-slate-500"
            placeholder="John Doe"
            required
          />
        </div>

        {/* Email Field */}
        <div>
          <label
            htmlFor="email"
            className="mb-1.5 block text-sm font-medium text-slate-700 dark:text-slate-300"
          >
            Email Address
          </label>
          <input
            type="email"
            id="email"
            value={formState.email}
            onChange={(e) =>
              setFormState({ ...formState, email: e.target.value })
            }
            className="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-slate-800 placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 dark:border-slate-600 dark:bg-slate-700/50 dark:text-white dark:placeholder:text-slate-500"
            placeholder="john@example.com"
            required
          />
        </div>

        {/* Message Field */}
        <div>
          <label
            htmlFor="message"
            className="mb-1.5 block text-sm font-medium text-slate-700 dark:text-slate-300"
          >
            Your Message
          </label>
          <textarea
            id="message"
            value={formState.message}
            onChange={(e) =>
              setFormState({ ...formState, message: e.target.value })
            }
            rows={4}
            className="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-slate-800 placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 dark:border-slate-600 dark:bg-slate-700/50 dark:text-white dark:placeholder:text-slate-500"
            placeholder="How can we help you?"
            required
          />
        </div>
      </div>

      <div className="mt-6">
        <button
          type="submit"
          className="w-full rounded-lg bg-blue-600 px-5 py-3 text-center font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:ring-offset-2 @md:w-auto"
        >
          Send Message
        </button>
      </div>

      {formState.submitted && (
        <div className="mt-4 rounded-lg bg-emerald-50 p-3 text-sm text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-300">
          Thanks for your message! We'll get back to you soon.
        </div>
      )}
    </form>
  );
}
```

**Técnicas destacadas:**

- Campos de formulário otimizados com `focus:ring` para feedback visual
- CSS nativo para dark mode com `dark:`
- Container queries para responsividade: `@lg:p-8` e `@md:w-auto`
- Uso de `placeholder:text-slate-400` para estilização específica

## 🔍 Mais Exemplos

Para mais exemplos e componentes, confira os seguintes recursos:

1. [Documentação Oficial do Tailwind CSS v4.1](https://tailwindcss.com/)
2. [API Completa do Servidor Tailwind CSS](../api/tailwind_server_api.md)
3. [Guia de Migração Tailwind v3 → v4.1](../guides/tailwind_migration_guide.md)

---

**Desenvolvido para o projeto MCP Servers**
