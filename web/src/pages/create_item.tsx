import React from 'react';

import { withRoles } from '../middlewares/withRoles';
import AppContainer from '../components/AppContainer';


const CreateItem: React.FC = () => {
  return (
    <AppContainer>

    </AppContainer>
  );
}

export default withRoles(CreateItem);
