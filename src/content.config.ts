import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const experimentStatus = z.enum([
  'Planned',
  'Running',
  'Completed',
  'Rejected',
  'Archived',
]);

const evidenceLevel = z.enum(['A', 'B', 'C', 'D']);

const experiments = defineCollection({
  loader: glob({
    pattern: '**/exp-*.{md,mdx}',
    base: './src/content/experiments',
  }),
  schema: z.object({
    id: z.string().regex(/^exp-\d{3}$/),
    number: z.number().int().positive(),
    title: z.string().min(1),
    researchQuestion: z.string().min(1),
    /**
     * Manual status. Completed / Rejected / Archived are never auto-set.
     * Planned + startsOn auto-promotes to Running on that UTC day.
     */
    status: experimentStatus,
    /**
     * When status is Planned, effective status becomes Running on/after this
     * UTC calendar day. Terminal statuses ignore startsOn.
     */
    startsOn: z.coerce.date().optional(),
    /**
     * A = confirmed with data and repeated
     * B = confirmed once
     * C = initial observation
     * D = hypothesis
     */
    evidenceLevel: evidenceLevel.default('D'),
    author: z.object({
      name: z.string(),
      role: z.string(),
      organization: z.string(),
    }),
    published: z.coerce.date(),
    updated: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    relatedEntities: z.array(z.string()).default([]),
    summary: z.string().min(1),
  }),
});

export const collections = { experiments };
