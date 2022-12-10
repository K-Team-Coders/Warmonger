/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'corme':'Cormorant Garamond',
        'rale':'Raleway'
      },
      colors:{
        'dark-blue':'#1a1e22',
        'dark-gray':'#0e0f10'
      }

    },
  },
  plugins: [],
}