import React from 'react';
import { action } from '@storybook/addon-actions';
import CreateModal from '.';

export default {
  title: 'Component/CreateModal',
  component: CreateModal,
};

const closeModalAction = action('close modal');
const createDatasetAction = action('create dataset');

export const createModal = () => <CreateModal closeModal={closeModalAction} createDataset={createDatasetAction} />;
