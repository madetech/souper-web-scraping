import React from 'react';
import Plot from 'react-plotly.js';


export default function PlotHelper(props) {
    return (
        <Plot
        sx={{ pt: 2, pl: 8 }}
        data={[
          {
            x: props.xAxis,
            y: props.yAxis,
            type: 'scatter',
            mode: 'lines+markers',
            marker: { color: 'red' },
            name: props.trace,
          },
          { type: 'bar', x: props.xAxis, y: props.yAxis, name: props.traceType },
        ]}
        layout={{ width: 450, height: 350, title: props.title }}
        />
        );
      }
      
  