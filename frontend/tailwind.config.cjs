/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'oxford-blue': {
          50: '#9da7b3',
          100: '#8591a1',
          200: '#6c7b8e',
          300: '#54657b',
          400: '#3b4f68',
          500: '#223955',
          600: '#0a2342', // Pallette base color
          700: '#09203b',
          800: '#081c35',
          900: '#07192e'
        },
        'zomp': {
          50: '#96d2c6',
          100: '#80c9bb',
          200: '#6bc0af',
          300: '#56b7a4',
          400: '#41ae98',
          500: '#2ca58d', // Pallette base color
          600: '#28957f',
          700: '#238471',
          800: '#1f7363',
          900: '#1a6355'
        },
        'eton-blue': {
          50: '#b5d7c4',
          100: '#a9d0ba',
          200: '#9dc9b0',
          300: '#90c3a6', 
          400: '#84bc9c', // Pallette base color
          500: '#77a98c',
          600: '#6a967d',
          700: '#5c846d',
          800: '#4f715e',
          900: '#425e4e'
        },
        'baby-powder': {
          50: '#fffdf7', // Pallette base color
          100: '#e6e4de',
          200: '#cccac6',
          300: '#b3b1ad',
          400: '#999894',
          500: '#807f7c',
          600: '#666563',
          700: '#4d4c4a',
          800: '#333331',
          900: '#191919'
        },
        'violet-red': {
          50: '#fbc0d5',
          100: '#fab0cb',
          200: '#f8a0c1',
          300: '#f790b6',
          400: '#f681ac',
          500: '#f571a1',
          600: '#f46197', // Pallette base color
          700: '#dc5788',
          800: '#c34e79',
          900: '#ab446a'
        }
      },
      fontFamily: {
        'sans': ['Poppins', ...defaultTheme.fontFamily.sans]
      }
    },
  },
  plugins: [],
}
