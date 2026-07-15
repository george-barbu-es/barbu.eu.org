const SITE_ORIGIN = 'https://barbu.eu.org';

/**
 * External http(s) links open in a new tab. Same-site, relative, hash,
 * mailto, and tel stay in the current tab.
 */
export function isExternalHref(href: string, siteOrigin = SITE_ORIGIN): boolean {
  if (!href) return false;
  if (
    href.startsWith('/') ||
    href.startsWith('#') ||
    href.startsWith('?') ||
    href.startsWith('mailto:') ||
    href.startsWith('tel:')
  ) {
    return false;
  }

  try {
    const resolved = new URL(href, siteOrigin);
    return resolved.origin !== new URL(siteOrigin).origin;
  } catch {
    return false;
  }
}

export function externalLinkProps(href: string): {
  target?: '_blank';
  rel?: string;
} {
  if (!isExternalHref(href)) return {};
  return { target: '_blank', rel: 'noopener noreferrer' };
}
