import { makeDataMockup } from '../../__mocks__/data';
import { parseData } from '../data';

describe('Utils/data', () => {
  const fromDate = new Date('2020-01-01');
  const toDate = new Date('2020-04-01');
  const period = 30; // Day

  it('all dataset has valid date', () => {
    const validDataset = [
      makeDataMockup({ date: new Date('2020-01-01') }),
      makeDataMockup({ date: new Date('2020-01-22') }),
      makeDataMockup({ date: new Date('2020-03-12') }),
    ];

    const { chartFormatData, graphFormatData, countTreesData } = parseData(validDataset, fromDate, toDate, period);
    expect(countTreesData.broken).toBe(15);
    expect(countTreesData.down).toBe(15);
  });

  it('dataset has invalid date', () => {
    const validDataset = [
      makeDataMockup({ date: new Date('2019-12-01') }),
      makeDataMockup({ date: new Date('2020-01-22') }),
      makeDataMockup({ date: new Date('2020-03-12') }),
    ];

    const { chartFormatData, graphFormatData, countTreesData } = parseData(validDataset, fromDate, toDate, period);
    expect(countTreesData.broken).toBe(10);
    expect(countTreesData.down).toBe(10);
  });
});
