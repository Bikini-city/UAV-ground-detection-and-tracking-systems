import React, { useState } from 'react';
import ModalContainer from '../../Container/ModalContainer';
import * as Style from './styled';

function CreateModal({ closeModal, createDataset }) {
  const [userFile, setUserFile] = useState({
    file: null,
    previewURL: '',
  });

  const [userData, setUserData] = useState({
    date: new Date().toUTCString(),
    lng: 0,
    lat: 0,
  });
  const [loading, setLoading] = useState(false);

  const uploadFile = (e) => {
    e.stopPropagation();
    const reader = new FileReader();
    const file = e.target.files[0];

    reader.onloadend = () => {
      setUserFile({
        file,
        previewURL: reader.result,
      });
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  };

  const inputData = (e, key) => {
    setUserData({
      ...userData,
      [key]: e.target.value,
    });
  };

  const getPreview = () => {
    if (!userFile.file) return <></>;

    const fileExt = userFile.file.name.split('.').pop().toLowerCase();
    const extList = ['mp4', 'jpg', 'png', 'jpeg'];
    if (!extList.includes(fileExt)) return <></>;

    const isImage = userFile.file.type.includes('image/');
    if (isImage) return <Style.ImgFile name="dataset" src={userFile.previewURL} />;
    return <Style.VideoFile name="dataset" src={userFile.previewURL} controls />;
  };

  const handleCreateDataset = async () => {
    setLoading(true);
    await createDataset({ src: userFile.file, date: userData.date, lng: userData.lng, lat: userData.lat });
    setLoading(false);
  };

  return (
    <ModalContainer closeModal={closeModal}>
      <Style.Container>
        <Style.FileContainer>{getPreview()}</Style.FileContainer>
        <Style.FileInput id="upload-file" type="file" accept="image/*, video/*" multiple onChange={uploadFile} />
        <Style.UploadBtn htmlFor="upload-file">Select a file</Style.UploadBtn>
        <Style.InputContainer>
          <Style.UserData>
            <Style.UserInputLabel htmlFor="date">Date</Style.UserInputLabel>
            <Style.UserInput
              type="date"
              id="date"
              name="date"
              value={userData.date}
              onChange={(e) => inputData(e, 'date')}
            />
          </Style.UserData>
          <Style.UserData>
            <Style.UserInputLabel htmlFor="lng">Longitude</Style.UserInputLabel>
            <Style.UserInput
              type="number"
              id="lng"
              name="lng"
              value={userData.lng}
              onChange={(e) => inputData(e, 'lng')}
            />
          </Style.UserData>
          <Style.UserData>
            <Style.UserInputLabel htmlFor="lat">Latitude</Style.UserInputLabel>
            <Style.UserInput
              type="number"
              id="lat"
              name="lat"
              value={userData.lat}
              onChange={(e) => inputData(e, 'lat')}
            />
          </Style.UserData>
        </Style.InputContainer>
        <Style.SubmitBtn onClick={handleCreateDataset}>Submit</Style.SubmitBtn>
        {loading && <Style.Loading>Loading</Style.Loading>}
      </Style.Container>
    </ModalContainer>
  );
}

export default CreateModal;
