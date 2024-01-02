import React from "react";
import { Chart } from "react-google-charts";

export const data = [["Stage", "Met", "Not Met"],["Alpha", 20, 5],["Beta", 10, 8],["Live", 35, 7]];

export const options = {
  title: "Stage Times",
  vAxis: { title: "Days" },
  hAxis: { title: "Stage" },
  seriesType: "bars",
  legend: { position: "right" },
};

export function countChart() {
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
