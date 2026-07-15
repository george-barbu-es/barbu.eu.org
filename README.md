# Open AI Search Research Lab

Public research infrastructure for **real** experiments in AI Search, Entity SEO, and Knowledge Graphs.

This is not a blog to fill, not a marketing site, and not an SEO news feed. It is an open lab whose catalog grows only when genuine observation exists.

**Author:** [George Barbu](https://barbu.es/about/), Founder of [InfoWebPlus](https://infowebplus.com/)

## Mandate

- Every article documents a real experiment.
- Distinguish **Facts**, **Assumptions**, **Hypotheses**, **Unknowns**, and **Limitations**.
- Never invent results.
- Quality over cadence: publish when work is real. One well-documented completion per month is enough; zero is fine if nothing relevant ran.

## Day-1 posture

| Status | Count |
| --- | --- |
| Running | 2 (Exp-001, Exp-002) |
| Planned | 8 |
| Completed | 0 |

Unsupported Completed claims destroy credibility. Evidence starts at **D** for Planned protocols. Active runs may move to **C** when observation has begun. Raise to **B**/**A** only with archived captures.

Change per experiment via frontmatter:

```yaml
evidenceLevel: D # or C, B, A
```

## Status badges

| Badge | Meaning |
| --- | --- |
| Planned | Protocol defined; measurement not started |
| Running | Intervention / collection in progress |
| Completed | Finished; results from archived captures |
| Rejected | Stopped / not pursued |
| Archived | Closed historically; kept for reference |

`Planned` + `startsOn` auto-promotes to `Running` on that UTC day. Terminal states are never auto-set.

## Evidence level

| Level | Meaning |
| --- | --- |
| A | Confirmed with data and repeated |
| B | Confirmed once |
| C | Initial observation |
| D | Hypothesis |

## Canonical sources (from [barbu.es](https://barbu.es/))

Prefer these URLs when probing or citing Person / Organization entities (also in [llms.txt](https://barbu.es/llms.txt)). Full table and trust links: see site homepage and `src/data/canonical.ts`, `src/data/trust-links.ts`.

## Repository layout

```text
src/content/experiments/   # Experiment MDX (content collection)
src/pages/                 # Astro routes
src/data/lab.ts            # Brand / publishing rules
templates/experiment.mdx   # Reusable template (repo only, not shown in UI footer)
data/                      # Reserved for raw captures
```

## Develop locally

```bash
npm install
npm run dev
```

```bash
npm run build
npm run preview
```
