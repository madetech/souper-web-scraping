import { Chart } from "react-google-charts";
import getChartCount from "../../RemoteUseCases/ChartCountFetcher";
import { useEffect, useState } from "react";

export default function CountChart() {

  // var data = [["Stage", "Met", "Not Met"],["Alpha", 0, 0],["Beta", 0, 0],["Live", 0, 0]]

  const [data, setReport] = useState([]);

  useEffect(() => {
    const fetchReport = async () => {
      setReport(await getChartCount());
    };

    fetchReport();
  }, [])

  const options = {
    title: "Count of Projects at each stage",
    vAxis: { title: "Stage" },
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
