import { Chart } from "react-google-charts";
import getChartAverage from "../../RemoteUseCases/ChartCountFetcher";

export default function AverageChart() {
  const data = async () => {await getChartAverage();
  };

  const options = {
    title: "Stage Averages",
    vAxis: { title: "Days" },
    hAxis: { title: "Stage" },
    seriesType: "bars",
    legend: { position: "right" },
  };

  return (
    <Chart
      chartType="BarChart"
      width="100%"
      height="400px"
      data={data}
      options={options}
    />
  );
}
