import styled from '@emotion/styled';
import * as Color from '../../../style/color';

export const Container = styled.div`
  width: 60rem;
  height: 60rem;
  border: 1px solid ${Color.gray};
  border-radius: 3px;
  background-color: ${Color.white};
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const Img = styled.img`
  width: 60rem;
  height: 45rem;
  object-fit: contain;
  background-color: #000;
`;

export const Video = styled.video`
  width: 60rem;
  height: 45rem;
`;

export const CloseButton = styled.button`
  position: absolute;
  padding: 0;
  top: 1rem;
  right: 1rem;
  width: 2.5rem;
  height: 2.5rem;

  z-index: 100;
  border: none;
  background-color: transparent;
`;

export const DeleteButton = styled.button`
  margin-top: 2rem;
  font-size: 1.5rem;
  width: 23rem;
  height: 3.5rem;
  background-color: white;
  border-radius: 15px;
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

export const Species = styled.div`
  margin-top: 0.5rem;
  font-size: 1.5rem;
`;

export const Count = styled.span`
  color: ${Color.gold};
  font-weight: bold;
  font-size: 1.8rem;
`;
