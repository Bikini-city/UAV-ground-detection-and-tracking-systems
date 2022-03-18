import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import GlobalStyle from '../src/style/GlobalStyle';

export const decorators = [
  (Story) => (
    <BrowserRouter>
      <Story />
      <GlobalStyle />
    </BrowserRouter>
  ),
];
