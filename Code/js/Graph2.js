function init() {
    d3.json('http://127.0.0.1:5000/api/v1.0/disasters/final_data').then(function(data) {
        countries = [];
        for (let i = 1;  i < data.length; i++) {
            let coun = data[i];
            countries.push(coun.Country);
        }

        for (let i=0; i < countries.length; i++) {
            $('#selDataset').append($('<option>', {value: countries[i], text:countries[i]}));
        }

        disasters = [];
        for (let i=0; i < 14; i++) {
            disasters.push(Object.values(data[1][1+i])); //change for data
        }

        labels = [];
        for (let i=0; i <14; i++) {
            labels.push(Object.keys(data[1][1+i]));
        }

        let info = [{
            values: disasters,
            labels: labels,
            type: "pie"
        }]

        let layout = {
            title: 'Percentages of Disaster Types',
            height: 500,
            width: 500
        }

        Plotly.newPlot("pie", info, layout)

    });
}


function dropDown() {
    d3.json('http://127.0.0.1:5000/api/v1.0/disasters/final_data').then(function(data) {
        let dropdown = d3.select('selDataset');
        let dataset = dropdown.property('value');
        countries = [];
        for (let i = 1;  i < data.length; i++) {
            countries.push(data[i].country);
        }

        let disasters = [];

        for (let i = 0; i < countries.length; i++) {
            selected = countries[i];
            if (dataset == selected) {
                for (let info = 0; i < 14; i++) {
                    disasters.push(Object.values(data[1][1+i])); //change for data
                }
            }
        }
        let info = [{
            values: disasters,
            labels: labels,
            type: "pie"
        }];

        let layout = {
            title: 'Percentages of Disaster Types',
            height: 500,
            width: 500
        };

    Plotly.newPlot("pie", info, layout)
    });

}

init();

d3.selectAll('#selDataset').on("dropDown(this.value)", dropDown);
