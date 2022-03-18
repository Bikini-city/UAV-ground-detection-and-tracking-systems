import React from 'react';
import { Marker } from 'react-map-gl';
import * as Style from './styled';

function CustomMarker({ lng, lat, onClickMarker }) {
  return (
    <Marker longitude={lng} latitude={lat} onClick={onClickMarker}>
      <Style.Marker />
    </Marker>
  );
}

export default CustomMarker;
