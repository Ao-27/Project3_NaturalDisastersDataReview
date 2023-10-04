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
    let countries = info.data;

    let countryMarkers =[]

    for (let i = 0; i < countries.length; i++) {
        let country = countries[i];

        let marker =  L.marker([country.lat, country.lon])
        .bindPopup("<h3>" + country.Country + "<h3><h3>Disasters: " + country.flood_total + ...)

        countryMarkers.push(marker);
    }

    makeMap(L.layerGroup(bikeMarkers));

}

d3.json("http://127.0.0.1:5000/api/v1.0/disasters/data").then(markers);