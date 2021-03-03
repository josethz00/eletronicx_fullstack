import React, { useEffect, useState } from 'react';

import { withAuth } from '../middlewares/withAuth';
import AppContainer from '../components/AppContainer'
import Heading from '../components/Heading';
import GridSection from '../components/GridSection';
import api from '../services/api';
import { Item, ItemCreationDate, ItemPrice, ItemQuantity, ItemTitle, Wrapper } from '../styles/pages/List';
import { formatCurrency } from '../utils/formatCurrency';
import GoBack from '../components/GoBack';


interface ItemProps {
  id: number
  name: string
  price: number
  image_url: string
  quantity: string
  created_at: Date
  updated_at: Date
  category_id: number
}

const List: React.FC = () => {

  const [items, setItems] = useState<ItemProps[]>([])

  useEffect(() => {
    async function loadItems () {
      const { data } = await api.get('/items?page=1')
      setItems(data)
    }
    loadItems()
  }, [])

  return (
    <AppContainer>
      <Heading
        size={32}
        color='#fff'
        weight={500}
        marginBottom={40}
        marginTop={40}
      >
        List of Items
      </Heading>
      <GridSection>
        {items.map(item => (
          <Item key={item.id}>
            <Wrapper>
              <ItemTitle>
                Título: {item.name}
              </ItemTitle>
              <ItemPrice>
                Preço: {formatCurrency(item.price)}
              </ItemPrice>
            </Wrapper>
            <Wrapper>
              <ItemQuantity>
                Quantidade: {item.quantity}
              </ItemQuantity>
              <ItemCreationDate>
                Data de criação: {item.created_at}
              </ItemCreationDate>
            </Wrapper>
          </Item>
        ))}
      </GridSection>
      <GoBack to='/' />
    </AppContainer>
  );
}

export default withAuth(List);
