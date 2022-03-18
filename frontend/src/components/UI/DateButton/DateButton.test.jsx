import React from 'react';
import { render } from '@testing-library/react';
import DateButton from '.';

const DUMMY_DATE = '02/09/2022';
const clickButtonMockFn = jest.fn();

describe('Component/UI/DateButton', () => {
  it('rendering test', () => {
    const component = render(<DateButton onClick={clickButtonMockFn} value={DUMMY_DATE} />);

    component.getByText('02 . 09 . 2022');
  });
});
