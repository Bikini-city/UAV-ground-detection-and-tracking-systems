import React from 'react';
import Icon from '.';
import { IconList, IconItem } from './styled';

export default {
  title: 'UI/Icon',
  component: Icon,
};

export const icon = () => (
  <IconList>
    <IconItem>
      <Icon icon="home" />
    </IconItem>
    <IconItem>
      <Icon icon="plus" />
    </IconItem>
    <IconItem>
      <Icon icon="purdue" />
    </IconItem>
    <IconItem>
      <Icon icon="statistics" />
    </IconItem>
    <IconItem>
      <Icon icon="tree" />
    </IconItem>
  </IconList>
);
