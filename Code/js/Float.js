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

        let info = data
        let countries = [];
        for (let i = 0;  i < info.length; i++) {
            let coun = info[i];
            countries.push(coun.Country);
        }

        let disasters = [];

        for (let i = 0; i < countries.length; i++){
            selectedCountry = countries[i];
            if (dataset == countries){
                disasters.push(info[i]['animal_acc']);
                disasters.push(info[i]['drought']);
                disasters.push(info[i]['earthquake']);
                disasters.push(info[i]['epidemic']);
                disasters.push(info[i]['extreme_temp']);
                disasters.push(info[i]['flood']);
                disasters.push(info[i]['glacial']);
                disasters.push(info[i]['impact']);
                disasters.push(info[i]['insect']);
                disasters.push(info[i]['lanslide']);
                disasters.push(info[i]['mass_move']);
                disasters.push(info[i]['storm']);
                disasters.push(info[i]['volcano']);
                disasters.push(info[i]['wildfire']);
            
            }
        }

        labels = ['animal_acc', 'drought', 'earthquake', 'epidemic', 'extreme_temp', 'flood', 'glacial',
        'impact', 'insect', 'lanslide', 'mass_move', 'storm', 'volcano', 'wildfire']
    

        let stuff =[{
            values: disasters,
            labels: labels,
            type: "pie"
        }]
        console.log(stuff);
        
        Plotly.newPlot("pie", stuff)
    });
}

d3.json('http://127.0.0.1:5000/api/v1.0/disasters/final_data').then(init);
d3.selectAll("#selDataset").on("optionChanged(this.value)", optionChanged);
//$('#selDataset').on('change', optionChanged);