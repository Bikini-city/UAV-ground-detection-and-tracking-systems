import React from 'react';
import { action } from '@storybook/addon-actions';
import DateButton from '.';

export default {
  title: 'UI/DateButton',
  component: DateButton,
};

const DUMMY_DATE = '02/09/2022';
const clickButton = action('click button');

export const dateButton = () => <DateButton onClick={clickButton} value={DUMMY_DATE} />;
