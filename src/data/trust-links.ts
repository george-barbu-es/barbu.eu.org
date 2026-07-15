/**
 * Authoritative external references used across the lab.
 * Link these in prose so claims stay auditable. Do not invent citations.
 */
export const standards = {
  schemaOrg: 'https://schema.org/',
  person: 'https://schema.org/Person',
  organization: 'https://schema.org/Organization',
  creativeWork: 'https://schema.org/CreativeWork',
  softwareApplication: 'https://schema.org/SoftwareApplication',
  article: 'https://schema.org/Article',
  profilePage: 'https://schema.org/ProfilePage',
  collectionPage: 'https://schema.org/CollectionPage',
  founder: 'https://schema.org/founder',
  worksFor: 'https://schema.org/worksFor',
  sameAs: 'https://schema.org/sameAs',
  jobTitle: 'https://schema.org/jobTitle',
  image: 'https://schema.org/image',
  parentOrganization: 'https://schema.org/parentOrganization',
  brand: 'https://schema.org/brand',
  jsonLd: 'https://json-ld.org/',
  rfc9309: 'https://www.rfc-editor.org/rfc/rfc9309.html',
  llmsTxtProposal: 'https://llmstxt.org/',
  llmsTxtRepo: 'https://github.com/AnswerDotAI/llms-txt',
  googleStructuredData:
    'https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data',
  googleSpamPolicies: 'https://developers.google.com/search/docs/essentials/spam-policies',
  schemaValidator: 'https://validator.schema.org/',
  richResultsTest: 'https://search.google.com/test/rich-results',
} as const;

/** Grouped for lab UI and README. */
export const trustLinkGroups = [
  {
    title: 'schema.org vocabulary',
    links: [
      { label: 'schema.org', href: standards.schemaOrg },
      { label: 'Person', href: standards.person },
      { label: 'Organization', href: standards.organization },
      { label: 'CreativeWork', href: standards.creativeWork },
      { label: 'SoftwareApplication', href: standards.softwareApplication },
      { label: 'Article', href: standards.article },
      { label: 'ProfilePage', href: standards.profilePage },
      { label: 'CollectionPage', href: standards.collectionPage },
      { label: 'founder', href: standards.founder },
      { label: 'worksFor', href: standards.worksFor },
      { label: 'sameAs', href: standards.sameAs },
    ],
  },
  {
    title: 'Validation & search guidance',
    links: [
      { label: 'JSON-LD', href: standards.jsonLd },
      { label: 'Schema Markup Validator', href: standards.schemaValidator },
      { label: 'Rich Results Test', href: standards.richResultsTest },
      { label: 'Google structured data intro', href: standards.googleStructuredData },
      { label: 'Google spam policies', href: standards.googleSpamPolicies },
    ],
  },
  {
    title: 'Related web conventions',
    links: [
      { label: 'llms.txt proposal', href: standards.llmsTxtProposal },
      { label: 'llms.txt repository', href: standards.llmsTxtRepo },
      { label: 'RFC 9309 (robots)', href: standards.rfc9309 },
    ],
  },
] as const;
