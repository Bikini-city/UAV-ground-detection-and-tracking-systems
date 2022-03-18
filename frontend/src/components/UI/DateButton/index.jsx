import React, { forwardRef } from 'react';
import * as Style from './styled';

function DateButton({ value, onClick }, ref) {
  const parseDate = (date) => {
    const [mm, dd, yyyy] = date.split('/');

    return `${mm} . ${dd} . ${yyyy}`;
  };

  return (
    <Style.Button type="button" onClick={onClick} ref={ref}>
      {parseDate(value)}
    </Style.Button>
  );
}

export default forwardRef(DateButton);
