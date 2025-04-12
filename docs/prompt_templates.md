# AI Agent Prompt Templates

This document contains standardized prompt templates for interacting with AI agents throughout the AgriPort Optimizer project. These templates ensure that all agents adhere to the Ultimate Vibe Architecting Roadmap and the project context.

## Standard Prompt Template

Use this template for most interactions with AI agents:

```markdown
I'm working on the AgriPort Optimizer webapp, following the **Ultimate Vibe Architecting Roadmap for AI-Powered Development**. You must adhere to the roadmap's phases and steps, using the master context file as your guide.

**Instructions**:
1. Read the master context file (`project_context.md`) in the project root to understand the current state, PRD, tickets, and decisions.
2. Focus on the specified roadmap phase and step (provided below).
3. Work on the active ticket or task described, adhering to its acceptance criteria.
4. Do not add unapproved features, change technologies, or skip steps without my explicit approval.
5. If clarification is needed, ask specific questions before proceeding.
6. After completing the task, suggest updates to `project_context.md` (e.g., new decisions, progress, challenges).

**Current Task**:
- **Roadmap Phase**: [e.g., Phase 3: Targeted Implementation]
- **Step**: [e.g., Step 6: Pre-Implementation Research]
- **Ticket/Task**: [e.g., Select Routing Engine]
- **Details**: [e.g., Research OSRM vs. GraphHopper, document pros/cons.]

**Project Context**:
- File: `project_context.md`
- Key Points: [Summarize briefly, e.g., Flask/Folium stack, 100x100 grid, OSRM for routing.]

**Output**:
- Provide the deliverables for the task (e.g., research summary, plan, file changes).
- Include any questions for me.
- Suggest updates to `project_context.md`.

Please confirm you've read `project_context.md` and are ready to proceed with the task.
```

## Phase-Specific Templates

### Phase 1: Creative Ideation & Strategic Brainstorming

```markdown
I'm working on the AgriPort Optimizer webapp, following the **Ultimate Vibe Architecting Roadmap for AI-Powered Development**. We are currently in Phase 1: Creative Ideation & Strategic Brainstorming.

**Instructions**:
1. Read the master context file (`project_context.md`) to understand the project's vision and current state.
2. Focus on creative exploration without excessive planning or implementation details.
3. Help me capture the vision for the project, focusing on the problem, features, user experience, and potential technologies.
4. Do not proceed to technical planning or implementation details appropriate for later phases.

**Current Task**:
- **Roadmap Phase**: Phase 1: Creative Ideation & Strategic Brainstorming
- **Step**: [Initial Creative Exploration | Research Query Preparation]
- **Task**: [Describe the specific ideation task]

**Project Context**:
- File: `project_context.md`
- Current Status: [Brief summary of project status]

**Output**:
- [Describe expected output: vision document, brainstorming ideas, research queries, etc.]
- Suggest updates to `project_context.md` based on our ideation.

Please confirm you've read `project_context.md` and are ready to proceed with the task.
```

### Phase 2: Deep Knowledge Acquisition & Structured Planning

```markdown
I'm working on the AgriPort Optimizer webapp, following the **Ultimate Vibe Architecting Roadmap for AI-Powered Development**. We are currently in Phase 2: Deep Knowledge Acquisition & Structured Planning.

**Instructions**:
1. Read the master context file (`project_context.md`) to understand the project's vision and current state.
2. Focus on gathering domain knowledge and creating structured planning documents.
3. Help me transform the project vision into actionable plans and specifications.
4. Do not proceed to implementation details appropriate for later phases.

**Current Task**:
- **Roadmap Phase**: Phase 2: Deep Knowledge Acquisition & Structured Planning
- **Step**: [Comprehensive Technical Research | PRD Creation | Ticket Generation]
- **Task**: [Describe the specific planning task]

**Project Context**:
- File: `project_context.md`
- Current Status: [Brief summary of project status]

**Output**:
- [Describe expected output: research findings, PRD sections, tickets, etc.]
- Suggest updates to `project_context.md` based on our planning.

Please confirm you've read `project_context.md` and are ready to proceed with the task.
```

### Phase 3: Targeted Implementation

```markdown
I'm working on the AgriPort Optimizer webapp, following the **Ultimate Vibe Architecting Roadmap for AI-Powered Development**. We are currently in Phase 3: Targeted Implementation.

**Instructions**:
1. Read the master context file (`project_context.md`) to understand the project's vision, PRD, and tickets.
2. Focus on implementing a specific ticket or task according to the PRD and project plan.
3. Follow the project's technical standards and architecture.
4. Do not add features or change technologies without approval.

**Current Task**:
- **Roadmap Phase**: Phase 3: Targeted Implementation
- **Step**: [Pre-Implementation Research | Architecture & Planning | Implementation | Testing | Cleanup]
- **Ticket**: [Specific ticket title]
- **Details**: [Ticket description and acceptance criteria]

**Project Context**:
- File: `project_context.md`
- Technical Stack: [Brief summary of technical stack]
- Current Status: [Brief summary of project status]

**Output**:
- [Describe expected output: code, tests, documentation, etc.]
- Explain how the implementation meets the ticket requirements.
- Suggest updates to `project_context.md` based on implementation decisions.

Please confirm you've read `project_context.md` and are ready to proceed with the task.
```

### Phase 4: Integration & Project Finalization

```markdown
I'm working on the AgriPort Optimizer webapp, following the **Ultimate Vibe Architecting Roadmap for AI-Powered Development**. We are currently in Phase 4: Integration & Project Finalization.

**Instructions**:
1. Read the master context file (`project_context.md`) to understand the project's vision, PRD, and implementation status.
2. Focus on integrating components, testing the entire system, and finalizing documentation.
3. Help identify gaps, issues, or improvements needed for project completion.
4. Prepare for project handoff and maintenance.

**Current Task**:
- **Roadmap Phase**: Phase 4: Integration & Project Finalization
- **Step**: [Integration Testing | Documentation Creation | Retrospective & Future Planning]
- **Task**: [Describe the specific integration or finalization task]

**Project Context**:
- File: `project_context.md`
- Implementation Status: [Brief summary of implementation status]

**Output**:
- [Describe expected output: test results, documentation, retrospective findings, etc.]
- Suggest updates to `project_context.md` based on integration and finalization insights.

Please confirm you've read `project_context.md` and are ready to proceed with the task.
```

## Context Update Template

Use this template to get AI assistance in updating the project_context.md file after completing tasks:

```markdown
Please review the work we've completed on the following task for the AgriPort Optimizer project:

**Task Completed**:
- **Roadmap Phase**: [Phase completed in]
- **Step**: [Step completed]
- **Ticket/Task**: [Task completed]
- **Summary of Work**: [Brief summary of what was done]

Based on this work, suggest updates to the `project_context.md` file, including:
1. Updates to the Current State section
2. New Key Decisions made
3. Progress on the PRD or tickets
4. New challenges identified
5. Next steps to be taken

Please format your response as editable markdown sections that I can directly copy into the project_context.md file.
```

## Security Review Template

Use this template to have AI agents review code or designs for security issues:

```markdown
I need a security review for the AgriPort Optimizer project. Please read the relevant files and identify any security concerns, following the security guidelines in our project context.

**Files to Review**:
- [List of files or code snippets to review]

**Focus Areas**:
- Input validation and sanitization
- Authentication and authorization
- Data protection
- API security
- Common web vulnerabilities (OWASP Top 10)
- [Any other specific security concerns]

**Context**:
- This is a webapp for agricultural logistics in Argentina
- It processes user-provided cost data and shows optimized shipping routes
- [Any other relevant context]

Please provide:
1. Identified security issues (if any)
2. Severity rating for each issue
3. Recommended fixes
4. Best practices to implement

Refer to the security guidelines in `project_context.md` and `.cursor/rules` during your review.
```