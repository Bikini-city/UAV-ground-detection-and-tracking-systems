import * as Color from '../style/color';

const getDateGap = (toDate, fromDate) => {
  const diffTime = toDate - fromDate;
  const dateGap = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return dateGap;
};

export const parseData = (dataset, fromDate, toDate, gap) => {
  const chartFormatData = [];
  const graphFormatData = [];
  const countTreesData = { broken: 0, down: 0 };
  const dateGap = getDateGap(toDate, fromDate);
  if (dateGap < gap) return { chartFormatData, graphFormatData, countTreesData };

  const treeInfos = []; // 각 날짜에 해당하는 나무들 저장
  const innerCount = Math.ceil(dateGap / gap);

  new Array(innerCount).fill(0).forEach((_, index) => {
    treeInfos.push({ broken: 0, down: 0 });
    chartFormatData.push({
      name: `${index}`,
      percentage: (100 / innerCount).toFixed(2),
      color: Color.gray,
      textColor: Color.black,
      data: [
        { name: 'broken', percentage: 0, color: Color.gold, textColor: Color.black },
        { name: 'down', percentage: 0, color: Color.black, textColor: Color.gold },
      ],
    });
    graphFormatData.push({
      name: `${index}`,
      broken: 0,
      down: 0,
    });
  });

  dataset.forEach((data) => {
    const gapOfDataAndFromDate = getDateGap(new Date(data.date), fromDate);
    const gapOfDataAndToDate = getDateGap(new Date(data.date), toDate);
    const isUnvalidData = gapOfDataAndFromDate < 0 || gapOfDataAndToDate > 0;
    if (isUnvalidData) return;

    const index = Math.floor(gapOfDataAndFromDate / gap);
    treeInfos[index].broken += data.broken;
    treeInfos[index].down += data.down;
    graphFormatData[index].broken += data.broken;
    graphFormatData[index].down += data.down;
    countTreesData.broken += data.broken;
    countTreesData.down += data.down;
  });

  treeInfos.forEach((info, index) => {
    if (info.broken === 0 && info.down === 0) return;

    chartFormatData[index].data[0].percentage = Math.floor((info.broken / (info.broken + info.down)) * 100); // broken tree
    chartFormatData[index].data[1].percentage = Math.floor((info.down / (info.broken + info.down)) * 100); // down tree
  });

  return { chartFormatData, graphFormatData, countTreesData };
};
