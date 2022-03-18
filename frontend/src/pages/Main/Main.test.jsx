import React from 'react';
import { render } from '@testing-library/react';
import MainPage from '.';

describe('Page/Main', () => {
  it('rendering test', () => {
    const component = render(<MainPage />);

    expect(component.container.innerHTML).not.toBeNull();
  });
});
