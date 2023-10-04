function init(data) {
    let info = data
    let total_disasters = [];
    for (let i = 0;  i < info.length; i++) {
      let disa = info[i]
      total_disasters.push(disa.Total_Disasters);
    }
    console.log(total_disasters);
         
    let years = [];
      for (let i = 0;  i < info.length; i++) {
        let year = info[i]
        years.push(year.Year);
    }
    console.log(years);
  
    var layout = {
      xaxis: {title:{text: 'Years'}},
      yaxis: {title:{text: 'Number of Disasters'}}
    }

    data = [{
      x: years,
      y: total_disasters}];

    Plotly.newPlot("plot", data, layout)
};

d3.json('http://127.0.0.1:5000/api/v1.0/disasters/data/per_year').then(init);