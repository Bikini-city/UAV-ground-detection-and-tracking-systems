import styled from '@emotion/styled';
import * as Color from '../../../style/color';

export const Container = styled.div`
  width: 50rem;
  height: 50rem;
  border: 1px solid ${Color.gray};
  border-radius: 3px;
  background-color: ${Color.white};
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  position: relative;
`;

export const FileContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 45rem;
  height: 25rem;
  border: 2px solid ${Color.lightgold};
`;

export const UploadBtn = styled.label`
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: ${Color.lightgold};
  width: 10rem;
  height: 3rem;
  border-radius: 3px;
  font-size: 11px;
  cursor: pointer;
`;

export const FileInput = styled.input`
  display: none;
`;

export const ImgFile = styled.img`
  width: 45rem;
  height: 25rem;
`;

export const VideoFile = styled.video`
  width: 45rem;
  height: 25rem;
`;

export const InputContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

export const UserData = styled.div`
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: center;
  margin-right: 5px;
`;

export const UserInputLabel = styled.label`
  font-size: 1.3rem;
`;
export const UserInput = styled.input`
  width: 14rem;
  border: none;
  border-bottom: 1px solid ${Color.gray};

  &:focus {
    outline: none;
    border-bottom: 2px solid ${Color.lightgold};
  }
`;
export const SubmitBtn = styled.button`
  width: 23rem;
  height: 3.5rem;
  background-color: white;
  border-radius: 15px;
  margin-top: 5px;
  border: 2px solid ${Color.lightgold};

  &:hover {
    background-color: ${Color.lightgold};
    cursor: pointer;
  }

  &:active {
    position: relative;
    top: 2px;
  }
`;

export const Loading = styled.span`
  position: absolute;
  bottom: 60px;
  left: 50%;
  transform: translateX(-50%);
  color: ${Color.gold};
  font-weight: bold;
  font-size: 1.8rem;
`;
