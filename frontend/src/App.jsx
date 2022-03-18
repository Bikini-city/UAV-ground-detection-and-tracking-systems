import React from 'react';
import { Routes, Route } from 'react-router-dom';
import * as Path from './Routes';
import Layout from './components/Layout';
import MainPage from './pages/Main';
import StatisticsPage from './pages/Statistics';

function App() {
  return (
    <Layout>
      <Routes>
        <Route exact path={Path.mainPath} element={<MainPage />} />
        <Route path={Path.statisticsPath} element={<StatisticsPage />} />
      </Routes>
    </Layout>
  );
}

export default App;
