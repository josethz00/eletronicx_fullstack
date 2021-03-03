import React, { createContext } from 'react'

import { useAuth, User } from '../hooks/useAuth'


interface AuthContextData {
  signed:boolean
  user: User | null
  loading: boolean
  signIn(email: string, password: string): Promise<void>
  signOut(): void
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData)

const AuthProvider: React.FC = ({ children }) => {

  const { signed, user, loading, signIn, signOut } = useAuth();

  return(
    <AuthContext.Provider value={{
      signed,
      user,
      loading,
      signIn,
      signOut
    }}>
      {children}
    </AuthContext.Provider>
  );

};

export default AuthProvider
export { AuthContext }
