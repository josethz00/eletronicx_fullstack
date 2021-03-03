import React from 'react';

import { StyledGridSection } from '../styles/components/StyledGridSection';


const GridSection: React.FC = ({ children }) => {
  return (
    <StyledGridSection>
      {children}
    </StyledGridSection>
  );
}

export default GridSection;
