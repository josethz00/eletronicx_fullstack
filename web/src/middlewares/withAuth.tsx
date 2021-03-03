import { NextComponentType } from 'next'
import { useRouter } from 'next/router'
import { useContext, useEffect } from 'react'

import { AuthContext } from '../contexts/AuthContext'


const withAuth = (Component: NextComponentType) => {
  function Auth(props: any) {
    const { loading, signed } = useContext(AuthContext)
    const router = useRouter()

    useEffect(() => {
      if(!loading) {
        if(!signed) {
          router.push('/login')
        }
      }
    }, [loading])

    return <Component {...props} />
  }

  if (Component.getInitialProps) {
    Auth.getInitialProps = Component.getInitialProps
  }

  return Auth
}

export { withAuth }
