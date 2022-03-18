import React from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';
import GlobalStyle from './style/GlobalStyle';
import App from './App';

axios.defaults.baseURL = `${process.env.SERVER_URL}`;

ReactDom.render(
  <BrowserRouter>
    <GlobalStyle />
    <App />
  </BrowserRouter>,
  document.getElementById('app'),
);
