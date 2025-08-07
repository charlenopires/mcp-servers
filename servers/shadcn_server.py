#!/usr/bin/env python3
"""
shadcn/ui MCP Server - Servidor MCP Avançado para shadcn/ui
=========================================================

Servidor MCP completo e aprimorado para integração com shadcn/ui que combina:

1. ACESSO A COMPONENTES
   - Busca e análise de componentes shadcn/ui
   - Demonstrações e exemplos de uso
   - Metadados de componentes com dependências

2. GERAÇÃO INTELIGENTE
   - Templates otimizados para diferentes casos de uso
   - Customização automática de temas
   - Integração com frameworks React modernos

3. ANÁLISE E OTIMIZAÇÃO
   - Análise de componentes existentes
   - Sugestões de melhorias e otimizações
   - Padrões de design system modernos

4. INTEGRAÇÃO COMPLETA
   - Suporte a Next.js, Vite, Remix
   - CLI commands e configuração automática
   - Compatibilidade com Tailwind CSS

Baseado em:
- Repositório oficial shadcn/ui
- Documentação completa da biblioteca
- Melhores práticas de design systems
- Padrões React modernos 2025
"""

import asyncio
import json
import re
import aiohttp
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar servidor MCP
mcp = FastMCP(
    name="shadcn-ui-advanced",
    version="2.0.0",
    description="Servidor MCP avançado para shadcn/ui com análise inteligente e geração otimizada"
)

# ================================
# KNOWLEDGE BASE - SHADCN/UI CONTEXT
# ================================

class ShadcnComponentType(Enum):
    LAYOUT = "layout"
    FORM = "form"
    DATA_DISPLAY = "data_display"
    NAVIGATION = "navigation"
    FEEDBACK = "feedback"
    OVERLAY = "overlay"
    INPUT = "input"
    MEDIA = "media"

class ShadcnFramework(Enum):
    NEXTJS = "next"
    VITE = "vite"
    REMIX = "remix"
    ASTRO = "astro"
    ROUTER = "react-router"

class ShadcnComplexity(Enum):
    SIMPLE = "simple"
    INTERMEDIATE = "intermediate"
    COMPLEX = "complex"

@dataclass
class ShadcnComponent:
    name: str
    category: ShadcnComponentType
    description: str
    dependencies: List[str]
    complexity: ShadcnComplexity
    use_cases: List[str]
    props: Dict[str, str]
    examples: List[str]

class ShadcnKnowledgeBase:
    """Base de conhecimento atualizada do shadcn/ui"""
    
    COMPONENTS_DATA = {
        "accordion": ShadcnComponent(
            name="accordion",
            category=ShadcnComponentType.LAYOUT,
            description="Seções de conteúdo expansíveis organizadas verticalmente",
            dependencies=["@radix-ui/react-accordion", "class-variance-authority"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["FAQ", "Navegação vertical", "Organização de conteúdo"],
            props={
                "type": "single | multiple",
                "collapsible": "boolean",
                "className": "string",
                "children": "ReactNode"
            },
            examples=["FAQ section", "Settings panel", "Product details"]
        ),
        "alert-dialog": ShadcnComponent(
            name="alert-dialog",
            category=ShadcnComponentType.OVERLAY,
            description="Modal dialog para confirmações e alertas importantes",
            dependencies=["@radix-ui/react-alert-dialog"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Confirmações", "Avisos críticos", "Ações destrutivas"],
            props={
                "open": "boolean",
                "onOpenChange": "function",
                "children": "ReactNode"
            },
            examples=["Delete confirmation", "Logout dialog", "Destructive action"]
        ),
        "badge": ShadcnComponent(
            name="badge", 
            category=ShadcnComponentType.DATA_DISPLAY,
            description="Pequenos labels informativos para status e categorização",
            dependencies=["class-variance-authority"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Status indicators", "Tags", "Categorização"],
            props={
                "variant": "default | secondary | destructive | outline",
                "className": "string",
                "children": "ReactNode"
            },
            examples=["Status badge", "Category tag", "Count indicator"]
        ),
        "button": ShadcnComponent(
            name="button",
            category=ShadcnComponentType.INPUT,
            description="Botão interativo com múltiplas variantes e tamanhos",
            dependencies=["@radix-ui/react-slot", "class-variance-authority"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["CTAs", "Ações primárias", "Navegação"],
            props={
                "variant": "default | destructive | outline | secondary | ghost | link",
                "size": "default | sm | lg | icon",
                "asChild": "boolean",
                "disabled": "boolean"
            },
            examples=["Submit button", "Navigation CTA", "Icon button"]
        ),
        "card": ShadcnComponent(
            name="card",
            category=ShadcnComponentType.LAYOUT,
            description="Container flexível para exibir conteúdo relacionado",
            dependencies=[],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Product cards", "Content sections", "Dashboard widgets"],
            props={
                "className": "string",
                "children": "ReactNode"
            },
            examples=["Product showcase", "Blog post card", "Dashboard metric"]
        ),
        "dialog": ShadcnComponent(
            name="dialog",
            category=ShadcnComponentType.OVERLAY,
            description="Modal overlay para interações focadas",
            dependencies=["@radix-ui/react-dialog"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Formulários", "Detalhes", "Configurações"],
            props={
                "open": "boolean",
                "onOpenChange": "function",
                "modal": "boolean"
            },
            examples=["Edit form", "Settings panel", "Content details"]
        ),
        "form": ShadcnComponent(
            name="form",
            category=ShadcnComponentType.FORM,
            description="Sistema completo de formulários com validação",
            dependencies=["react-hook-form", "@hookform/resolvers", "zod"],
            complexity=ShadcnComplexity.COMPLEX,
            use_cases=["Validação", "Submissão de dados", "User input"],
            props={
                "onSubmit": "function",
                "schema": "ZodSchema",
                "defaultValues": "object"
            },
            examples=["Contact form", "User registration", "Settings form"]
        ),
        "input": ShadcnComponent(
            name="input",
            category=ShadcnComponentType.INPUT,
            description="Campo de entrada de texto estilizado",
            dependencies=[],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Text input", "Search", "User data entry"],
            props={
                "type": "text | email | password | number",
                "placeholder": "string",
                "disabled": "boolean",
                "className": "string"
            },
            examples=["Search input", "Email field", "Password input"]
        ),
        "select": ShadcnComponent(
            name="select",
            category=ShadcnComponentType.INPUT,
            description="Dropdown select com busca e customização",
            dependencies=["@radix-ui/react-select"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Options selection", "Filtering", "Categorization"],
            props={
                "value": "string",
                "onValueChange": "function",
                "placeholder": "string",
                "disabled": "boolean"
            },
            examples=["Country selector", "Category filter", "Settings dropdown"]
        ),
        "table": ShadcnComponent(
            name="table",
            category=ShadcnComponentType.DATA_DISPLAY,
            description="Tabela responsiva para exibição de dados estruturados",
            dependencies=[],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Data display", "Lists", "Reports"],
            props={
                "className": "string",
                "children": "ReactNode"
            },
            examples=["User list", "Product catalog", "Analytics table"]
        ),
        "toast": ShadcnComponent(
            name="toast",
            category=ShadcnComponentType.FEEDBACK,
            description="Notificações temporárias não-intrusivas",
            dependencies=["@radix-ui/react-toast"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Feedback", "Success messages", "Error notifications"],
            props={
                "title": "string",
                "description": "string",
                "variant": "default | destructive",
                "duration": "number"
            },
            examples=["Success message", "Error notification", "Info alert"]
        )
    }

    THEMES_CONFIG = {
        "default": {
            "cssVars": True,
            "prefix": "",
            "colors": {
                "border": "hsl(var(--border))",
                "input": "hsl(var(--input))",
                "ring": "hsl(var(--ring))",
                "background": "hsl(var(--background))",
                "foreground": "hsl(var(--foreground))",
                "primary": {
                    "DEFAULT": "hsl(var(--primary))",
                    "foreground": "hsl(var(--primary-foreground))"
                },
                "secondary": {
                    "DEFAULT": "hsl(var(--secondary))",
                    "foreground": "hsl(var(--secondary-foreground))"
                }
            }
        },
        "dark": {
            "colors": {
                "background": "hsl(222.2 84% 4.9%)",
                "foreground": "hsl(210 40% 98%)",
                "primary": {
                    "DEFAULT": "hsl(210 40% 98%)",
                    "foreground": "hsl(222.2 84% 4.9%)"
                }
            }
        }
    }

    CLI_COMMANDS = {
        "init": "npx shadcn-ui@latest init",
        "add": "npx shadcn-ui@latest add [component]",
        "add_all": "npx shadcn-ui@latest add --all",
        "diff": "npx shadcn-ui@latest diff",
        "update": "npx shadcn-ui@latest update"
    }

    FRAMEWORK_CONFIGS = {
        ShadcnFramework.NEXTJS: {
            "installation": ["npm install next react react-dom", "npx create-next-app@latest"],
            "config_file": "next.config.js",
            "css_location": "app/globals.css",
            "components_dir": "components/ui"
        },
        ShadcnFramework.VITE: {
            "installation": ["npm create vite@latest", "npm install"],
            "config_file": "vite.config.ts",
            "css_location": "src/index.css",
            "components_dir": "src/components/ui"
        }
    }

# ================================
# ANALYZERS AND OPTIMIZERS
# ================================

class ShadcnAnalyzer:
    """Analisador avançado para componentes shadcn/ui"""
    
    def __init__(self):
        self.knowledge_base = ShadcnKnowledgeBase()
    
    async def analyze_component_usage(self, code: str) -> Dict[str, Any]:
        """Analisa uso de componentes shadcn/ui no código"""
        
        analysis = {
            "detected_components": [],
            "missing_imports": [],
            "optimization_suggestions": [],
            "accessibility_score": 0,
            "complexity_level": "simple"
        }
        
        # Detectar componentes utilizados
        detected = []
        for component_name in self.knowledge_base.COMPONENTS_DATA.keys():
            if f"<{component_name.title()}" in code or f"<{component_name}" in code:
                detected.append(component_name)
        
        analysis["detected_components"] = detected
        
        # Verificar imports necessários
        missing_imports = []
        for component_name in detected:
            component_data = self.knowledge_base.COMPONENTS_DATA[component_name]
            for dep in component_data.dependencies:
                if dep not in code and "package.json" not in code:
                    missing_imports.append(dep)
        
        analysis["missing_imports"] = list(set(missing_imports))
        
        # Sugestões de otimização
        suggestions = []
        
        if "className" in code and not any(x in code for x in ["cn(", "clsx(", "twMerge("]):
            suggestions.append("Considere usar utilitário cn() para merge de classes")
        
        if detected and "use client" not in code and any("onClick" in code for _ in [""]):
            suggestions.append("Adicione 'use client' para componentes interativos")
        
        if len(detected) > 5:
            suggestions.append("Considere dividir em componentes menores")
        
        analysis["optimization_suggestions"] = suggestions
        
        # Score de acessibilidade simples
        a11y_score = 50  # Base
        if "aria-" in code:
            a11y_score += 20
        if "alt=" in code:
            a11y_score += 15
        if "role=" in code:
            a11y_score += 15
        
        analysis["accessibility_score"] = min(100, a11y_score)
        
        # Nível de complexidade
        if len(detected) > 8:
            analysis["complexity_level"] = "complex"
        elif len(detected) > 3:
            analysis["complexity_level"] = "intermediate"
        
        return analysis

class ShadcnOptimizer:
    """Otimizador para componentes shadcn/ui"""
    
    def __init__(self):
        self.knowledge_base = ShadcnKnowledgeBase()
    
    async def optimize_component_code(self, code: str, focus_areas: List[str] = None) -> Dict[str, Any]:
        """Otimiza código shadcn/ui com foco em áreas específicas"""
        
        if focus_areas is None:
            focus_areas = ["performance", "accessibility", "best_practices"]
        
        optimized_code = code
        changes_made = []
        
        # Otimizações de performance
        if "performance" in focus_areas:
            # Adicionar React.memo se necessário
            if "export default" in optimized_code and "React.memo" not in optimized_code:
                optimized_code = re.sub(
                    r'export default function (\w+)',
                    r'export default React.memo(function \1',
                    optimized_code
                )
                if "React.memo" in optimized_code:
                    optimized_code += "\n)" if not optimized_code.endswith(")") else ""
                    changes_made.append("Adicionado React.memo para otimização")
        
        # Otimizações de acessibilidade
        if "accessibility" in focus_areas:
            # Adicionar roles ARIA apropriados
            if "<Button" in optimized_code and "role=" not in optimized_code:
                optimized_code = re.sub(
                    r'<Button([^>]*?)>',
                    r'<Button\1 role="button">',
                    optimized_code
                )
                changes_made.append("Adicionado role='button' aos botões")
        
        # Melhores práticas
        if "best_practices" in focus_areas:
            # Adicionar cn() utility
            if "className=" in optimized_code and "cn(" not in optimized_code:
                import_addition = 'import { cn } from "@/lib/utils"\n'
                if import_addition not in optimized_code:
                    optimized_code = import_addition + optimized_code
                
                optimized_code = re.sub(
                    r'className="([^"]*)"',
                    r'className={cn("\1")}',
                    optimized_code
                )
                changes_made.append("Adicionado utilitário cn() para classes")
        
        return {
            "original_code": code,
            "optimized_code": optimized_code,
            "changes_made": changes_made,
            "performance_improvements": [c for c in changes_made if "performance" in c.lower() or "memo" in c.lower()],
            "accessibility_improvements": [c for c in changes_made if "accessibility" in c.lower() or "aria" in c.lower() or "role" in c.lower()]
        }

class ShadcnGenerator:
    """Gerador inteligente de componentes shadcn/ui"""
    
    def __init__(self):
        self.knowledge_base = ShadcnKnowledgeBase()
    
    async def generate_component(
        self,
        component_type: str,
        use_case: str = "",
        framework: ShadcnFramework = ShadcnFramework.NEXTJS,
        theme: str = "default",
        include_examples: bool = True
    ) -> Dict[str, Any]:
        """Gera componente shadcn/ui otimizado"""
        
        if component_type not in self.knowledge_base.COMPONENTS_DATA:
            return {"error": f"Componente '{component_type}' não encontrado"}
        
        component_data = self.knowledge_base.COMPONENTS_DATA[component_type]
        
        # Templates base para diferentes componentes
        templates = {
            "button": self._generate_button_template,
            "card": self._generate_card_template,
            "form": self._generate_form_template,
            "dialog": self._generate_dialog_template,
            "table": self._generate_table_template,
            "select": self._generate_select_template,
            "input": self._generate_input_template,
            "badge": self._generate_badge_template,
            "accordion": self._generate_accordion_template,
            "toast": self._generate_toast_template
        }
        
        if component_type in templates:
            component_code = await templates[component_type](use_case, framework)
        else:
            component_code = await self._generate_generic_template(component_type, use_case)
        
        # Gerar exemplo de uso
        usage_example = await self._generate_usage_example(component_type, use_case)
        
        # Gerar configuração necessária
        setup_instructions = await self._generate_setup_instructions(component_type, framework)
        
        return {
            "component_type": component_type,
            "component_code": component_code,
            "usage_example": usage_example,
            "setup_instructions": setup_instructions,
            "dependencies": component_data.dependencies,
            "props": component_data.props,
            "complexity": component_data.complexity.value,
            "framework": framework.value
        }
    
    async def _generate_button_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de botão otimizado"""
        return f'''import {{ Button }} from "@/components/ui/button"
import {{ cn }} from "@/lib/utils"

interface CustomButtonProps {{
  variant?: "default" | "destructive" | "outline" | "secondary" | "ghost" | "link"
  size?: "default" | "sm" | "lg" | "icon"
  loading?: boolean
  children: React.ReactNode
  className?: string
  onClick?: () => void
}}

export default function CustomButton({{
  variant = "default",
  size = "default", 
  loading = false,
  children,
  className,
  onClick,
  ...props
}}: CustomButtonProps) {{
  return (
    <Button
      variant={{variant}}
      size={{size}}
      disabled={{loading}}
      className={{cn(
        "transition-all duration-200",
        loading && "opacity-50 cursor-not-allowed",
        className
      )}}
      onClick={{onClick}}
      {{...props}}
    >
      {{loading ? (
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
          Carregando...
        </div>
      ) : (
        children
      )}}
    </Button>
  )
}}'''
    
    async def _generate_card_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de card otimizado"""
        return f'''import {{ Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle }} from "@/components/ui/card"
import {{ Button }} from "@/components/ui/button"
import {{ cn }} from "@/lib/utils"

interface CustomCardProps {{
  title: string
  description?: string
  children?: React.ReactNode
  footer?: React.ReactNode
  className?: string
  variant?: "default" | "outline" | "ghost"
}}

export default function CustomCard({{
  title,
  description,
  children,
  footer,
  className,
  variant = "default",
  ...props
}}: CustomCardProps) {{
  return (
    <Card 
      className={{cn(
        "w-full transition-all duration-200 hover:shadow-lg",
        variant === "outline" && "border-2",
        variant === "ghost" && "border-none shadow-none",
        className
      )}}
      {{...props}}
    >
      <CardHeader>
        <CardTitle className="text-lg font-semibold">
          {{title}}
        </CardTitle>
        {{description && (
          <CardDescription className="text-muted-foreground">
            {{description}}
          </CardDescription>
        )}}
      </CardHeader>
      
      {{children && (
        <CardContent>
          {{children}}
        </CardContent>
      )}}
      
      {{footer && (
        <CardFooter className="pt-6">
          {{footer}}
        </CardFooter>
      )}}
    </Card>
  )
}}'''
    
    async def _generate_form_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de formulário completo"""
        return f'''import {{ useForm }} from "react-hook-form"
import {{ zodResolver }} from "@hookform/resolvers/zod"
import * as z from "zod"
import {{ Button }} from "@/components/ui/button"
import {{ Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage }} from "@/components/ui/form"
import {{ Input }} from "@/components/ui/input"
import {{ toast }} from "@/components/ui/use-toast"

const formSchema = z.object({{
  email: z.string().email({{
    message: "Por favor, insira um email válido.",
  }}),
  name: z.string().min(2, {{
    message: "Nome deve ter pelo menos 2 caracteres.",
  }}),
  message: z.string().min(10, {{
    message: "Mensagem deve ter pelo menos 10 caracteres.",
  }}),
}})

interface CustomFormProps {{
  onSubmit?: (values: z.infer<typeof formSchema>) => void
  submitText?: string
  className?: string
}}

export default function CustomForm({{
  onSubmit,
  submitText = "Enviar",
  className
}}: CustomFormProps) {{
  const form = useForm<z.infer<typeof formSchema>>({{
    resolver: zodResolver(formSchema),
    defaultValues: {{
      email: "",
      name: "",
      message: "",
    }},
  }})

  async function handleSubmit(values: z.infer<typeof formSchema>) {{
    try {{
      if (onSubmit) {{
        await onSubmit(values)
      }}
      
      toast({{
        title: "Sucesso!",
        description: "Formulário enviado com sucesso.",
      }})
      
      form.reset()
    }} catch (error) {{
      toast({{
        title: "Erro",
        description: "Ocorreu um erro ao enviar o formulário.",
        variant: "destructive",
      }})
    }}
  }}

  return (
    <Form {{...form}}>
      <form onSubmit={{form.handleSubmit(handleSubmit)}} className={{className}}>
        <div className="space-y-6">
          <FormField
            control={{form.control}}
            name="name"
            render={{({{ field }}) => (
              <FormItem>
                <FormLabel>Nome</FormLabel>
                <FormControl>
                  <Input placeholder="Seu nome completo" {{...field}} />
                </FormControl>
                <FormDescription>
                  Como você gostaria de ser chamado?
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}}
          />
          
          <FormField
            control={{form.control}}
            name="email"
            render={{({{ field }}) => (
              <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl>
                  <Input 
                    type="email" 
                    placeholder="seu@email.com" 
                    {{...field}} 
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}}
          />
          
          <FormField
            control={{form.control}}
            name="message"
            render={{({{ field }}) => (
              <FormItem>
                <FormLabel>Mensagem</FormLabel>
                <FormControl>
                  <textarea
                    className="min-h-[100px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                    placeholder="Sua mensagem..."
                    {{...field}}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}}
          />
        </div>
        
        <Button 
          type="submit" 
          className="w-full mt-6"
          disabled={{form.formState.isSubmitting}}
        >
          {{form.formState.isSubmitting ? "Enviando..." : submitText}}
        </Button>
      </form>
    </Form>
  )
}}'''
    
    async def _generate_dialog_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de dialog"""
        return '''import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { useState } from "react"

interface CustomDialogProps {
  trigger: React.ReactNode
  title: string
  description?: string
  children: React.ReactNode
  onConfirm?: () => void
  onCancel?: () => void
  confirmText?: string
  cancelText?: string
}

export default function CustomDialog({
  trigger,
  title,
  description,
  children,
  onConfirm,
  onCancel,
  confirmText = "Confirmar",
  cancelText = "Cancelar"
}: CustomDialogProps) {
  const [open, setOpen] = useState(false)

  const handleConfirm = () => {
    if (onConfirm) {
      onConfirm()
    }
    setOpen(false)
  }

  const handleCancel = () => {
    if (onCancel) {
      onCancel()
    }
    setOpen(false)
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        {trigger}
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>{title}</DialogTitle>
          {description && (
            <DialogDescription>
              {description}
            </DialogDescription>
          )}
        </DialogHeader>
        
        <div className="py-4">
          {children}
        </div>
        
        <DialogFooter>
          <Button variant="outline" onClick={handleCancel}>
            {cancelText}
          </Button>
          <Button onClick={handleConfirm}>
            {confirmText}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}'''
    
    async def _generate_table_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de tabela"""
        return '''import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

interface TableData {
  id: string
  [key: string]: any
}

interface CustomTableProps<T extends TableData> {
  data: T[]
  columns: {
    key: keyof T
    label: string
    render?: (value: any, row: T) => React.ReactNode
  }[]
  caption?: string
  onRowClick?: (row: T) => void
  className?: string
}

export default function CustomTable<T extends TableData>({
  data,
  columns,
  caption,
  onRowClick,
  className
}: CustomTableProps<T>) {
  return (
    <div className={`rounded-md border ${className}`}>
      <Table>
        {caption && <TableCaption>{caption}</TableCaption>}
        
        <TableHeader>
          <TableRow>
            {columns.map((column) => (
              <TableHead key={String(column.key)}>
                {column.label}
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        
        <TableBody>
          {data.map((row) => (
            <TableRow 
              key={row.id}
              className={onRowClick ? "cursor-pointer hover:bg-muted/50" : ""}
              onClick={() => onRowClick?.(row)}
            >
              {columns.map((column) => (
                <TableCell key={String(column.key)}>
                  {column.render 
                    ? column.render(row[column.key], row)
                    : String(row[column.key])
                  }
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
        
        {data.length === 0 && (
          <TableBody>
            <TableRow>
              <TableCell 
                colSpan={columns.length} 
                className="h-24 text-center text-muted-foreground"
              >
                Nenhum resultado encontrado.
              </TableCell>
            </TableRow>
          </TableBody>
        )}
      </Table>
    </div>
  )
}'''
    
    async def _generate_select_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de select"""
        return '''import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { FormControl, FormDescription, FormItem, FormLabel, FormMessage } from "@/components/ui/form"

interface SelectOption {
  value: string
  label: string
  disabled?: boolean
}

interface CustomSelectProps {
  options: SelectOption[]
  placeholder?: string
  value?: string
  onValueChange?: (value: string) => void
  disabled?: boolean
  className?: string
  label?: string
  description?: string
  error?: string
}

export default function CustomSelect({
  options,
  placeholder = "Selecione uma opção...",
  value,
  onValueChange,
  disabled = false,
  className,
  label,
  description,
  error
}: CustomSelectProps) {
  return (
    <FormItem className={className}>
      {label && <FormLabel>{label}</FormLabel>}
      <Select 
        value={value} 
        onValueChange={onValueChange}
        disabled={disabled}
      >
        <FormControl>
          <SelectTrigger>
            <SelectValue placeholder={placeholder} />
          </SelectTrigger>
        </FormControl>
        <SelectContent>
          {options.map((option) => (
            <SelectItem 
              key={option.value} 
              value={option.value}
              disabled={option.disabled}
            >
              {option.label}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
      {description && (
        <FormDescription>
          {description}
        </FormDescription>
      )}
      {error && <FormMessage>{error}</FormMessage>}
    </FormItem>
  )
}'''
    
    async def _generate_input_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de input"""
        return '''import { Input } from "@/components/ui/input"
import { FormControl, FormDescription, FormItem, FormLabel, FormMessage } from "@/components/ui/form"
import { cn } from "@/lib/utils"
import { forwardRef } from "react"

interface CustomInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  description?: string
  error?: string
  leftIcon?: React.ReactNode
  rightIcon?: React.ReactNode
}

const CustomInput = forwardRef<HTMLInputElement, CustomInputProps>(({
  label,
  description,
  error,
  leftIcon,
  rightIcon,
  className,
  ...props
}, ref) => {
  return (
    <FormItem>
      {label && <FormLabel>{label}</FormLabel>}
      <FormControl>
        <div className="relative">
          {leftIcon && (
            <div className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground">
              {leftIcon}
            </div>
          )}
          <Input
            ref={ref}
            className={cn(
              leftIcon && "pl-10",
              rightIcon && "pr-10",
              error && "border-destructive",
              className
            )}
            {...props}
          />
          {rightIcon && (
            <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-muted-foreground">
              {rightIcon}
            </div>
          )}
        </div>
      </FormControl>
      {description && (
        <FormDescription>
          {description}
        </FormDescription>
      )}
      {error && <FormMessage>{error}</FormMessage>}
    </FormItem>
  )
})

CustomInput.displayName = "CustomInput"

export default CustomInput'''
    
    async def _generate_badge_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de badge"""
        return '''import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"
import { cva, type VariantProps } from "class-variance-authority"

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default: "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
        secondary: "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive: "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
        outline: "text-foreground",
        success: "border-transparent bg-green-100 text-green-800 hover:bg-green-200 dark:bg-green-900 dark:text-green-300",
        warning: "border-transparent bg-yellow-100 text-yellow-800 hover:bg-yellow-200 dark:bg-yellow-900 dark:text-yellow-300",
        info: "border-transparent bg-blue-100 text-blue-800 hover:bg-blue-200 dark:bg-blue-900 dark:text-blue-300",
      },
      size: {
        default: "px-2.5 py-0.5 text-xs",
        sm: "px-2 py-0.5 text-xs",
        lg: "px-3 py-1 text-sm",
      }
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

interface CustomBadgeProps extends React.HTMLAttributes<HTMLDivElement>, VariantProps<typeof badgeVariants> {
  children: React.ReactNode
  icon?: React.ReactNode
}

export default function CustomBadge({
  children,
  variant,
  size,
  icon,
  className,
  ...props
}: CustomBadgeProps) {
  return (
    <Badge
      className={cn(badgeVariants({ variant, size }), className)}
      {...props}
    >
      {icon && <span className="mr-1">{icon}</span>}
      {children}
    </Badge>
  )
}'''
    
    async def _generate_accordion_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de accordion"""
        return '''import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

interface AccordionItemData {
  id: string
  title: string
  content: React.ReactNode
  disabled?: boolean
}

interface CustomAccordionProps {
  items: AccordionItemData[]
  type?: "single" | "multiple"
  collapsible?: boolean
  defaultValue?: string | string[]
  className?: string
}

export default function CustomAccordion({
  items,
  type = "single",
  collapsible = true,
  defaultValue,
  className
}: CustomAccordionProps) {
  return (
    <Accordion 
      type={type}
      collapsible={type === "single" ? collapsible : undefined}
      defaultValue={defaultValue}
      className={className}
    >
      {items.map((item) => (
        <AccordionItem 
          key={item.id} 
          value={item.id}
          disabled={item.disabled}
        >
          <AccordionTrigger className="text-left">
            {item.title}
          </AccordionTrigger>
          <AccordionContent>
            {item.content}
          </AccordionContent>
        </AccordionItem>
      ))}
    </Accordion>
  )
}'''
    
    async def _generate_toast_template(self, use_case: str, framework: ShadcnFramework) -> str:
        """Gera template de toast"""
        return '''import { toast } from "@/components/ui/use-toast"
import { Button } from "@/components/ui/button"
import { CheckCircle, AlertCircle, Info, AlertTriangle } from "lucide-react"

interface ToastOptions {
  title: string
  description?: string
  duration?: number
  action?: {
    altText: string
    label: string
    onClick: () => void
  }
}

export const showToast = {
  success: ({ title, description, duration = 5000, action }: ToastOptions) => {
    toast({
      title: (
        <div className="flex items-center gap-2">
          <CheckCircle className="h-4 w-4 text-green-600" />
          {title}
        </div>
      ),
      description,
      duration,
      action: action ? (
        <Button
          variant="outline"
          size="sm"
          onClick={action.onClick}
          aria-label={action.altText}
        >
          {action.label}
        </Button>
      ) : undefined,
    })
  },
  
  error: ({ title, description, duration = 5000, action }: ToastOptions) => {
    toast({
      title: (
        <div className="flex items-center gap-2">
          <AlertCircle className="h-4 w-4 text-red-600" />
          {title}
        </div>
      ),
      description,
      duration,
      variant: "destructive",
      action: action ? (
        <Button
          variant="outline"
          size="sm"
          onClick={action.onClick}
          aria-label={action.altText}
        >
          {action.label}
        </Button>
      ) : undefined,
    })
  },
  
  warning: ({ title, description, duration = 5000, action }: ToastOptions) => {
    toast({
      title: (
        <div className="flex items-center gap-2">
          <AlertTriangle className="h-4 w-4 text-yellow-600" />
          {title}
        </div>
      ),
      description,
      duration,
      action: action ? (
        <Button
          variant="outline"
          size="sm"
          onClick={action.onClick}
          aria-label={action.altText}
        >
          {action.label}
        </Button>
      ) : undefined,
    })
  },
  
  info: ({ title, description, duration = 5000, action }: ToastOptions) => {
    toast({
      title: (
        <div className="flex items-center gap-2">
          <Info className="h-4 w-4 text-blue-600" />
          {title}
        </div>
      ),
      description,
      duration,
      action: action ? (
        <Button
          variant="outline"
          size="sm"
          onClick={action.onClick}
          aria-label={action.altText}
        >
          {action.label}
        </Button>
      ) : undefined,
    })
  }
}

// Hook para uso simplificado
export function useToast() {
  return showToast
}'''
    
    async def _generate_generic_template(self, component_type: str, use_case: str) -> str:
        """Gera template genérico para componentes não específicos"""
        return f'''import {{ {component_type.title()} }} from "@/components/ui/{component_type}"
import {{ cn }} from "@/lib/utils"

interface Custom{component_type.title()}Props {{
  children?: React.ReactNode
  className?: string
}}

export default function Custom{component_type.title()}({{
  children,
  className,
  ...props
}}: Custom{component_type.title()}Props) {{
  return (
    <{component_type.title()}
      className={{cn("", className)}}
      {{...props}}
    >
      {{children}}
    </{component_type.title()}>
  )
}}'''
    
    async def _generate_usage_example(self, component_type: str, use_case: str) -> str:
        """Gera exemplo de uso do componente"""
        
        examples = {
            "button": '''// Exemplo de uso do CustomButton
import CustomButton from "./CustomButton"

export default function Page() {
  const handleClick = () => {
    console.log("Botão clicado!")
  }

  return (
    <div className="p-4 space-y-4">
      <CustomButton onClick={handleClick}>
        Botão Padrão
      </CustomButton>
      
      <CustomButton variant="destructive" loading={true}>
        Excluir Item
      </CustomButton>
      
      <CustomButton variant="outline" size="sm">
        Botão Pequeno
      </CustomButton>
    </div>
  )
}''',
            "card": '''// Exemplo de uso do CustomCard
import CustomCard from "./CustomCard"
import { Button } from "@/components/ui/button"

export default function Page() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      <CustomCard
        title="Produto Incrível"
        description="Descrição detalhada do produto"
        footer={
          <Button className="w-full">
            Comprar Agora
          </Button>
        }
      >
        <p>Conteúdo adicional do card aqui.</p>
      </CustomCard>
    </div>
  )
}''',
            "form": '''// Exemplo de uso do CustomForm
import CustomForm from "./CustomForm"

export default function Page() {
  const handleSubmit = async (values) => {
    console.log("Dados do formulário:", values)
    // Enviar para API
  }

  return (
    <div className="max-w-md mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Entre em Contato</h1>
      <CustomForm 
        onSubmit={handleSubmit}
        submitText="Enviar Mensagem"
      />
    </div>
  )
}'''
        }
        
        return examples.get(component_type, f'''// Exemplo de uso do Custom{component_type.title()}
import Custom{component_type.title()} from "./Custom{component_type.title()}"

export default function Page() {{
  return (
    <div className="p-4">
      <Custom{component_type.title()}>
        Conteúdo do componente
      </Custom{component_type.title()}>
    </div>
  )
}}''')
    
    async def _generate_setup_instructions(self, component_type: str, framework: ShadcnFramework) -> Dict[str, Any]:
        """Gera instruções de configuração"""
        
        component_data = self.knowledge_base.COMPONENTS_DATA.get(component_type)
        if not component_data:
            return {"error": "Componente não encontrado"}
        
        framework_config = self.knowledge_base.FRAMEWORK_CONFIGS.get(framework, {})
        
        return {
            "installation": {
                "cli_command": f"npx shadcn-ui@latest add {component_type}",
                "dependencies": component_data.dependencies,
                "manual_install": f"npm install {' '.join(component_data.dependencies)}" if component_data.dependencies else "Nenhuma dependência adicional"
            },
            "framework_setup": framework_config,
            "required_files": [
                f"components/ui/{component_type}.tsx",
                "lib/utils.ts",
                "tailwind.config.js"
            ],
            "css_variables": self.knowledge_base.THEMES_CONFIG["default"]["colors"] if component_type in ["button", "card", "input"] else {}
        }

# ================================
# FERRAMENTAS MCP
# ================================

@mcp.tool()
async def shadcn_analyze_component(code: str) -> Dict[str, Any]:
    """
    Analisa código que usa componentes shadcn/ui e fornece insights detalhados.
    
    Args:
        code: Código React que utiliza componentes shadcn/ui
        
    Returns:
        Análise completa com detecção de componentes, otimizações e sugestões
    """
    try:
        analyzer = ShadcnAnalyzer()
        analysis = await analyzer.analyze_component_usage(code)
        
        logger.info(f"Analyzed shadcn components - detected: {len(analysis['detected_components'])}")
        
        return analysis
        
    except Exception as e:
        logger.error(f"Error analyzing shadcn component: {str(e)}")
        raise

@mcp.tool()
async def shadcn_optimize_component(
    code: str,
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Otimiza código shadcn/ui aplicando melhores práticas e padrões modernos.
    
    Args:
        code: Código React com componentes shadcn/ui
        focus_areas: Áreas de foco para otimização (performance, accessibility, best_practices)
        
    Returns:
        Código otimizado com explicação das mudanças aplicadas
    """
    try:
        optimizer = ShadcnOptimizer()
        optimization = await optimizer.optimize_component_code(code, focus_areas)
        
        logger.info(f"Optimized shadcn component - changes: {len(optimization['changes_made'])}")
        
        return optimization
        
    except Exception as e:
        logger.error(f"Error optimizing shadcn component: {str(e)}")
        raise

@mcp.tool()
async def shadcn_generate_component(
    component_type: str,
    use_case: str = "",
    framework: str = "next",
    theme: str = "default",
    include_examples: bool = True
) -> Dict[str, Any]:
    """
    Gera componente shadcn/ui otimizado e pronto para uso.
    
    Args:
        component_type: Tipo do componente (button, card, form, dialog, etc.)
        use_case: Caso de uso específico para customização
        framework: Framework alvo (next, vite, remix, astro)
        theme: Tema a ser aplicado (default, dark)
        include_examples: Incluir exemplos de uso
        
    Returns:
        Código completo do componente com exemplos e configuração
    """
    try:
        generator = ShadcnGenerator()
        
        # Converter string para enum
        framework_enum = ShadcnFramework.NEXTJS
        if framework in ["vite"]:
            framework_enum = ShadcnFramework.VITE
        elif framework in ["remix"]:
            framework_enum = ShadcnFramework.REMIX
        elif framework in ["astro"]:
            framework_enum = ShadcnFramework.ASTRO
        elif framework in ["react-router", "router"]:
            framework_enum = ShadcnFramework.ROUTER
        
        result = await generator.generate_component(
            component_type=component_type,
            use_case=use_case,
            framework=framework_enum,
            theme=theme,
            include_examples=include_examples
        )
        
        logger.info(f"Generated shadcn component: {component_type} for {framework}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating shadcn component: {str(e)}")
        raise

@mcp.tool()
async def shadcn_get_component_info(component_name: str = "") -> Dict[str, Any]:
    """
    Obtém informações detalhadas sobre componentes shadcn/ui disponíveis.
    
    Args:
        component_name: Nome específico do componente (opcional)
        
    Returns:
        Informações completas sobre componente(s) shadcn/ui
    """
    try:
        knowledge_base = ShadcnKnowledgeBase()
        
        if not component_name:
            # Retorna lista de todos os componentes
            return {
                "available_components": list(knowledge_base.COMPONENTS_DATA.keys()),
                "components_by_category": {
                    category.value: [
                        name for name, comp in knowledge_base.COMPONENTS_DATA.items()
                        if comp.category == category
                    ]
                    for category in ShadcnComponentType
                },
                "total_components": len(knowledge_base.COMPONENTS_DATA)
            }
        
        if component_name not in knowledge_base.COMPONENTS_DATA:
            return {"error": f"Componente '{component_name}' não encontrado"}
        
        component = knowledge_base.COMPONENTS_DATA[component_name]
        
        return {
            "name": component.name,
            "category": component.category.value,
            "description": component.description,
            "dependencies": component.dependencies,
            "complexity": component.complexity.value,
            "use_cases": component.use_cases,
            "props": component.props,
            "examples": component.examples,
            "cli_install": f"npx shadcn-ui@latest add {component_name}"
        }
        
    except Exception as e:
        logger.error(f"Error getting shadcn component info: {str(e)}")
        raise

@mcp.tool()
async def shadcn_get_setup_guide(framework: str = "next") -> Dict[str, Any]:
    """
    Fornece guia completo de configuração do shadcn/ui para diferentes frameworks.
    
    Args:
        framework: Framework alvo (next, vite, remix, astro, react-router)
        
    Returns:
        Guia completo de instalação e configuração
    """
    try:
        knowledge_base = ShadcnKnowledgeBase()
        
        # Converter string para enum
        framework_enum = ShadcnFramework.NEXTJS
        if framework in ["vite"]:
            framework_enum = ShadcnFramework.VITE
        elif framework in ["remix"]:
            framework_enum = ShadcnFramework.REMIX
        elif framework in ["astro"]:
            framework_enum = ShadcnFramework.ASTRO
        elif framework in ["react-router", "router"]:
            framework_enum = ShadcnFramework.ROUTER
        
        framework_config = knowledge_base.FRAMEWORK_CONFIGS.get(framework_enum, {})
        
        setup_guide = {
            "framework": framework,
            "installation_steps": [
                "1. Instalar dependências do framework",
                "2. Configurar Tailwind CSS",
                "3. Inicializar shadcn/ui",
                "4. Configurar tema e CSS variables",
                "5. Adicionar componentes necessários"
            ],
            "commands": {
                "init": "npx shadcn-ui@latest init",
                "add_component": "npx shadcn-ui@latest add [component-name]",
                "add_all": "npx shadcn-ui@latest add --all"
            },
            "required_files": {
                "components.json": "Configuração dos componentes",
                "lib/utils.ts": "Utilitários (cn function)",
                f"{framework_config.get('css_location', 'globals.css')}": "CSS com variables do tema",
                "tailwind.config.js": "Configuração do Tailwind"
            },
            "framework_specific": framework_config,
            "theme_configuration": knowledge_base.THEMES_CONFIG,
            "next_steps": [
                "Personalizar tema no CSS",
                "Configurar dark mode",
                "Adicionar componentes necessários",
                "Configurar TypeScript paths",
                "Testar componentes básicos"
            ]
        }
        
        logger.info(f"Generated setup guide for {framework}")
        
        return setup_guide
        
    except Exception as e:
        logger.error(f"Error generating setup guide: {str(e)}")
        raise

@mcp.tool()
async def shadcn_create_theme(
    primary_color: str = "#000000",
    secondary_color: str = "#f1f5f9",
    accent_color: str = "#0ea5e9",
    theme_name: str = "custom"
) -> Dict[str, Any]:
    """
    Cria tema personalizado para shadcn/ui com cores especificadas.
    
    Args:
        primary_color: Cor primária em hexadecimal
        secondary_color: Cor secundária em hexadecimal  
        accent_color: Cor de destaque em hexadecimal
        theme_name: Nome do tema personalizado
        
    Returns:
        CSS do tema personalizado e configurações
    """
    try:
        # Converter hex para HSL (implementação simplificada)
        def hex_to_hsl(hex_color: str) -> str:
            # Remove # se presente
            hex_color = hex_color.lstrip('#')
            
            # Converte para RGB
            r = int(hex_color[0:2], 16) / 255
            g = int(hex_color[2:4], 16) / 255
            b = int(hex_color[4:6], 16) / 255
            
            # Simples aproximação HSL (para exemplo)
            max_val = max(r, g, b)
            min_val = min(r, g, b)
            
            h, s, l = 0, 0, (max_val + min_val) / 2
            
            if max_val == min_val:
                h = s = 0  # achromatic
            else:
                d = max_val - min_val
                s = d / (2 - max_val - min_val) if l > 0.5 else d / (max_val + min_val)
                
                if max_val == r:
                    h = (g - b) / d + (6 if g < b else 0)
                elif max_val == g:
                    h = (b - r) / d + 2
                elif max_val == b:
                    h = (r - g) / d + 4
                h /= 6
            
            return f"{h*360:.1f} {s*100:.1f}% {l*100:.1f}%"
        
        primary_hsl = hex_to_hsl(primary_color)
        secondary_hsl = hex_to_hsl(secondary_color)
        accent_hsl = hex_to_hsl(accent_color)
        
        theme_css = f'''/* {theme_name.title()} Theme for shadcn/ui */
@layer base {{
  :root {{
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: {primary_hsl};
    --primary-foreground: 210 40% 98%;
    --secondary: {secondary_hsl};
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: {accent_hsl};
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: {primary_hsl};
    --radius: 0.5rem;
  }}

  .dark {{
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;
    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;
    --primary: {primary_hsl};
    --primary-foreground: 222.2 84% 4.9%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: {accent_hsl};
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: {primary_hsl};
  }}
}}'''
        
        tailwind_config = f'''/** @type {{import('tailwindcss').Config}} */
const config = {{
  darkMode: ["class"],
  content: [
    './pages/**/*.{{ts,tsx}}',
    './components/**/*.{{ts,tsx}}',
    './app/**/*.{{ts,tsx}}',
    './src/**/*.{{ts,tsx}}',
  ],
  prefix: "",
  theme: {{
    container: {{
      center: true,
      padding: "2rem",
      screens: {{
        "2xl": "1400px",
      }},
    }},
    extend: {{
      colors: {{
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {{
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        }},
        secondary: {{
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        }},
        destructive: {{
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        }},
        muted: {{
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        }},
        accent: {{
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        }},
        popover: {{
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        }},
        card: {{
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        }},
      }},
      borderRadius: {{
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      }},
      keyframes: {{
        "accordion-down": {{
          from: {{ height: "0" }},
          to: {{ height: "var(--radix-accordion-content-height)" }},
        }},
        "accordion-up": {{
          from: {{ height: "var(--radix-accordion-content-height)" }},
          to: {{ height: "0" }},
        }},
      }},
      animation: {{
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      }},
    }},
  }},
  plugins: [require("tailwindcss-animate")],
}};

export default config;'''
        
        logger.info(f"Created custom theme: {theme_name}")
        
        return {
            "theme_name": theme_name,
            "colors": {
                "primary": primary_color,
                "secondary": secondary_color,
                "accent": accent_color
            },
            "css_variables": theme_css,
            "tailwind_config": tailwind_config,
            "installation_steps": [
                "1. Substitua o conteúdo do seu globals.css com o CSS fornecido",
                "2. Atualize seu tailwind.config.js com a configuração fornecida", 
                "3. Instale tailwindcss-animate: npm install tailwindcss-animate",
                "4. Reinicie seu servidor de desenvolvimento"
            ],
            "preview_components": [
                f'<Button className="bg-[{primary_color}]">Primary Button</Button>',
                f'<Badge className="bg-[{accent_color}]">Accent Badge</Badge>',
                f'<Card className="border-[{secondary_color}]">Themed Card</Card>'
            ]
        }
        
    except Exception as e:
        logger.error(f"Error creating shadcn theme: {str(e)}")
        raise

@mcp.tool()
async def shadcn_get_best_practices() -> Dict[str, Any]:
    """
    Retorna guia de melhores práticas para uso do shadcn/ui.
    
    Returns:
        Guia completo com padrões recomendados, estrutura de projeto e dicas
    """
    try:
        return {
            "project_structure": {
                "recommended": [
                    "components/ui/ - Componentes shadcn/ui",
                    "components/custom/ - Componentes customizados", 
                    "lib/utils.ts - Utilitários (cn function)",
                    "hooks/ - Custom hooks",
                    "types/ - Definições TypeScript"
                ],
                "organization": "Separe componentes base (ui) dos customizados"
            },
            
            "component_patterns": {
                "composition": "Use compound components para flexibilidade",
                "props": "Tipagem forte com TypeScript interfaces",
                "styling": "Use cn() utility para merge de classes",
                "variants": "Use class-variance-authority para variants consistentes"
            },
            
            "styling_guidelines": {
                "css_variables": "Use CSS variables para temas consistentes",
                "dark_mode": "Implemente dark mode com class strategy",
                "customization": "Customize no components.json, não nos arquivos de componente",
                "responsive": "Mobile-first approach com Tailwind breakpoints"
            },
            
            "performance_tips": [
                "Use React.memo para componentes puros",
                "Lazy load componentes pesados com React.lazy",
                "Otimize re-renders com useCallback e useMemo",
                "Use code splitting por rotas/features"
            ],
            
            "accessibility_checklist": [
                "Mantenha estrutura semântica HTML",
                "Use roles ARIA apropriados",
                "Garanta contraste mínimo de cores",
                "Teste navegação por teclado",
                "Adicione labels apropriados",
                "Use focus indicators claros"
            ],
            
            "form_patterns": {
                "validation": "React Hook Form + Zod para type-safe validation",
                "error_handling": "Consistent error display com FormMessage",
                "loading_states": "Disable forms durante submission",
                "accessibility": "Proper form labeling e error association"
            },
            
            "theming_strategy": {
                "design_tokens": "Use CSS custom properties para design tokens",
                "consistency": "Mantenha paleta de cores limitada e consistente",
                "customization": "Extend tema via tailwind.config.js",
                "testing": "Teste todos os estados em light/dark mode"
            },
            
            "common_patterns": {
                "data_display": "Table + Pagination para datasets grandes",
                "navigation": "NavigationMenu para hierarquias complexas", 
                "feedback": "Toast para notificações não-intrusivas",
                "overlays": "Dialog para ações focadas, AlertDialog para confirmações"
            },
            
            "do_dont": {
                "do": [
                    "Use TypeScript para type safety",
                    "Implemente dark mode desde o início",
                    "Teste acessibilidade regularmente",
                    "Mantenha componentes pequenos e focados",
                    "Use compound components para flexibilidade"
                ],
                "dont": [
                    "Não modifique componentes ui/ diretamente",
                    "Não use !important para override styles",
                    "Não ignore warnings de acessibilidade",
                    "Não crie muitas variants sem necessidade",
                    "Não esqueça de testar em diferentes devices"
                ]
            }
        }
        
    except Exception as e:
        logger.error(f"Error getting best practices: {str(e)}")
        raise

# ================================
# RECURSOS ADICIONAIS
# ================================

@mcp.resource(uri="guide://shadcn-ui-complete")
async def get_shadcn_complete_guide() -> str:
    """Guia completo do shadcn/ui"""
    return json.dumps({
        "title": "Guia Completo shadcn/ui - Servidor MCP Avançado",
        "sections": {
            "component_analysis": "Análise inteligente de componentes shadcn/ui",
            "code_optimization": "Otimização automática com melhores práticas",
            "component_generation": "Geração de componentes customizados",
            "theme_creation": "Criação de temas personalizados",
            "setup_automation": "Configuração automatizada por framework",
            "best_practices": "Padrões e práticas recomendadas"
        },
        "features": {
            "intelligent_analysis": "Detecção automática de componentes e dependências",
            "optimization_engine": "Engine de otimização para performance e a11y",
            "template_generation": "Templates otimizados para casos de uso específicos",
            "theme_generator": "Gerador de temas com suporte a dark mode",
            "multi_framework": "Suporte a Next.js, Vite, Remix, Astro",
            "best_practices_integration": "Integração automática de melhores práticas"
        }
    }, indent=2)

@mcp.resource(uri="templates://shadcn-components")
async def get_shadcn_templates() -> str:
    """Templates de componentes shadcn/ui"""
    knowledge_base = ShadcnKnowledgeBase()
    
    templates = {
        "components": {
            name: {
                "description": comp.description,
                "category": comp.category.value,
                "complexity": comp.complexity.value,
                "use_cases": comp.use_cases,
                "install_command": f"npx shadcn-ui@latest add {name}"
            }
            for name, comp in knowledge_base.COMPONENTS_DATA.items()
        },
        "categories": {
            category.value: [
                name for name, comp in knowledge_base.COMPONENTS_DATA.items()
                if comp.category == category
            ]
            for category in ShadcnComponentType
        }
    }
    
    return json.dumps(templates, indent=2)

# ================================
# INICIALIZAÇÃO DO SERVIDOR
# ================================

if __name__ == "__main__":
    logger.info("Starting shadcn/ui Advanced MCP Server")
    logger.info("Features: Component Analysis | Code Optimization | Intelligent Generation")
    logger.info("Based on: Official shadcn/ui documentation + Modern React patterns")
    
    # Executar o servidor MCP
    mcp.run()