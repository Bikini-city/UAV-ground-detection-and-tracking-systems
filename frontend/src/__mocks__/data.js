export const makeDataMockup = ({
  id = Math.floor(Math.random() * 100),
  lat = 40.42409882753435,
  lng = -86.91777942906364,
  src = '/media/%EC%84%9C%EB%AA%85_gtv1QSR.jpg',
  date = new Date(),
  broken = 5,
  down = 5,
} = {}) => ({
  id,
  lat,
  lng,
  src,
  date,
  broken,
  down,
});
