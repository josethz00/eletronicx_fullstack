import styled from 'styled-components';


export const LogoSection = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 450px;
`;

export const CredentialsSection = styled.div`
  display: flex;
  height: 90%;
  background-color: #131317;
  border-radius: 8px;
  flex-direction: column;
  align-items: stretch;
  padding: 40px 60px;
  & > h3 {
    margin-left: 5px;
    margin-top: 2px;
    cursor: pointer;
    color: #5482aa;
    font-weight: 600;
    transition: .7s;
  }
  & > h3:hover {
    color: #5373ff;
  }
  & > button {
    margin-top: 35px;
    height: 62px;
    border: 0px;
    border-radius: 8px;
    color:#ccc;
    cursor: pointer;
    font-size: 18px;
    font-weight: 800;
    background-color: #5271ff;
    transition: .4s;
  }
  & > button:hover {
    background-color: #5354ff;
  }
`;

export const BackButtonWrapper = styled.div `
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 30px;
  cursor: pointer;
  margin-top: 30px;
  color: #5482aa;
  &:hover {
    color: #5373ff;
  }
  & > span {
    font-weight: 600;
    font-size: 18px;
    color: #aaa
  }

  & > .arrow-icon {
    margin-right: 12px;
  }
`;
