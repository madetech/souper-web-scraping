import React from "react";
import { Chart } from "react-google-charts";

export const data = [
  ["Stage", "Average Met", "Average NotMet", "Median Met", "Median NotMet"],
  ["Alpha", 165, 938, 522, 998],
  ["Beta", 135, 1120, 599, 1268],
  ["Live", 157, 1167, 587, 807],
];

export const options = {
  title: "Stage Times",
  vAxis: { title: "Days" },
  hAxis: { title: "Stage" },
  seriesType: "bars",
};

export function AverageChart() {
  return (
    <Chart
      chartType="ComboChart"
      width="100%"
      height="400px"
      data={data}
      options={options}
    />
  );
}
