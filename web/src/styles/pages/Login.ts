import styled from 'styled-components';


export const LogoSection = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 450px;
`;

export const CredentialsSection = styled.form`
  display: flex;
  height: 80%;
  border-radius: 8px;
  background-color: #131317;
  flex-direction: column;
  align-items: stretch;
  padding: 70px;
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
    height: 57px;
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

export const RegisterButtonWrapper = styled.div `
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 30px;
  & > span {
    font-weight: 300;
    font-size: 16px;
    margin-right: 8px;
    color:  #aaa;
  }
  & > h3 {
    color: #5482aa;
    cursor: pointer;
    font-weight: 600;
    transition: .7s;
  }
  & > h3:hover {
    color: #5373ff;
  }
`;
