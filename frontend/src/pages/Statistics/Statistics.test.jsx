import React from 'react';
import { render } from '@testing-library/react';
import StatisticsPage from '.';

describe('Page/Statistics', () => {
  it('rendering test', () => {
    const component = render(<StatisticsPage />);

    component.getByText('Statistics');
  });
});
