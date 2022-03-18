import React, { useEffect, useState } from 'react';
import Map from '../../components/UI/Map';

import Icon from '../../components/UI/Icon';
import { getDatas, createDatas, deleteDatas } from '../../api/data';
import * as Style from './styled';
import * as Color from '../../style/color';
import MarkerModal from '../../components/UI/MarkerModal';
import CreateModal from '../../components/UI/CreateModal';

function Main() {
  const [dataset, setDataset] = useState([]);
  const [selectedData, setSelectedData] = useState();
  const [map, setMap] = useState();
  const [showTree, setShowTree] = useState(false);
  const [createModalOpen, setCreateModalOpen] = useState(false);

  const initDataset = async () => {
    const datasetFromServer = await getDatas();
    setDataset(datasetFromServer);
  };

  useEffect(() => {
    initDataset();
  }, []);

  const onClickMarker = (id) => {
    const data = dataset.find((d) => d.id === id);
    setSelectedData(data);
  };

  const closeModal = () => {
    setSelectedData(undefined);
    setCreateModalOpen(false);
  };

  const createDataset = async ({ src, date, lat, lng }) => {
    const formData = new FormData();
    formData.append('src', src);
    formData.append('date', date);
    formData.append('lat', lat);
    formData.append('lng', lng);

    const data = await createDatas(formData);
    setDataset([...dataset, data]);
    setCreateModalOpen(false);
  };

  const deleteDataset = async ({ dataId }) => {
    await deleteDatas({ dataId });
    const filteredDataset = dataset.filter((data) => data.id !== dataId);
    setDataset(filteredDataset);
    setSelectedData(null);
  };

  return (
    <Style.Container>
      {selectedData && <MarkerModal data={selectedData} closeModal={closeModal} deleteDataset={deleteDataset} />}
      {createModalOpen && <CreateModal closeModal={closeModal} createDataset={createDataset} />}
      <Map getMap={setMap} markers={dataset} onClickMarker={onClickMarker} />
      <Style.AddButton onClick={() => setCreateModalOpen(!createModalOpen)}>
        <Icon icon="plus" />
      </Style.AddButton>
      <Style.TreeButton onClick={() => setShowTree(!showTree)}>
        <Icon icon="tree" color={showTree ? Color.gray : Color.black} />
      </Style.TreeButton>
    </Style.Container>
  );
}

export default Main;
