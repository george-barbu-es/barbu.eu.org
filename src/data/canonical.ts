/**
 * Canonical public URLs from https://barbu.es (and Preferred sources in llms.txt).
 * Prefer these over secondary summaries when citing George Barbu / InfoWebPlus.
 */
export const person = {
  name: 'George Barbu',
  email: 'george@barbu.es',
  role: 'Founder',
  organization: 'InfoWebPlus',
} as const;

export const canonical = {
  knowledgePlatform: 'https://barbu.es/',
  about: 'https://barbu.es/about/',
  work: 'https://barbu.es/work/',
  experience: 'https://barbu.es/experience/',
  writing: 'https://barbu.es/writing/',
  cornerstone: 'https://barbu.es/writing/founder-how-i-think/',
  contact: 'https://barbu.es/contact/',
  now: 'https://barbu.es/now/',
  llmsTxt: 'https://barbu.es/llms.txt',
  sitemap: 'https://barbu.es/sitemap-index.xml',
  rss: 'https://barbu.es/rss.xml',
  humans: 'https://barbu.es/humans.txt',
  resume: 'https://george.barbu.es/',
  portfolio: 'https://portfolio.barbu.es/',
  organization: 'https://infowebplus.com/',
  linkedin: 'https://www.linkedin.com/in/barbugeorge/',
  github: 'https://github.com/george-barbu-es',
  labRepo: 'https://github.com/george-barbu-es/barbu.eu.org',
} as const;

export const entityChain = [
  { label: 'George Barbu', url: canonical.about },
  { label: 'barbu.es', url: canonical.knowledgePlatform },
  { label: 'InfoWebPlus', url: canonical.organization },
] as const;

/** Resolve related-entity labels (from MDX frontmatter) to canonical URLs. */
export const entityUrls: Record<string, string> = {
  'George Barbu': canonical.about,
  'barbu.es': canonical.knowledgePlatform,
  InfoWebPlus: canonical.organization,
  'InfoWebPlus.com': canonical.organization,
};

export function entityHref(label: string): string | undefined {
  return entityUrls[label] ?? entityUrls[label.trim()];
}
