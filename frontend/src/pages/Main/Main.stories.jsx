import React from 'react';
import Layout from '../../components/Layout';
import MainPage from '.';

export default {
  title: 'Page/Main',
  component: MainPage,
};

export const mainPage = () => (
  <Layout>
    <MainPage />
  </Layout>
);
