import axios from 'axios';

/**
 * id : number
 * lat : number
 * lng : number
 * src : string
 * date: string
 * broken : number
 * down : number
 */
export const getDatas = async () => {
  const response = await axios({
    url: '/datas',
    method: 'GET',
  });

  return response.data;
};

export const createDatas = async (formData) => {
  const response = await axios({
    url: '/datas/uploads',
    method: 'POST',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

  return response.data;
};

export const deleteDatas = async ({ dataId }) => {
  const response = await axios({
    url: `/datas/${dataId}`,
    method: 'DELETE',
  });

  return response.data;
};

export const getDataImageOrVideo = async ({ dataId }) => {
  const response = await axios({
    url: `/datas/${dataId}`,
    method: 'GET',
  });

  return response.data;
};
