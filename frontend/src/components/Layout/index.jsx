import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import Icon from '../UI/Icon';
import * as Style from './styled';
import * as Color from '../../style/color';

function Layout({ children }) {
  const { pathname } = useLocation();

  return (
    <Style.Container>
      <Style.Header>
        <Icon icon="purdue" width="7rem" />
        <Style.Title>Fallen Tree Visualization</Style.Title>
      </Style.Header>
      <Style.Nav>
        <Style.IconWrapper>
          <Link to="/">
            <Icon color={pathname === '/' ? Color.gold : Color.gray} icon="home" width="70%" />
          </Link>
        </Style.IconWrapper>
        <Style.IconWrapper>
          <Link to="/statistics">
            <Icon color={pathname === '/statistics' ? Color.gold : Color.gray} icon="statistics" width="70%" />
          </Link>
        </Style.IconWrapper>
      </Style.Nav>
      <Style.Children>{children}</Style.Children>
    </Style.Container>
  );
}

export default Layout;
