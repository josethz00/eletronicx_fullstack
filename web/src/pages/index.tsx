import { useRouter } from 'next/router'
import React, { useContext } from 'react'

import AppContainer from '../components/AppContainer'
import GridSection from '../components/GridSection'
import Heading from '../components/Heading'
import { AuthContext } from '../contexts/AuthContext'
import { withAuth } from '../middlewares/withAuth'
import { ButtonLink } from '../styles/pages/Home'


const Home: React.FC = () => {

  const router = useRouter()
  const { user, signOut } = useContext(AuthContext)

  function navigateTo(url: string) {
    router.push(url)
    return
  }

  return (
    <AppContainer>
      <Heading
        size={60}
        color='#fff'
        weight={500}
        marginBottom={40}
      >
        Page Links
      </Heading>
      <GridSection>
        <ButtonLink onClick={() => navigateTo('/list')}>
          See Items List
        </ButtonLink>
        <ButtonLink
          onClick={() => navigateTo('/create_item')}
          disabled={user && user.role !== 'admin'}
          style={{
            backgroundColor: user && user.role !== 'admin' ? '#889' : '#5271ff',
            cursor: 'default'
          }}
        >
          Create Item
        </ButtonLink>
        <ButtonLink
          onClick={() => navigateTo('/create_category')}
          disabled={user && user.role !== 'admin'}
          style={{
            backgroundColor: user && user.role !== 'admin' ? '#889' : '#5271ff',
            cursor: 'default'
          }}
        >
          Create Category
        </ButtonLink>
        <ButtonLink onClick={() => signOut()}>
          Sign Out
        </ButtonLink>
      </GridSection>
    </AppContainer>
  )
}

export default withAuth(Home)
