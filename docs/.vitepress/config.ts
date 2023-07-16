import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/libquery/',
  lang: 'en-US',
  title: 'libquery',
  description: 'Documentation for libquery',
  themeConfig: {
    logo: '/logo.png',

    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      {
          text: 'Docs',
          link: '/guide/get-started'
      },
    ],

    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Get Started', link: '/guide/get-started' },
        ]
      },
      {
        text: 'API Reference',
        items: [
          { text: 'David Rumsey Map Collection', link: '/api/david-rumsey-map-collection' },
          { text: 'Gallica', link: '/api/gallica' },
          { text: 'Internet Archive', link: '/api/internet-archive' },
          { text: 'Library of Congress', link: '/api/library-of-congress' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/oldvis/libquery' }
    ],

    search: {
      provider: 'local'
    }
  }
})
