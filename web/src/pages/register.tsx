import React, { useContext, useEffect, useRef } from 'react'
import { FiArrowLeft } from 'react-icons/fi'
import { toast } from 'react-toastify'
import { useRouter } from 'next/router'

import AuthContainer from '../components/AuthContainer'
import nextJSLogo from '../assets/images/logo.png'
import { CredentialsSection, LogoSection, BackButtonWrapper } from '../styles/pages/Register'
import FormInput from '../components/FormInput'
import Heading from '../components/Heading'
import api from '../services/api'
import { AuthContext } from '../contexts/AuthContext'


const Register: React.FC = () => {

  const usernameInputRef = useRef(null)
  const emailInputRef = useRef(null)
  const passwordInputRef = useRef(null)
  const passwordConfirmationInputRef = useRef(null)

  const router = useRouter()
  const { loading, signed, signIn } = useContext(AuthContext)

  useEffect(() => {
    if(!loading) {
      if(signed) {
        router.push('/')
      }
    }
  }, [loading])

  async function handleSignUp() {
    try {
      const { data } = await api.post('/users', {
        username: usernameInputRef.current.value,
        email: emailInputRef.current.value,
        role: 'client',
        password: passwordInputRef.current.value,
        password_confirmation: passwordConfirmationInputRef.current.value
      })
      toast.success(data.success)
      router.push('/login')
    }
    catch (err) {
      toast.error('Cannot register new user')
    }
  }

  return (
    <AuthContainer>
      <CredentialsSection>
        <Heading alignSelf='center' marginBottom={15} size={30} color='#aaa' marginTop={0} weight={700}>
          Create an account
        </Heading>
        <FormInput ref={usernameInputRef} placeholder='Username' type='text' required/>
        <FormInput ref={emailInputRef} placeholder='E-mail' type='email' required/>
        <FormInput ref={passwordInputRef} placeholder='Password' type='password' required/>
        <FormInput ref={passwordConfirmationInputRef} placeholder='Password confirmation' type='password' required/>
        <button onClick={handleSignUp}>
          Sign Up
        </button>
      </CredentialsSection>
      <LogoSection>
        <img alt='Logo' style={{ width: 290 }} src={nextJSLogo} />
        <Heading size={30} color='#aaa' marginTop={50} weight={700} >
         Register on the platform and have access to various products
        </Heading>
        <BackButtonWrapper onClick={() => {}}>
          <FiArrowLeft size={20} className='arrow-icon' />
          <span>Back to sign in  </span>
        </BackButtonWrapper>
      </LogoSection>
    </AuthContainer>
    )
}

export default Register
