import React, { useEffect, useState } from 'react';
import Modalhelper from '../Helpers/ModalHelper';
import { Chart } from "react-google-charts";

export default function ChartModal() {
  return (
    <Modalhelper>
      <Chart
        chartType="ComboChart"
        width="100%"
        height="400px"
        data={[
          ["Stage", "Average Met", "Average NotMet", "Median Met", "Median NotMet"],
          ["Alpha", 165, 938, 522, 998],
          ["Beta", 135, 1120, 599, 1268],
          ["Live", 157, 1167, 587, 807],
        ]}
        options={{
          title: "Stage Times",
          vAxis: { title: "Days" },
          hAxis: { title: "Stage" },
          seriesType: "bars",
        }}
      />
    </Modalhelper>
  )
}


