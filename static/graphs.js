
function LoadChartData(filterType, filterValue){
    apiUrl = 'http://127.0.0.1:8000/api/filterd_data/';
     if(filterType != '' && filterValue != '')
        apiUrl = 'http://127.0.0.1:8000/api/filterd_data/?filterType='+filterType+'&filterValue='+filterValue; 

    fetch(apiUrl)
    .then(response => response.json())
    .then(data =>{
        //Get "pestle" unique values
        let uniquePestle = data
        .map((item) => item.pestle)
        .filter(
            (value, index, current_value) => current_value.indexOf(value) === index
        );
        
        graphYAxis = ["intensity", "relevance", "likelihood"]
        
        graphYAxis.forEach(yAxisValue => {
            graphInpList = []

            uniquePestle.forEach(element => {
                graphInp = {pestle: "", intensity: 0}
    
                pestleList = data.filter(item => item.pestle === element);
    
                //console.log(pestleList.map(function(item) { return item["intensity"]; }));
                //var intesityArray = Object.entries(pestleList).map(el => el[1].intesity) //Object.entries(pestleList).map(el => el[1].height);
                let intesityArray = pestleList.map(function(item) { return item[yAxisValue]; });
    
                //console.log(intesityArray);
                //var avg2 = heights.reduce((a,c) => a + c) / heights.length;
                //var avg2 = heights.reduce((a,c) => a + c) / pestleList.length;
                // console.log(avg2); // 182
    
                // Calculate the average intensity for the current pestle
                let avgIntensity = intesityArray.reduce((acc, cur) => acc + cur, 0) / intesityArray.length;
                
                // console.log(avgIntensity);
               graphInp.pestle = element;
               graphInp.intensity = parseInt(avgIntensity);//avg2;
               graphInpList.push(graphInp);
               
    
            });
            
            createChart(yAxisValue+'Chart', graphInpList.map(x => x.pestle), graphInpList.map(x => x.intensity));
        });

        
        // console.log(graphInpList.pestle)
        // //console.log(graphInpList.map(x => x.intensity))
        // // Process the fetched data
        // const intensityData = graphInp.intesity;
        // const likelihoodData = data.likelihood;
        // const relevanceData = data.relevance;
        // const yearData = data.year;
        // const countryData = data.country;
        // const topicsData = data.topics;
        // const regionData = data.region;
        // const cityData = data.city;

        // Create different charts using Chart.js
        // createChart('intensityChart', graphInpList.map(x => x.pestle), graphInpList.map(x => x.intensity));
        // createChart('likelihoodChart', ['Likelihood', "kirat", "Jitesh"], [1,2,3]);
        // createChart('relevanceChart', 'Relevance', [relevanceData]);
        // createChart('yearChart', 'Year', [yearData]);
        // createChart('countryChart', 'Country', [countryData]);
        // createChart('topicsChart', 'Topics', [topicsData]);
        // createChart('regionChart', 'Region', [regionData]);
        // createChart('cityChart', 'City', [cityData]);
    }).catch(error => console.error('Error fetching data:', error));
}

// Function to create a chart using Chart.js
function createChart(canvasId, label, data) {
    new Chart(document.getElementById(canvasId), {
        type: 'bar',
        data: {
            labels: label,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


// fetch('http://127.0.0.1:8000/api/filters/')
//     .then(response => response.json())
//     .then(data =>{
//         console.log(data)
//     }
//     ).catch(error => console.error('Error fetching data:', error));

