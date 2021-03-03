import { useRouter } from 'next/router'
import { useState, useEffect } from 'react'
import { toast } from 'react-toastify'

import api from '../services/api'
import { isTokenExpired } from '../utils/isTokenExpired'


interface User {
  id: number
  username: string
  email: string
  role: string
}


const useAuth = () => {

  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  const router = useRouter()

  useEffect(()=>{
    function loadStorageData() {
      const storagedUser = localStorage.getItem('@eletronicx:user')
      const storagedToken = localStorage.getItem('@eletronicx:auth_token')

      if(storagedUser && storagedToken) {
        if(isTokenExpired(storagedToken)) {
          signOut()
          return
        }
        api.defaults.headers['authorization'] = `Bearer ${storagedToken}`
        setUser(JSON.parse(storagedUser))
        setLoading(false)
      }
      else if (!storagedUser || !storagedToken) {
        setLoading(false)
      }
      else {
        setLoading(false)
      }
    }
    loadStorageData()
  }, [])

  async function signIn(email: string, password: string) {
    try {
      const response = await api.post('/users/auth', {
        email,
        password
      })

      setUser(response.data)

      localStorage.setItem('@eletronicx:user', JSON.stringify(response.data))
      localStorage.setItem('@eletronicx:auth_token', response.data.token)

      toast.success(`Welcome ${response.data.username}`)
      router.push('/')
    }
    catch(err) {
      toast.error('Error when trying to sign in')
    }

    return
  }

  function signOut() {
    localStorage.clear()
    setUser(null)
    router.push('/login')
  }

  return {
    signed: Boolean(user),
    user,
    loading,
    signIn,
    signOut
  }

}

export { useAuth }
export type { User }

