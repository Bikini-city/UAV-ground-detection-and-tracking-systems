import React from 'react';
import Icon from '../Icon';
import ModalContainer from '../../Container/ModalContainer';
import * as Style from './styled';

function MarkerModal({ data, closeModal, deleteDataset }) {
  const imgExtList = ['jpg', 'png', 'jpeg'];
  const isInclude = imgExtList.filter((ext) => data.src.includes(ext));

  return (
    <ModalContainer closeModal={closeModal}>
      <Style.CloseButton onClick={closeModal}>
        <Icon icon="close" />
      </Style.CloseButton>
      <Style.Container>
        {isInclude.length ? <Style.Img src={data.src} /> : <Style.Video src={data.src} controls />}
        <Style.Species>
          Broken:
          <Style.Count> {data.broken}</Style.Count>
        </Style.Species>
        <Style.Species>
          Down:
          <Style.Count> {data.down}</Style.Count>
        </Style.Species>
        <Style.DeleteButton onClick={() => deleteDataset({ dataId: data.id })}>Delete</Style.DeleteButton>
      </Style.Container>
    </ModalContainer>
  );
}

export default MarkerModal;
