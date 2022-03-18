import styled from '@emotion/styled';
import * as Color from '../../style/color';

export const Container = styled.main`
  width: 100vw;
  height: 100vh;
  display: grid;
  grid-template-areas:
    'header header'
    'nav main';
  grid-template-columns: 8rem 20fr;
  grid-template-rows: 8rem 10fr;
`;

export const Header = styled.header`
  position: relative;
  grid-area: header;
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  padding-left: 0.5rem;
  z-index: 1000;
  background-color: ${Color.white};
  border-bottom: 2px solid ${Color.gold};
`;

export const Title = styled.h1`
  position: absolute;
  margin: 0;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  color: ${Color.gold};
  user-select: none;
`;

export const Nav = styled.nav`
  grid-area: nav;
  padding: 2rem 0;
  width: 100%;
  height: 100%;
  z-index: 500;
  background-color: ${Color.white};
  border-right: 2px solid ${Color.gold};
`;

export const IconWrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 3rem;
  cursor: pointer;

  a {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
`;

export const Children = styled.div`
  grid-area: main;
`;
