import React from "react";
import { Chart } from "react-google-charts";

const met = [
  ["Stage", "Count"],
  ["Alpha", 250],
  ["Beta", 420],
  ["Live", 290],
];

const notMet = [
  ["Stage", "Count"],
  ["Alpha", 37],
  ["Beta", 60],
  ["Live", 70],
];

export const diffdata = {
  old: met,
  new: notMet,
};

export const options = {
  legend: { position: "bottom" },
  title: "Count by stage",
};

export function App() {
  return (
    <Chart
      chartType="BarChart"
      width="100%"
      height="400px"
      diffdata={diffdata}
      options={options}
    />
  );
}
