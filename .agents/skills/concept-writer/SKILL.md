---
name: concept-writer
description: Write or revise rigorous algorithm and computer-science concept notes. Use when the user asks to explain, document, teach, or create learning notes for a data structure, algorithm, or CS topic such as stacks, heaps, graphs, Dijkstra, dynamic programming, or complexity.
---

# Concept Writer

Create one concept note at the requested path. Do not commit or push.

## Inputs

Use the user's topic, destination path, and any stated curriculum scope. Ask only when the destination is necessary and unknown.

## Note structure

Adapt headings to the topic. Cover these where relevant:

1. Definition
2. Core principle and step-by-step operation
3. Abstract concept versus common implementations
4. Complexity, including why it has that cost
5. Language-neutral pseudocode
6. Use cases, trade-offs, and common mistakes

## Writing rules

- When writing in Korean, use the formal `-습니다` style consistently for all explanatory prose.
- Use English and symbols only inside fenced code blocks, including ASCII diagrams and pseudocode; explain them in Korean outside the block.
- Use unnumbered Markdown headings; do not prefix headings with numeric ordinals.
- Write for beginners without omitting the underlying CS reasoning.
- Introduce technical terms precisely, then explain them in plain language.
- Explain performance causally: for example, random access, contiguous memory, pointer traversal, cache locality, heap ordering, or relaxation.
- Separate guaranteed complexity from amortized or implementation-dependent complexity.
- State trade-offs and invalid assumptions; do not present a structure or algorithm as universally best.
- Use paper-style pseudocode, not a programming language or language-specific library API.
- Stay within any supplied curriculum scope. Mention later concepts only when necessary and label them as later material.
- Keep examples minimal and illustrative. Do not add problem solutions unless requested.
