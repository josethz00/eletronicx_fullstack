import React from 'react';

import { StyledAppContainer } from '../styles/components/StyledAppContainer';

const AppContainer: React.FC = ({ children }) => {
  return (
    <StyledAppContainer>
      {children}
    </StyledAppContainer>
  );
}

export default AppContainer;
