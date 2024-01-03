
import React from 'react';
import Navbar from './Components/Navbar';
import ReportList from './Components/ReportList.js';
import CountChart from './Components/charts/CountChart';
import AverageChart from './Components/charts/AverageChart';
import ParentChartComponent from './Components/charts/ParentChart.js';

export default function App() {
  return (
    <div className="App">
      <React.Fragment>
        <Navbar 
        />
        <div class="container">
          <div class="column">
        <CountChart/>
        </div>
        <div class="column">
          <AverageChart/> 
        </div>
        </div>
        {/* <ParentChartComponent /> */}
        <ReportList />
      </React.Fragment>
    </div>
  )
}

