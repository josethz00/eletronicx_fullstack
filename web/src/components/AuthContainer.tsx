import React from 'react';

import { StyledAuthContainer } from '../styles/components/StyledAuthContainer';

const AuthContainer: React.FC = ({ children }) => {
  return (
    <StyledAuthContainer>
      {children}
    </StyledAuthContainer>
  );
}

export default AuthContainer;
