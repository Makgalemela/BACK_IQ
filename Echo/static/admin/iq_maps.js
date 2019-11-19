
$(function () {

 $('.DeviceLocation').click(function() {  

 	$.ajax({
 			async: false,
 			type: 'GET',
 			url : "https://iqmediaapp.herokuapp.com/api/"+$(this).attr('data-idll'),
 			datatype : "json",
 			success : function(data){
		 		var latitude = parseFloat(data.latitude);
		  		var longitude = parseFloat(data.longitude);
		        mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nocm9vZGluZ2VyIiwiYSI6ImNrMnpmbGthbzBnenQzbW9tbGJqbTN2d3UifQ.Dkye4BD0DH1eVWbDUqBmPw';
			    var map = new mapboxgl.Map({
		          container: 'map',
		          style: 'mapbox://styles/mapbox/streets-v11',
		          center : [latitude,longitude],
		          zoom: 14
				});
		        var size = 150;
		        map.addControl(new mapboxgl.NavigationControl());
		        map.addControl(new mapboxgl.FullscreenControl());
		        map.on('load', function() {
				map.addLayer({
				'id': 'off-leash-areas',
				'type': 'symbol',
				// data from opendata.cityofboise.org/
				'source': {
				'type': 'geojson',
				'data': 'https://docs.mapbox.com/mapbox-gl-js/assets/boise.geojson'

				},
				"layout": {
				"icon-image": 'dog-park-11',
				"text-field": ['format',
				['upcase', ['get', 'FacilityName']], { 'font-scale': .8 },
				'\n', {},
				['downcase', ['get', 'Comments']], { 'font-scale': .6 }],
				"text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
				"text-offset": [0, 0.6],
				"text-anchor": "top"
				}
				});
		 
				});


				  var pulsingDot = {
				width: size,
				height: size,
				data: new Uint8Array(size * size * 4),
				 
				// get rendering context for the map canvas when layer is added to the map
				onAdd: function() {
				var canvas = document.createElement('canvas');
				canvas.width = this.width;
				canvas.height = this.height;
				this.context = canvas.getContext('2d');
				},
				 
				// called once before every frame where the icon will be used
				render: function() {
				var duration = 1000;
				var t = (performance.now() % duration) / duration;
				 
				var radius = size / 2 * 0.3;
				var outerRadius = size / 2 * 0.7 * t + radius;
				var context = this.context;
				 
				// draw outer circle
				context.clearRect(0, 0, this.width, this.height);
				context.beginPath();
				context.arc(this.width / 2, this.height / 2, outerRadius, 0, Math.PI * 2);
				context.fillStyle = 'rgba(255, 200, 200,' + (1 - t) + ')';
				context.fill();
				 
				// draw inner circle
				context.beginPath();
				context.arc(this.width / 2, this.height / 2, radius, 0, Math.PI * 2);
				context.fillStyle = 'rgba(255, 100, 100, 1)';
				context.strokeStyle = 'white';
				context.lineWidth = 2 + 4 * (1 - t);
				context.fill();
				context.stroke();
				 
				// update this image's data with data from the canvas
				this.data = context.getImageData(0, 0, this.width, this.height).data;
				 
				// continuously repaint the map, resulting in the smooth animation of the dot
				map.triggerRepaint();
				 
				// return `true` to let the map know that the image was updated
				return true;
				}
				};

				map.on('load', function () {
				 
				map.addImage('pulsing-dot', pulsingDot, { pixelRatio: 2 });
				 
				map.addLayer({
				"id": "points",
				"type": "symbol",
				"source": {
				"type": "geojson",
				"data": {
				"type": "FeatureCollection",
				"features": [{
				"type": "Feature",
				"geometry": {
				"type": "Point",
				"coordinates": [ latitude,longitude]
				}
				}]
				}
				},
				"layout": {
				"icon-image": "pulsing-dot"
				}
				});
				});
        
 				
 			},
 			 error: function () {
       			 console.log("error");
    		}
  
 	});

  	
         
});

});