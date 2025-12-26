const config = {
  content: [
    './mysite/templates/**/*.html',
    './mysite/static/**/*.{js,ts,jsx,tsx}'
    // add other paths as needed
  ],
  theme: {
    extend: {
      colors: {
        primary: '#5b7a8e',
        muted: '#ececf0',
        // add other custom colors here
      },
    },
  },
  plugins: [],
}
export default config
