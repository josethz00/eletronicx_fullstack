import React from 'react';
import { StyledHeading } from '../styles/components/StyledHeading';


export interface HeadingProps{
  size: number;
  color: string;
  marginTop?: number;
  weight: number;
  alignSelf?: string;
  marginBottom?: number;
  marginLeft?: number;
  marginRight?: number;
}

const Heading: React.FC<HeadingProps> = ({
  size,
  color,
  marginTop,
  weight,
  alignSelf,
  marginBottom,
  marginLeft,
  marginRight,
  children
}) => {

  return (
    <StyledHeading
      size={size}
      color={color}
      weight={weight}
      marginTop={marginTop}
      alignSelf={alignSelf}
      marginBottom={marginBottom}
      marginLeft={marginLeft}
      marginRight={marginRight}
    >
      {children}
    </StyledHeading>
  );

};

export default Heading;
