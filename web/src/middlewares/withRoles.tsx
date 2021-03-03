import { NextComponentType } from 'next'
import { useRouter } from 'next/router'
import { useContext, useEffect } from 'react'

import { AuthContext } from '../contexts/AuthContext'


const withRoles = (Component: NextComponentType) => {
  function AuthWithRoles(props: any) {
    const { loading, signed, user } = useContext(AuthContext)
    const router = useRouter()

    useEffect(() => {
      if(!loading) {
        if(!signed) {
          router.push('/login')
        }
        else if(!user || user.role !== 'admin') {
          alert('Not enough permissions')
          router.back()
        }
      }
    }, [loading])

    return <Component {...props} />
  }

  if (Component.getInitialProps) {
    AuthWithRoles.getInitialProps = Component.getInitialProps
  }

  return AuthWithRoles
}

export { withRoles }
