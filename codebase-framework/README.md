# Codebase Framework

> Implementation guide for building Next.js frontends from design specifications

## Overview

The **Codebase Framework** is the final stage of the PO → Design → Code workflow. It provides templates, patterns, and standards for implementing features as working Next.js applications with dummy data, enabling rapid MVP deployment without backend complexity.

**Philosophy:** Build working frontends first, validate UX/UI with stakeholders, then invest in backend infrastructure.

**Output:** A deployable Next.js application that implements your designs using dummy JSON data instead of a real backend.

---

## Framework Vision

### The Complete Flow

```
PO Framework → Design Framework → Codebase Framework → Deployed MVP
    ↓               ↓                    ↓
  PRD/USD      Wireframes/          Next.js App
  UAT Tests    Components           + Dummy Data
```

### What You Get

A working website that:
- ✅ Implements designs from design-framework
- ✅ Connects to dummy JSON files (no real backend needed)
- ✅ Can be deployed easily to Vercel/Netlify
- ✅ Validates UX/UI before backend investment
- ✅ Provides realistic demos for stakeholders

---

## Tech Stack

The framework is built for this modern, lean stack:

### Frontend (Core)
- **Framework:** Next.js 15 with App Router
- **Styling:** TailwindCSS + ShadCN UI
- **Tables:** TanStack Table
- **Forms:** React Hook Form + Zod
- **Language:** TypeScript

### State Management
- **UI State:** React Context + useState (zero dependencies)
- **Server State:** Native fetch with Next.js caching

### Backend (Prototype Phase)
- **API:** Next.js API Routes
- **Data:** Dummy JSON files
- **Auth:** Skip initially (add later when needed)

### Deployment
- **Hosting:** Vercel (recommended) or Netlify
- **Strategy:** Static site with API routes

---

## Framework Structure

```
codebase-framework/
├── README.md                         # This file - Overview and getting started
├── FRAMEWORK_INTEGRATION.md          # How PO/Design stages → Code
├── QUICK_START.md                    # 5-minute quick start guide
│
├── project-structure/                # Next.js project organization
│   ├── README.md                     # Structure overview
│   ├── nextjs-app-router.md         # App Router conventions
│   ├── folder-organization.md       # Components, lib, utils organization
│   ├── naming-conventions.md        # File and folder naming rules
│   └── file-structure-example.md    # Complete example structure
│
├── themes/                           # CSS theme files
│   ├── README.md                     # Theme documentation
│   └── mds.css                       # MDS (Modern Design System) theme
│
├── component-patterns/               # React component implementation
│   ├── README.md                     # Component architecture
│   ├── shadcn-setup.md               # Installing ShadCN UI
│   ├── shadcn-usage.md               # Using ShadCN components
│   ├── theming.md                    # MDS theme integration guide
│   ├── animations.md                 # MDS animation patterns
│   ├── form-patterns.md              # Form handling patterns
│   ├── table-patterns.md             # TanStack Table patterns
│   ├── layout-components.md          # Headers, navigation, footers
│   ├── page-components.md            # Page structure patterns
│   └── common-patterns.md            # Modals, toasts, loading states
│
├── state-management/                 # State management patterns
│   ├── README.md                     # State philosophy
│   ├── context-patterns.md           # React Context setup
│   ├── state-best-practices.md      # When to use what
│   ├── data-fetching.md              # Client/server fetching
│   └── example-contexts.md           # Common context examples
│
├── api-patterns/                     # API and data patterns
│   ├── README.md                     # API strategy overview
│   ├── dummy-data-organization.md   # Structuring JSON files
│   ├── nextjs-api-routes.md         # Creating API routes
│   ├── data-fetching-client.md      # Client-side fetching
│   ├── data-fetching-server.md      # Server-side fetching
│   ├── api-conventions.md           # REST patterns
│   └── example-endpoints.md         # Common endpoint examples
│
├── testing-patterns/                 # Testing strategy
│   ├── README.md                     # Testing overview
│   ├── playwright-setup.md          # E2E testing setup
│   ├── uat-to-playwright.md         # Converting UAT → tests
│   ├── testing-examples.md          # Common test patterns
│   └── testing-checklist.md         # What to test
│
├── deployment/                       # Deployment guides
│   ├── README.md                     # Deployment overview
│   ├── vercel-setup.md               # Vercel deployment
│   ├── netlify-setup.md              # Netlify deployment
│   ├── environment-variables.md     # Managing env vars
│   └── deployment-checklist.md      # Pre-deployment checks
│
└── templates/                        # Ready-to-use code
    ├── README.md                     # Template usage guide
    ├── nextjs-starter/               # Complete starter project
    ├── component-templates/          # Copy-paste components
    └── data-templates/               # Dummy JSON examples
```

---

## How Stages Connect

### From PO Framework → Code

**USD (User Story Details) → Component Requirements**
- Acceptance criteria = Features to implement
- "User can click X" = Button with onClick handler
- "System shows Y" = Display logic

**UAT (User Acceptance Tests) → Playwright Tests**
- Given/When/Then = Test scenarios
- Direct conversion from UAT files (`uat/*.md`) to test cases

**User Stories → Implementation Checklist**
- Each story = A feature to build
- MoSCoW priority = Development order

### From Design Framework → Code

**Wireframes (WF-XXX) → Page Structure**
- ASCII layout = HTML/JSX structure
- Sections = React components

**Component Specs (COMP-XXX) → ShadCN Implementation**
- "Use Button variant='primary'" = `<Button variant="primary">`
- Component specs = Props and configuration

**Interactions (INT-XXX) → State + Handlers**
- State diagrams = useState/Context logic
- Transitions = Event handlers (onClick, onChange)
- User actions = Functions

**See [FRAMEWORK_INTEGRATION.md](FRAMEWORK_INTEGRATION.md) for detailed examples**

---

## Getting Started

### Quick Start (5 Minutes)

1. **Clone the starter template**
   ```bash
   cp -r codebase-framework/templates/nextjs-starter my-project
   cd my-project
   npm install
   ```

2. **Add your dummy data**
   ```bash
   # Edit data files in /data folder
   vim data/users.json
   vim data/products.json
   ```

3. **Create your first page**
   ```bash
   # Copy a page template
   cp templates/component-templates/list-page.tsx app/users/page.tsx
   ```

4. **Run development server**
   ```bash
   npm run dev
   # Open http://localhost:3000
   ```

5. **Deploy to Vercel**
   ```bash
   npm run build
   vercel deploy
   ```

**See [QUICK_START.md](QUICK_START.md) for detailed step-by-step guide**

---

## Core Concepts

### 1. Dummy Data Strategy

Instead of building a backend first, use dummy JSON files:

```
/data/
├── users.json          # User records
├── products.json       # Product catalog
└── orders.json         # Order history
```

Access via Next.js API routes:
```typescript
// app/api/users/route.ts
import users from '@/data/users.json'

export async function GET() {
  return Response.json(users)
}
```

**Benefits:**
- No database setup needed
- Easy deployment (static hosting)
- Fast iteration on frontend
- Realistic API patterns
- Easy to swap for real backend later

### 2. Component-First Development

Build pages from ShadCN components:

```typescript
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { DataTable } from '@/components/shared/data-table'

export default function UsersPage() {
  return (
    <Card>
      <Button>Add User</Button>
      <DataTable data={users} columns={columns} />
    </Card>
  )
}
```

**Benefits:**
- Professional UI out of the box
- Consistent design system
- Copy-paste from design specs
- Accessible by default

### 3. Zero-Dependency State Management

Use React's built-in features:

```typescript
// contexts/theme-context.tsx
import { createContext, useState } from 'react'

export const ThemeContext = createContext()

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light')

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}
```

**Benefits:**
- No external dependencies
- Simple mental model
- Easy to understand and debug
- Sufficient for MVP-scale apps

---

## Documentation Roadmap

### Phase 1: Core Documentation ✅
- [x] Framework overview (this file)
- [ ] Framework integration guide
- [ ] Quick start guide

### Phase 2: Project Structure ⏳
- [ ] Next.js App Router conventions
- [ ] Folder organization standards
- [ ] Naming conventions
- [ ] File structure examples

### Phase 3: Component Patterns 📋
- [ ] ShadCN setup and usage
- [ ] Form patterns
- [ ] Table patterns
- [ ] Layout patterns
- [ ] Common UI patterns

### Phase 4: State Management 📋
- [ ] Context patterns
- [ ] State best practices
- [ ] Data fetching patterns
- [ ] Example contexts

### Phase 5: API Patterns 📋
- [ ] Dummy data organization
- [ ] Next.js API routes
- [ ] Data fetching (client/server)
- [ ] API conventions

### Phase 6: Starter Template 📋
- [ ] Complete Next.js starter project
- [ ] Pre-configured with all tools
- [ ] Example pages and components
- [ ] Dummy data and API routes

### Phase 7: Component Templates 📋
- [ ] Dashboard page template
- [ ] List/table page template
- [ ] Detail view template
- [ ] Form page template
- [ ] Modal examples

### Phase 8: Testing & Deployment 📋
- [ ] Playwright setup
- [ ] UAT to test conversion
- [ ] Deployment guides (Vercel/Netlify)

---

## Success Criteria

The framework is successful when a developer can:

1. ✅ Clone the nextjs-starter template
2. ✅ Add dummy JSON data for their domain
3. ✅ Create pages matching their wireframes
4. ✅ Implement components from component specs
5. ✅ Add interactions from interaction diagrams
6. ✅ Deploy to Vercel in under 1 hour

And the documentation clearly shows:

1. ✅ How USD acceptance criteria → code features
2. ✅ How wireframes → JSX structure
3. ✅ How component specs → ShadCN usage
4. ✅ How interactions → state + handlers
5. ✅ How UAT scenarios → Playwright tests

---

## Why This Approach?

### Traditional Approach
```
Requirements → Design → Backend → Frontend → Integration → Deploy
                                   ↑
                          6-12 weeks to first demo
```

### Our Approach
```
Requirements → Design → Frontend + Dummy Data → Deploy
                           ↑
                   1-2 weeks to working demo
```

**Benefits:**
- **Faster validation:** Show working UI to stakeholders in days, not months
- **Cheaper iteration:** Change UI without backend rewrites
- **Better planning:** Real UI helps identify missing requirements
- **Reduced risk:** Validate UX before investing in infrastructure
- **Easier demos:** Deployable apps are better than wireframes

---

## Related Frameworks

- **PO Framework:** [../po-framework/](../po-framework/) - Product specifications (PRD → UAT)
- **Design Framework:** [../design-framework/](../design-framework/) - Design specifications (Wireframes → Interactions)
- **Features:** [../features/](../features/) - Feature implementations

---

## Tech Stack Rationale

### Why Next.js 14?
- App Router = Better performance, simpler patterns
- Built-in API routes = No separate backend needed
- Server components = Faster page loads
- Easy deployment = Vercel one-click deploy
- SEO-friendly = Server-side rendering

### Why TailwindCSS + ShadCN?
- Matches design-framework specifications
- Rapid development with utility classes
- Professional components out of the box
- Easy to customize and extend
- Copy-paste from documentation

### Why TanStack Table?
- Referenced in design-framework
- Powerful features (sorting, filtering, pagination)
- Headless = Full styling control
- TypeScript support
- Great documentation

### Why React Context + useState?
- Zero dependencies = Simpler stack
- Built into React = No learning curve
- Good enough = Sufficient for MVP scale
- Easy upgrade = Can add Zustand later if needed

### Why Skip Auth Initially?
- Focus on core features first
- Auth adds significant complexity
- Easy to add later when needed
- Can mock with hardcoded context for demos

### Why Dummy JSON + API Routes?
- Realistic API patterns = Easy to swap later
- No database setup = Faster start
- Static deployment = Cheaper hosting
- Better simulation = Can add delays, pagination, errors

---

## Getting Help

1. **Read the Quick Start:** [QUICK_START.md](QUICK_START.md)
2. **Check Integration Guide:** [FRAMEWORK_INTEGRATION.md](FRAMEWORK_INTEGRATION.md)
3. **Browse Templates:** [templates/](templates/)
4. **Review Examples:** See one-api-portal-mvp in [../features/](../features/)

---

**Framework:** Codebase Framework
**Purpose:** Rapid frontend prototyping with dummy data
**Status:** In active development
**Last Updated:** 2026-01-29
