/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    fontFamily: {
      'body': [
        'Inter',
        'ui-sans-serif',
        'system-ui',
        // other fallback fonts
      ],
      'sans': [
        'Inter',
        'ui-sans-serif',
        'system-ui',
        // other fallback fonts
      ]
    }
  },
  plugins: [],
}