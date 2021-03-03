import React, { FormEvent, useContext, useEffect, useRef } from 'react'
import { toast } from 'react-toastify'

import AuthContainer from '../components/AuthContainer'
import nextJSLogo from '../assets/images/logo.png'
import { CredentialsSection, LogoSection, RegisterButtonWrapper } from '../styles/pages/Login'
import FormInput from '../components/FormInput'
import Heading from '../components/Heading'
import { AuthContext } from '../contexts/AuthContext'
import { useRouter } from 'next/router'


const Login: React.FC = () => {

  const emailInputRef = useRef<HTMLInputElement>(null)
  const passwordInputRef = useRef<HTMLInputElement>(null)
  const router = useRouter()
  const { loading, signed, signIn } = useContext(AuthContext)

  useEffect(() => {
    if(!loading) {
      if(signed) {
        router.push('/')
      }
    }
  }, [loading])

  function validateFormData () {
    let emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (!emailInputRef.current.value || !emailRegex.test(emailInputRef.current.value)) {
      return true;
    }
    if (!passwordInputRef.current.value || passwordInputRef.current.value.length < 8) {
      return true;
    }
    return false;
  }

  async function handleSignIn(event: FormEvent) {
    event.preventDefault()

    const email = emailInputRef.current.value
    const password = passwordInputRef.current.value

    const hasErrors = validateFormData();

    if (hasErrors) {
      toast.error('Error when trying to sign in');
      return
    }
    await signIn(email, password)

    return
  }

  return (
    <AuthContainer>
      <LogoSection>
        <img src={nextJSLogo} style={{ width: 320 }} />
          <Heading size={30} color='#aaa' marginTop={50} weight={500} >
            Welcome to Eletronicx, sign in now in our platform
          </Heading>
      </LogoSection>
      <CredentialsSection onSubmit={handleSignIn}>
        <FormInput ref={emailInputRef} placeholder='E-mail' type='email' required/>
        <FormInput ref={passwordInputRef} placeholder='Password' type='password' required/>
        <h3>Forgot my password</h3>
        <button type='submit'>
          Sign In
        </button>
        <RegisterButtonWrapper>
          <span>Do not have an account?  </span>
          <h3 onClick={() => router.push('/register')}>Sign Up</h3>
        </RegisterButtonWrapper>
      </CredentialsSection>
    </AuthContainer>
  )
}

export default Login
