import { Chart } from "react-google-charts";
import getChartAverage from "../../RemoteUseCases/ChartAverageFetcher";
import { useEffect, useState } from "react";

export default function AverageChart() {

  const [data, setReport] = useState([]);

  useEffect(() => {
    const fetchReport = async () => {
      setReport(await getChartAverage());
    };

    fetchReport();
  }, [])

  const options = {
    title: "Averages of days per stage",
    vAxis: { title: "Stages" },
    hAxis: { title: "Days" },
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
