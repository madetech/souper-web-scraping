import React from 'react';
import AverageChart from './AverageChart';
import CountChart from './CountChart';

const ParentChartComponent = () => {
    return (
        <div>
            <div class = "column">
            <AverageChart />
            </div>
            <div class = "column">
            <CountChart />
            </div>
        </div>
    )
}

export default ParentChartComponent;