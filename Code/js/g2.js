function init(data) {
    let info = data
    let countries = [];
    for (let i = 0;  i < info.length; i++) {
        let coun = info[i];
        countries.push(coun.Country);
    }
    
    for (i=0; i<countries.length; i++){
        $('#selDataset').append($('<option>', {value: countries[i], text:countries[i]}));
    }


    let disasters = [];

    disasters.push(info[0]['animal_acc']);
    disasters.push(info[0]['drought']);
    disasters.push(info[0]['earthquake']);
    disasters.push(info[0]['epidemic']);
    disasters.push(info[0]['extreme_temp']);
    disasters.push(info[0]['flood']);
    disasters.push(info[0]['glacial']);
    disasters.push(info[0]['impact']);
    disasters.push(info[0]['insect']);
    disasters.push(info[0]['lanslide']);
    disasters.push(info[0]['mass_move']);
    disasters.push(info[0]['storm']);
    disasters.push(info[0]['volcano']);
    disasters.push(info[0]['wildfire']);

    labels = ['animal_acc', 'drought', 'earthquake', 'epidemic', 'extreme_temp', 'flood', 'glacial',
                'impact', 'insect', 'lanslide', 'mass_move', 'storm', 'volcano', 'wildfire'
]

    console.log(disasters);

    
    let stuff = [{
        values: disasters,
        labels: labels,
        type: "pie"
    }]
    Plotly.newPlot("pie", stuff)

};

function optionChanged() {
    d3.json('http://127.0.0.1:5000/api/v1.0/disasters/final_data').then(function(data) {
        let dropdown = d3.select('#selDataset');
        let dataset = dropdown.property('value');

        let info = data;
        let selectedData = info.find(country => country.Country === dataset);

        // Check if a matching country is found
        if (selectedData) {
            let disasters = labels.map(label => selectedData[label]);
            
            let stuff = [{
                values: disasters,
                labels: labels,
                type: "pie"
            }];

            Plotly.newPlot("pie", stuff);
        }
    });
}

d3.json('http://127.0.0.1:5000/api/v1.0/disasters/final_data').then(init);
d3.selectAll("#selDataset").on("optionChanged(this.value)", optionChanged);