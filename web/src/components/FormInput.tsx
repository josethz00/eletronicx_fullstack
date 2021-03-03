import React, { forwardRef, InputHTMLAttributes } from 'react';

import { StyledInput } from '../styles/components/StyledInput';


interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  placeholder: string;
  type: string;
}

const FormInput: React.ForwardRefRenderFunction<HTMLInputElement, InputProps> = ({ placeholder, type, ...rest }, ref)=>{
  return(
    <StyledInput
      ref={ref}
      placeholder={placeholder}
      type={type}
      {...rest}
    />
  );
};

export default forwardRef(FormInput);
