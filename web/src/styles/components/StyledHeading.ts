import styled from "styled-components";
import { HeadingProps } from "../../components/Heading";


export const StyledHeading = styled.h1<HeadingProps>`
  margin-top: ${props => props.marginTop + 'px'};
  font-size: ${props => props.size + 'px'};
  color: ${props => props.color};
  font-weight: ${props => props.weight};
  align-self: ${props => props.alignSelf};
  margin-bottom: ${props => props.marginBottom + 'px'};
  margin-left: ${props => props.marginLeft + 'px'};
  margin-right: ${props => props.marginRight + 'px'};
`;
