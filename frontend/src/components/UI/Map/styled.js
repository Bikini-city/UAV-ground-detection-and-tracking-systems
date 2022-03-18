import styled from '@emotion/styled';

/**
 * Map
 */
export const Container = styled.div`
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  height: 100%;
  width: 100%;

  .mapboxgl-ctrl-logo,
  .mapboxgl-ctrl-attrib-inner {
    display: none;
  }
`;

/**
 * Marker
 */
export const Marker = styled.div`
  width: 1rem;
  height: 1rem;
  border-radius: 0.5rem;
  background-color: red;
  cursor: pointer;
`;
