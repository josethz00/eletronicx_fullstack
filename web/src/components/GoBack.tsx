import { useRouter } from 'next/router';
import React from 'react';
import { FiArrowLeft } from 'react-icons/fi';

import { StyledGoBack, StyledGoBackText } from '../styles/components/StyledGoBack';


interface GoBackProps {
  to: string
}

const GoBack: React.FC<GoBackProps> = ({ to }) => {

  const router = useRouter()

  return (
    <StyledGoBack onClick={() => router.push(to)}>
      <FiArrowLeft color='#5271ff' size={28}/>
      <StyledGoBackText>
        Back to Home
      </StyledGoBackText>
    </StyledGoBack>
  );
}

export default GoBack;
