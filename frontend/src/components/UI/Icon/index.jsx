import React from 'react';
import * as Icons from './svg';
import * as Style from './styled';

function Icon({ icon, width, color = '#000' }) {
  const SVGIcons = Icons[icon];

  return (
    <Style.Container width={width}>
      <SVGIcons color={color} />
    </Style.Container>
  );
}

export default Icon;
