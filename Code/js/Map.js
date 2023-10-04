function makeMap(info) {
    let worldmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    let base = {
        "Map": worldmap
    }

    let overlay = {
        "Countries": info
    };

    let myMap = L.map("map", {
        center: [37.09024, -95.7129],
        zoom: 5,
        layers: [worldmap, info]
    });
    
    l.control.layers(base, overlay, {
        collapsed: false
    }).addTo(myMap)

}

function markers(info){
    let countries = info

    let countryMarkers =[]

    for (let i = 0; i < countries.length; i++) {
        let coun = countries[i];

        let marker =  L.marker([coun.lat, coun.lon])
        .bindPopup("<h3>" + coun.Country + "<h3><h3>Total Disasters: " + coun.total_dis + "<h3><h3>Total Deaths: " + coun.Total_deaths + "<h3><h3>Total Damages: $" + coun.Total_Damages)

        countryMarkers.push(marker);
    }

    makeMap(L.layerGroup(countryMarkers));

}

d3.json("http://127.0.0.1:5000/api/v1.0/disasters/final_data").then(markers);