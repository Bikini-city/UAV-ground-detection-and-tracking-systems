import styled from '@emotion/styled';
import * as Color from '../../style/color';

export const Container = styled.div`
  position: relative;
  width: 100%;
  height: 100%;
`;

export const AddButton = styled.button`
  padding: 1rem;
  width: 5rem;
  height: 5rem;
  right: 2rem;
  top: 2rem;
  position: absolute;

  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  background-color: ${Color.white};
  cursor: pointer;
  -webkit-box-shadow: 2px 2px 8px 5px rgba(0, 0, 0, 0.3);
  box-shadow: 2px 2px 8px 5px rgba(0, 0, 0, 0.3);

  &:active {
    width: 4rem;
    height: 4rem;
    top: 2.5rem;
    right: 2.5rem;
  }
`;

export const TreeButton = styled.button`
  padding: 1rem;
  width: 5rem;
  height: 5rem;
  right: 2rem;
  top: 50%;
  position: absolute;
  transform: translateY(-50%);

  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  background-color: ${Color.white};
  cursor: pointer;
  -webkit-box-shadow: 2px 2px 8px 5px rgba(0, 0, 0, 0.3);
  box-shadow: 2px 2px 8px 5px rgba(0, 0, 0, 0.3);
`;
