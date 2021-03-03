import { createGlobalStyle } from "styled-components"
import 'react-toastify/dist/ReactToastify.css';


export default createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    background: ${props => props.theme.colors.background};
    color: #e1e1e6;
    font: 400 16px Roboto, sans-serif;
    outline: 0;
    border: 0;
    height: auto;
  }
  input, button {
    outline: 0;
    border: 0;
  }
`
