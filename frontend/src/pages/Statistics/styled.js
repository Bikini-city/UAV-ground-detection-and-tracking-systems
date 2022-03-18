import styled from '@emotion/styled';
import * as Color from '../../style/color';

export const Container = styled.div`
  width: 100%;
  height: 100%;
  display: grid;
  padding: 2rem;
  grid-template-areas:
    'title graph graph'
    'chart . count';
  grid-template-columns: 4fr 3fr 3fr;
  grid-template-rows: 5fr 5fr;
  user-select: none;

  .react-datepicker {
    font-size: 1.3rem;
  }
  .react-datepicker__header {
    padding-top: 0.8em;
  }
  .react-datepicker__month {
    margin: 0.4em 1em;
  }
  .react-datepicker__day-name,
  .react-datepicker__day {
    width: 1.9em;
    line-height: 1.9em;
    margin: 0.166em;
  }
  .react-datepicker__current-month {
    font-size: 1em;
  }
  .react-datepicker__navigation {
    top: 1em;
    line-height: 1.7em;
    border: 0.45em solid transparent;
  }
  .react-datepicker__navigation--previous {
    left: 1rem;
    top: 0.5rem;
  }
  .react-datepicker__navigation--next {
    right: 1rem;
    top: 0.5rem;
  }
`;

export const TitleWrapper = styled.div`
  grid-area: title;
`;

export const Title = styled.h2`
  margin: 0;
  font-size: 4rem;
`;

export const DateList = styled.ul`
  height: 50%;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
`;

export const DateItem = styled.li`
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 1rem 0;
`;

export const DateTitle = styled.h3`
  margin: 0;
  font-size: 2rem;
`;

export const DateInput = styled.input`
  /* display: none; */
  width: 100%;
`;

export const DateLabel = styled.label`
  font-size: 2rem;
`;

export const GraphWrapper = styled.div`
  padding-top: 7%;
  grid-area: graph;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  svg {
    font-size: 1.5rem;
  }
`;

export const ChartWrapper = styled.div`
  grid-area: chart;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const CountWrapper = styled.div`
  grid-area: count;
  position: relative;
`;

export const CountList = styled.ul`
  width: 50%;
  height: 50%;
  padding: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
`;

export const CountItem = styled.li`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

export const CountTitle = styled.h3`
  font-size: 3rem;
`;

export const CountValue = styled.span`
  font-size: 3rem;
`;

export const RangeWrapper = styled.div`
  display: flex;
  align-items: center;
  gap: 1rem;
`;

export const RangeInput = styled.input`
  -webkit-appearance: none;
  opacity: 0.7;
  width: 30rem;
  height: 3px;
  background-color: ${Color.black};
  outline: none;
  border: none;

  &::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: ${Color.gold};
    cursor: pointer;
  }
  &::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: ${Color.gold};
    cursor: pointer;
    border: none;
  }
`;

export const RangeText = styled.span`
  font-size: 1.8rem;
  font-weight: bold;
  color: ${Color.gold};
`;
