
import React from 'react';
import Navbar from './Components/Navbar';
import ReportList from './Components/ReportList.js';
import ReportSectionCount from './Components/ReportSectionCount.js';
import CountChart from './Components/charts/CountChart';
import AverageChart from './Components/charts/AverageChart';
import ParentChartComponent from './Components/charts/ParentChart.js';

export default function App() {
  return (
    <div className="App">
      <React.Fragment>
        <Navbar/>
        <CountChart/>
        <AverageChart/>
        <ReportSectionCount/>
        {/* <ReportList /> */}
      </React.Fragment>
    </div>
  )
}

