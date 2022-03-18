import React from 'react';
import Layout from '../../components/Layout';
import StatisticsPage from '.';

export default {
  title: 'Page/Statistics',
  component: StatisticsPage,
};

export const statisticsPage = () => (
  <Layout>
    <StatisticsPage />
  </Layout>
);
