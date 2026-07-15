import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import rehypeExternalLinks from 'rehype-external-links';

export default defineConfig({
  site: 'https://barbu.eu.org',
  devToolbar: {
    enabled: false,
  },
  markdown: {
    rehypePlugins: [
      [
        rehypeExternalLinks,
        {
          target: '_blank',
          rel: ['noopener', 'noreferrer'],
        },
      ],
    ],
  },
  integrations: [mdx()],
});
