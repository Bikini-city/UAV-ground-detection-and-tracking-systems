import React from 'react';
import { BrowserRouter, MemoryRouter } from 'react-router-dom';
import { render } from '@testing-library/react';
import Layout from '.';

describe('Component/Layout', () => {
  it('rendering test', () => {
    const component = render(
      <BrowserRouter>
        <Layout>
          <>text</>
        </Layout>
      </BrowserRouter>,
    );

    component.getByText('Fallen Tree Visualization');
    component.getByText('text');
  });

  it('home route test', () => {
    const component = render(
      <MemoryRouter initialEntries={['/']}>
        <Layout />
      </MemoryRouter>,
    );

    component.getByText('Fallen Tree Visualization');
  });

  it('statistics route test', () => {
    const component = render(
      <MemoryRouter initialEntries={['/statistics']}>
        <Layout />
      </MemoryRouter>,
    );

    component.getByText('Fallen Tree Visualization');
  });
});
