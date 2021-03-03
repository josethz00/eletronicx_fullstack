import React from 'react'
import { AppProps } from 'next/app'
import { ThemeProvider } from 'styled-components'
import { ToastContainer } from 'react-toastify'

import GlobalStyle from '../styles/global'
import theme from '../styles/theme'
import AuthProvider from '../contexts/AuthContext'


const MyApp: React.FC<AppProps> = ({ Component, pageProps }) =>{
  return (
    <AuthProvider>
      <ThemeProvider theme={theme}>
        <Component {...pageProps} />
        <GlobalStyle />
        <ToastContainer autoClose={2000} />
      </ThemeProvider>
    </AuthProvider>
  )
}

export default MyApp
